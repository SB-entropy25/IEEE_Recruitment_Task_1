
paragraph = input("input paragraph")
words = paragraph.split()

palindromes = []

for word in words:
    word_lower = word.lower()
    if word_lower == word_lower[::-1]:
        palindromes.append(word)

if palindromes:
    print("Palindromes:", ' '.join(palindromes))
else:
    print(0)
