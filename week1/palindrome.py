#Write a program to check if a string is a palindrome or not.

print("Enter word: ")
word = input()

if word == word[::-1]:
    print(word, 'is a palindrome')
else:
     print(word, 'is not a palindrome')
