with open('/home/lisa/workspace/github.com/elisia-y/bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()


def count_words (book):
    words = book.split()
    num_words = len(words)

    print ("--- Begin report of books/frankenstein.txt ---")
    print(num_words, " words found in the document")
    print("")


def count_charc(book):
    dict_charcs = dict()
    lower_charcs = book.lower()
    charc_without_space = lower_charcs.split()
    for word in charc_without_space:
        for charc in word:
            if dict_charcs.get(charc, 0) == 0:
                dict_charcs[charc] = 0
            dict_charcs[charc] += 1
    
    for charc in dict_charcs:
        print(f"The {charc} character was found {dict_charcs.get(charc)} times")
    
    print("")
    print ("--- End report ---")
    


count_words(file_contents)
count_charc(file_contents)

def main():
    return

main()