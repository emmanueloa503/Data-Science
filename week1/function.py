#5) Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
#function.py


def sum_of_integers(a, b):
    sum = a + b
    return sum


print('Enter integer A: ')
A = int(input())
    
print('Enter integer B: ')
B = int(input())

print(A, '+', B, '= ', sum_of_integers(A, B))

