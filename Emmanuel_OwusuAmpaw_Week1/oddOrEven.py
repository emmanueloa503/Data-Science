#Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for numbers in range(0, 21):
    if numbers % 2 ==0 :
        print(numbers, 'is even')
        
    else:
        print(numbers , 'is odd')