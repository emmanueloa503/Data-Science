
#Write a program that takes a word as an input and print the number of vowels in the word.
#wordCount.py

print("Enter word: ")
word = input()

print("WORD = ", word)

vowels = ['a', 'e', 'i', 'o', 'u']
count=0

for char in word.lower():
    if char in vowels:
        count += 1
    
print ("number vovels: ", count)