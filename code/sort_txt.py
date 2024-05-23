import nltk
from nltk.tokenize import word_tokenize

#nltkのデータセットをダウンロード(初回のみ)
nltk.download('punkt')

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
    with open("author_output.txt", 'w', encoding='latin-1') as file:
        for i in author_box:
            file.write(i)
            for count,word in token[:20]: #20個並べる token[:20]
                file.write(f"{word}:{count}\n")
                #print(f"{word}:{count}\n")

def main():
    author_box = ["AnwarKhoirul_20.txt", "AokiToshiaki_4.txt","AsanoFumihiko_1.txt","ChenJiageng_6.txt","CheongKaiYuen_1.txt","DangJiannwu_5.txt","DefagoXavier_1.txt","IkedaKokolo_2.txt","InoguchiYasushi_1.txt","MatsumotoTadashi_19.txt","WirelessComm_unknown.txt"]
    all_token = []

    for i in range(11):
        text = read_file(author_box[i])
        all_token.extend(sort_context(text))
    write_file(all_token,author_box)

if (__name__ == "__main__"):
    main()