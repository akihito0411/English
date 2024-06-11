from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from collections import Counter
import re
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io

# nltkのデータセットをダウンロード（初回のみ）
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_word_counts():
    if 'files' not in request.files:
        return "No file part"
    files = request.files.getlist('files')
    if not files or all(file.filename == '' for file in files):
        return "No selected files"
    if any(not allowed_file(file.filename) for file in files):
        return "Invalid file type"

    action = request.form['action']
    keyword = request.form.get("search_word", "")
    if action == 'analyze':
        results = []
        for file in files:
            content = file.read().decode('latin-1')
            word_counts = sort_context(content)
            results.append((file.filename, word_counts))
        return render_template('index.html', action='analyze', results=results)

    elif action == 'identify':
        texts = [file.read().decode('latin-1') for file in files]
        similarities = identify(texts)
        return render_template('index.html', action='identify', similarities=similarities)
    
    elif action == 'search' and keyword:
        results = []
        for file in files:
            content = file.read().decode('utf-8')
            context = search_context(content, keyword)
            results.append((file.filename, context))
        return render_template('index.html', action='search', results=results)

    elif action == 'save':
        keyword = request.form.get("search_word", "")
        results = []
        for file in files:
            content = file.read().decode('utf-8')
            context = search_context(content, keyword)
            results.append((file.filename, context))
        
        output = io.StringIO()
        for filename, contexts in results:
            output.write(f"Results for {filename}\n")
            for left_context, search_term, right_context in contexts:
                output.write(f"{left_context} <strong>{search_term}</strong> {right_context}\n")
            output.write("\n")
        
        output.seek(0)
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/plain',
            as_attachment=True,
            download_name='search_results.txt'
        )

    return "Invalid action"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'txt'

def sort_context(text):
    words = word_tokenize(text)
    count = {}

    for word in words:
        if word in {",", ".", "?", "“", "”", "’", "!", ";", "=", ")", "("}:
            continue
        count[word] = count.get(word, 0) + 1

    sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts[:20]

def identify(texts):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
    tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
    cosine_similarities = cosine_similarity(tfidf_matrix)
    results = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            similarity = cosine_similarities[i, j]
            same_author = similarity > 0.2
            results.append((f"Text {i + 1} and Text {j + 1}", similarity, same_author))
    return results

def search_context(text, search_term, context_window=5):
    words = word_tokenize(text)
    results = []
    for i, word in enumerate(words):
        if word.lower() == search_term.lower():
            left_context = ' '.join(words[max(0, i - context_window):i])
            right_context = ' '.join(words[i + 1:min(len(words), i + 1 + context_window)])
            results.append((left_context, search_term, right_context))
    return results

if __name__ == '__main__':
    app.run(debug=True)
