def find_kth_smallest_recursively(arr, k):
    
    if k == 1:
        return min(arr)
    else:
        arr.remove(min(arr))
        return find_kth_smallest_recursively(arr, k - 1)


print(find_kth_smallest_recursively([5,9,3,2,1,4,555,7,80,79,45], 11))




def find_kth_biggest_recursively(arr, k):
    
    if k == 1:
        return max(arr)
    else:
        arr.remove(max(arr))
        return find_kth_biggest_recursively(arr, k - 1)


print(find_kth_biggest_recursively([5,9,3,2,1,4,555,7,80,79,45], 11))