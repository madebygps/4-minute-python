def main():
   

    with open('words.txt') as wf, open('definitions.txt') as df:
        words = [word for line in wf for word in line.split()]
        definitions = [line.strip() for line in df]
    
    word_definitions = {word: definition for word, definition in zip(words, definitions)}
    print(word_definitions)
    
    
if __name__ == "__main__":
    main()
