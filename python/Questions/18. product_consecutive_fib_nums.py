def product_fib(_prod):
    if _prod == 0:
        return [0, 1, True]
    
    a,b = 0,1

    for _ in range(_prod):
        a,b = b, a+b
        sum = a* b

        if sum == _prod:
            return [a, b, True]
        
        if sum > _prod:
            return [a, b, False]


print(product_fib(0))
print(product_fib(714))
print(product_fib(4895))
print(product_fib(5895))
