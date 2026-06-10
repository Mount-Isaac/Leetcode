import math 

def find_cube_number(cuberoot):
    
    # find square root & validate
    triagular_sum = math.isqrt(cuberoot)
    if triagular_sum ** 2 != cuberoot:
        return -1
    
    # find descriminat 
    descriminat = 1 + 8 * triagular_sum
    square_target = math.isqrt(descriminat)
    if square_target ** 2  != descriminat:
        return -1
    

    target = (square_target-1) // 2
    return target



print(find_cube_number(1071225))
print(find_cube_number(2205225))
print(find_cube_number(132425))