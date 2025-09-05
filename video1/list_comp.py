with open('words.txt') as word_file:
    words = [word.upper() for line in word_file for word in line.split() if len(word) > 13]

for word in words:
    print(word)