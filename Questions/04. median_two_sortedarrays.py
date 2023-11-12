def findMedianSortedArrays(nums1, nums2):
    merged_array = nums1 + nums2
    merged_array.sort()
    Lo = 0
    Hi = len(merged_array)
    if len(merged_array) == 1:
        return merged_array[0]
    if len(merged_array) % 2 != 0:
        mid = (Lo + Hi) // 2
        return merged_array[mid]
    else:
        mid1 = (Lo + len(merged_array)) // 2
        mid2 = mid1 - 1
        return ((merged_array[mid1] + merged_array[mid2]) / 2)
        