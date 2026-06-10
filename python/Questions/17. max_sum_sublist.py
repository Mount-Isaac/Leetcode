# using optimized solution 
# find the sum of the largest sublist in an arry
# return 0 if all nums are -ve else the sum


def max_sequence_sum(arr):
    current_sum, max_sum = 0,0

    for element in arr: # O(n)
        current_sum += element
        current_sum = max(0, current_sum) # factor in -ve numbers
        max_sum = max(current_sum, max_sum) # if new current sum > max_sum: swap vals
    
    return max_sum

    '''
    earlier on I had solved the sol using nested for loops but had a O(n)^2 
    as I had to add array slicing resulting to failed completion on large array lists

    variable intialization: takes constant time O(1)
    for loop takes runs exactly n times (n=length of the array)
    max calls inside: compares only individual nums & passing fixed args takes constant time O(1)

    Therefore: T(n) = C1 + n * C2
     :- drop constants for Big O leaving a linear time complexity of O(n)

     Similaliry, The S(n) is O(1) because the algorithm tracks two integer vars regardless of the size of n
    '''



print(max_sequence_sum([1,2,-2,-1,4,3,-3,2,3]))