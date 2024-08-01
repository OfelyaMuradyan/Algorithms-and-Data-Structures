from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
    di = {}
    for i in nums:
        if i not in di:
            di[i] = 0
        else:
            di[i] += 1
            return True
    return False



def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]



def missingNumber(self, nums: List[int]) -> int:
    S1 = sum(nums)
    
    max_element = max(nums)
    S2 = max_element * (max_element + 1) // 2  

    if S1 == S2:
        if 0 not in nums:
            return 0
        return max_element + 1
    else:
        return S2 - S1
    


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    for i in set(nums1):
        if i in nums2:
            result.append(i) 
    return result



def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1) - 1, -1, -1):
        if nums1[i] != 0 or len(nums1) == m:
            break
        else:
            nums1.pop(i)        
    
    if n == 0:
        return nums1
    if m == 0:
        for i in nums2:
            nums1.append(i)
        return nums1
    
    j1 = 0
    j2 = 0

    while j2 != n:
        if nums1[j1] < nums2[j2]:
            j1 += 1
            if j1 == len(nums1):
                for i in nums2[j2:]:
                    nums1.append(i)
                break
        else:
            nums1.insert(j1, nums2[j2])
            j1 += 1
            j2 += 1
    return nums1



def sortSentence(self, s: str) -> str:
    dict = {}
    k = 0
    for i in range(len(s)):
        if s[i] == " ":
            dict[int(s[i - 1])] = s[k:i-1]
            k = (i + 1)
    dict[int(s[-1])] = s[k:len(s) - 1]
    print(dict)

    st = ""
    for i in range(1,len(dict.keys())+1):
        st += (dict[i] + " ")
    
    return st[:-1]




def frequencySort(self, nums: List[int]) -> List[int]:
    di = {}
    res = []
    nums.sort(reverse = True)
    
    for i in nums:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    
    ls = list(di.values())
    ls.sort()

    for i in ls:

        position = list(di.values()).index(i)
        while i > 0:
            element = list(di.keys())[position]
            res.append(element)
            i -= 1
        di.pop(element)
            
    return res