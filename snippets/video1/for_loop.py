words = []

with open('words.txt') as word_file:
    for line in word_file:
        for word in line.split():
            if len(word) > 13:
                words.append(word.upper())

for word in words:
    print(word)