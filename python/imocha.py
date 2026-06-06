# # SORT ARRAY

# # P:[] = [1,3,...n] 
# # K:int

# #operations: 
# # ->choose any consecutive segment of at most K elements of the permutation P: 
# # sort in increasing order: Find the min no.of operations required to sort the array in increasing order
# # ->
# # ->

# # ->

# from itertools import permutations
# _list = [2, 6, 4, 3, 1, 5]
# k = 4
# n = len(_list)
# # print(list(permutations(_list)))

# def all_segment_permutations(l,k, n):
#     result = []

#     for length in range(1, k+1):
#         for start in range(n - length + 1):
#             segment = l[start:start+length]
#             result.append({
#                 "segment": segment,
#             })
    
#     return result

# for element in all_segment_permutations(_list,k,n):
#     print(f"segment:{element["segment"]}")
#     print()
    

# [2, 6, 4, 3, 1, 5]

# # 4, 3, 1, 5 -> 1,3,4,5 : I
# 2,6,1,3,4,5

# #2,6,1 -> 1,2,6 : II
# 1,2,6,3,4,5

# #6,3,4,5 ->3,4,5,6 : II
# 1,2,3,4,5,6


def min_sort_operations(l, k, n):
    arr = l[:]
    operations = 0

    i = 0
    while i < n:
        if arr[i] != i + 1:
            end = min(i + k, n)
            segment_before = arr[i:end]
            segment_after = sorted(segment_before)

            if segment_before == segment_after:
                # No progress possible, move to the next position
                i += 1
                continue

            # Apply the sort operation
            arr[i:end] = segment_after
            operations += 1

            # Print debug info
            print(f"Operation {operations}: sort arr[{i}:{end}] -> {segment_before} -> {segment_after}")
            print(f"Array now: {arr}")
            
            # Stay at same i to check if it's now correct
        else:
            i += 1  # Move to next element if correct

    return operations



_list = [2, 6, 4, 3, 1, 5]
k = 4
n = len(_list)

print(min_sort_operations(_list, k, n))  # Output: 3
