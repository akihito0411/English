import random
import os

def generate_sentence():
    subjects = ["The monkeys","A group of friends","The soccer player","An adventuros explorer"]
    verb = ["happily feasted on", "devoured","enjoyed","robed"]
    objects = ["ripe bananas","delicious fruits","tasty snacks","nutritious treats","bad smell"]
    locations = ["swinging from tree to tree in the lush jungle.","at the picnic table in the park.","in the kitchen of the resutaurant.","during their hike in the mountains."]

    subjects = random.choice(subjects)
    verb = random.choice(verb)
    obj = random.choice(objects)
    locations = random.choice(locations)

    sentence = f"{subjects} {verb} {obj}, {locations}"
    return sentence

#生成された文をファイルに書き込む
def write_file(filename, num_sentences): #num_sentencesには何行書き込みたいかを入力する
    with open(filename,'w') as file:
        for _ in range(num_sentences):
            sentence = generate_sentence()
            file.write(sentence + ' ')

#10個のテキストファイルを自動生成する
def generate_text_files():
    for i in range(1,11):
        filename = f"file_{i}.txt"
        write_file(filename,3) #各ファイルに3行の文を書き込む

def main():
    generate_text_files()

if (__name__ == "__main__"):
    main()