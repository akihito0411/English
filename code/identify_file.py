import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#nltkのデータセットをダウンロード(初回のみ)
nltk.download('punkt')
nltk.download('stopwords')

#ファイルの読み込み
def read_file(file_path):
    with open(file_path,'r',encoding = 'latin-1') as file:
        return file.read()

 #ソート関数   
def sort_context(text):
    words = word_tokenize(text)#トークン毎に格納
    count = {}

    for word in words:#要らない単語をフィルタリング
        if word == "," or word == "." or word == "?" or word == "“" or word == "”" or word == "’" or word == "!" or word == ";" or word == "=" or word == ")" or word == "(":
            count[word] = 0
        else:
            count[word] = count.get(word,0)+1

    #頻出順にソート
    d = [(v, k) for k, v in count.items()]
    d.sort()
    d.reverse()

    return d[:20]

def write_file(token,author_box):
    start = 0
    end = 20
    with open("author_output.txt", 'w', encoding='latin-1') as file:
        for i in author_box:
            file.write(i)
            file.write("\n")
            #print(i)
            #print("\n")
            for count,word in token[start:end]: #20個並べる token[:20]
                file.write(f"{word}:{count}\n")
                #print(f"{word}:{count}\n")
            start = start + 20
            end = end + 20

def identify(file_paths):
    texts = [read_file(file_path) for file_path in file_paths]
    # TF-IDFベクトライザーの初期化
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))

    # テキストデータをTF-IDFベクトルに変換
    tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

    # コサイン類似度の計算
    cosine_similarities = cosine_similarity(tfidf_matrix)

    # 結果の表示
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            print(f"Similarity between text {i + 1} and text {j + 1}: {cosine_similarities[i, j]:.4f}")

    # 閾値を設定して同じ著者かどうかを判別
    threshold = 0.2
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            if cosine_similarities[i, j] > threshold:
                print(f"Text {i + 1} and Text {j + 1} are likely written by the same author.")
            else:
                print(f"Text {i + 1} and Text {j + 1} are likely written by different authors.")


def main():
    author_box = ["AnwarKhoirul_20.txt", "AokiToshiaki_4.txt","AsanoFumihiko_1.txt","ChenJiageng_6.txt","CheongKaiYuen_1.txt","DangJiannwu_5.txt","DefagoXavier_1.txt","IkedaKokolo_2.txt","InoguchiYasushi_1.txt","MatsumotoTadashi_19.txt","WirelessComm_unknown.txt","AnwarKhoirul_201.txt"]
    all_token = []
    author =[]

    for i in range(3):
        text = read_file(author_box[i])
        author.extend(text)
        all_token.extend(sort_context(text))
    #write_file(all_token,author_box)
    
    identify(author_box)

if (__name__ == "__main__"):
    main()