
paragraph = input("input paragraph") #here we take input from user a paragraph of not more than 100 words as per q
words = paragraph.split()    #we create a list of all words present in the paragraph

palindromes = []

for word in words:        
    word_lower = word.lower()    #we convert everything in lower case for comaparision
    if word_lower == word_lower[::-1]:    #we are comparing whether the word and its reverse reading are same
        palindromes.append(word)    #if same we append our palindromes list.

if palindromes:    #if there are words in palindrome list it returns true and we enter if block
    print("Palindromes:", ' '.join(palindromes))
else:
    print(0)

