
def countWords(text):
    text_words = text.split()
    return len(text_words)

def countCharactersByType(text):
    characters = {}
    for o_char in text:
        char = str.lower(o_char)
        if char in characters:
            characters[char]+=1
        else:
            characters[char]= 1
    return characters


def main():
    with open("books/frankenstein.txt") as f:
        file_contents= f.read()
        wordsCount=countWords(file_contents)
        charCountByType=countCharactersByType(file_contents)

        print('--- Begin report of books/frankenstein.txt ---')
        print(wordsCount,"words found in the document")
        for char in list(charCountByType.keys()):
            if char.isalpha():
                print(f"The {char} character was found {charCountByType[char]} times")
        print('--- End report ---')


main()
