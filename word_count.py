from collections import Counter

sentence = "the cat sat on the mat the cat sat"
words = sentence.lower().split()

word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")