from collections import Counter

def most_common_word(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    word_count = Counter(words)
    most_common = word_count.most_common(1)
    if most_common:
        print("Most common word:", most_common[0][0])
        print("Count:", most_common[0][1])

