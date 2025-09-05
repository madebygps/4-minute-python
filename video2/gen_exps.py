with open('words.txt') as wf:
    for word in (w.upper() for line in wf for w in line.split() if len(w) > 13):
        print(word)