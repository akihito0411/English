import nltk
from nltk.tokenize import word_tokenize
from datetime import datetime

#nltkのデータセットをダウンロード(初回のみ)
nltk.download('punkt')

def read_file(file_path):
    with open(file_path,'r',encoding = 'utf-8') as file:
        return file.read()
    
def search_context(text, search_term, context_window = 5):
    words = word_tokenize(text)
    results = []
    for i, word in enumerate(words): #enumerateを使うことでiには数字がwordには文字が入る
        if word.lower() == search_term.lower(): #lowerを使うことですべて小文字になる
            left_context = ' '.join(words[max(0, i - context_window):i])
            right_context = ' '.join(words[i + 1:min(len(words),i + 1 + context_window)])
            results.append((left_context,search_term,right_context))

    return results

def save(results, term , initials):
    case_number = str(len(results)).zfill(3)
    current_time = datetime.now().strftime("%Y%m%d-%H%M")
    filename = f"{case_number}-{current_time}-{initials}-{term}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for left, term, right in results:
            file.write(f"{left} \033[91m{term}\033[0m {right}\n")

for i in range(1,11):
    text = read_file(f"generated_{i}.txt")
    results = search_context(text,'bananas')
    save(results,'bananas','STU')

# 使用例1
#text = read_file('example_text.txt')  # ここにテキストファイルのパスを指定
#results = search_word_in_context(text, 'bananas')
#save_results(results, 'bananas', 'STU')

# 使用例2
#text = read_file('threat_email.txt')  # ここに脅迫メールのテキストファイルのパスを指定
#results = search_word_in_context(text, 'idiosyncratic_term')  # 特異な言葉を指定
#save_results(results, 'idiosyncratic_term', 'AUTH')

