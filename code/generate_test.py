import random

def generate_sentence():
    subjects = ["The monkeys", "A group of friends", "The chef", "An adventurous explorer"]
    actions = ["happily feasted on", "devoured", "enjoyed", "savoured"]
    objects = ["ripe bananas", "delicious fruits", "tasty snacks", "nutritious treats"]
    locations = ["swinging from tree to tree in the lush jungle.", "at the picnic table in the park.", "in the kitchen of the restaurant.", "during their hike in the mountains."]

    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    location = random.choice(locations)

    sentence = f"{subject} {action} {obj}, {location}"
    return sentence

# 生成された文をテキストファイルに書き込む
def write_to_file(filename, num_sentences):
    with open(filename, 'w') as file:
        for _ in range(num_sentences):
            sentence = generate_sentence()
            file.write(sentence + '\n')

# ファイルに10行の文を書き込む例
for i in range(1,11):
    write_to_file(f'generated_{i}.txt', 10)
