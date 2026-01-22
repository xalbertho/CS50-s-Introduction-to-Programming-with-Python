# for week 5

def main():
    word=input('Input: ')
    print(shorten(word))


def shorten(word):
    #word=word.lower()
    word_new=''
    for letra in word:
        if letra not in {'a','e','i','o','u','A','E','I','O','U'}:
            word_new+=letra
    return word_new
   

if __name__=="__main__":
    main()