def main():
    word_dictionary={
        'hi':'a way of greeting',
        'eyes':'a way of seeing',
        'close':'a way of restricting access for example'
    }
    while True:
        word=input("enter a word: ")
        if word=='':
            
            break
        if word in word_dictionary:
            print(word,':',word_dictionary[word])
main()