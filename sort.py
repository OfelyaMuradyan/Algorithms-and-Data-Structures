#####
def insertion(arr):
    
    for i in range(1,len(arr)):
        j = i-1
        
        while j >= 0 and arr[j] >= arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    
    return arr

print(insertion([99, 88, 77, 66, 55, 111]))


######
def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    
    return start

print(binary_search([1, 5, 45, 79, 89, 96, 101], 96))


#####
def binary_search_recursive(arr, target, left, right):
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        right = mid - 1
        return binary_search_recursive(arr, target, left, right)
    
    else:
        left = mid + 1
        return binary_search_recursive(arr, target, left, right)

print(binary_search_recursive([1, 5, 45, 79, 89, 96, 101], 1, 0, 6))
 

#####
def selection_sort(arr):
    
    min_index = 0
    for i in range(len(arr) - 1):
        min_index = i
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr                                                             #####hertov min- ery piti gtnenq u dnenq iranc dirqerum

print(selection_sort([2, 7, 3, 9, 5, 1, 0]))  

#####
def bubble_sort(arr):

    for i in range(len(arr)):
        flagg = False
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                flagg = True
        if flagg:
            print(1)                    #ete stegh chmtav, complexity O(n)
            break       
    return arr

print(bubble_sort([77, 88, 99, 111]))
#print(bubble_sort([99, 88, 77, 66, 55, 111]))

######
def counting_sort(arr):
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]

    count = [0] * (max + 1)
    output = [0] * len(arr)

    for i in arr:
        count[i] += 1

    print(count)

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    print(count)

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    print(output)

counting_sort([1,0,5,3,4,2,8,8,8,7,1])



#######merge_sort

def merge(arr, left, mid, right):
    size1 = mid - left + 1
    size2 = right - mid

    leftArr = [0] * size1
    rightArr = [0] * size2

    for i in range(size1):
        leftArr[i] = arr[i + left] 

    for j in range(size2):
        rightArr[j] = arr[mid + j + 1]

    i = 0
    j = 0
    k = left

    while i < size1 and j < size2:
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while(i < size1):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while(j < size2):
        arr[k] = rightArr[j]
        j += 1
        k += 1

    
def mergeSort(arr, left, right):
    if left < right:
        mid = (right + left) // 2

        mergeSort(arr, mid+1, right)
        mergeSort(arr, left, mid)
        merge(arr, left, mid, right)

arr = [54, 27, 63, 1, 11, 45]
n = len(arr)
mergeSort(arr, 0, n-1)
print(arr)




######## quick sort

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= high and arr[i] < pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)  
        quickSort(arr, pi + 1, high)  

arr = [54, 27, 63, 1, 11, 45]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)


import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print(arr)



def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def partition(arr, low, high):
    median_index = median_of_three(arr, low, high)
    arr[median_index], arr[high] = arr[high], arr[median_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print(arr)
