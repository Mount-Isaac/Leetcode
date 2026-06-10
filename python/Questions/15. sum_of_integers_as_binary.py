def add_binary(a,b):
    total = a + b
    
    result = []
    while total > 0:
        result.append(str(total % 2))
        total //= 2 
    
    return ''.join(result[::-1]) # reverse the list


print(add_binary(2,0))
print(add_binary(1,3))
print(add_binary(20,35))
print(add_binary(2,11))
print(add_binary(2,30))