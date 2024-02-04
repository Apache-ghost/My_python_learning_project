def replace_word():
    string="Do you know that kotlin is modern programming language compare to java"
    print(string)
    word_to_replace=input("Enter the word to replace: ")
    word_replacement=input("Enter the word replacement: ")
    print(string.replace(word_to_replace,word_replacement))

replace_word()