'''
calculate the fibonacci of a given number
Fibonnaci: a basically built from the simple growth rule: 
Each value is the sum of the previous two
'''

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    
    return a


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))

    