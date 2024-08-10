from typing import List 
from math import sqrt

def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = target - nums[i]

        if (target - nums[i]) in dict.keys():
            k = nums.index(target - nums[i])
            if k != i:
                return [k, i]
    
    return -1



def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0

    j = 0

    for i in range(1, len(prices)):
        if prices[i] < prices[j]:
            j = i
            continue

        if prices[i] - prices[j] > maxProfit:
            maxProfit = prices[i] - prices[j]
    return maxProfit




def containsDuplicate(self, nums: List[int]) -> bool:
    di = {}
    for i in nums:
        if i not in di:
            di[i] = 0
        else:
            di[i] += 1
            return True
    return False




def getSum(self, a: int, b: int) -> int:
    s = a**2 + 2*a*b + b**2
    if a > 0 and b > 0:
        return int(sqrt(s))
    elif a == 0 or b == 0:
        if a == 0:
            return b
        else:
            return a
    elif a * b < 0:
        if min(abs(a), abs(b)) < a:
            return int(a/abs(a) * sqrt(s))
        else:
            return int(b/abs(b)* sqrt(s))
    else:
        return int(-sqrt(s))
    



def maxSubArray(self, nums: List[int]) -> int:
    max = float('-inf')  
    max_end = 0
    for i in range(len(nums)):
        max_end = max_end + nums[i]
        if max < max_end:
            max = max_end
        if max_end < 0:
            max_end = 0
    return max


def findShortestSubArray(self, nums: List[int]) -> int:
    di = {}
    maxx_ls = []
    for i in nums:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    max_freq = max(di.values())
    for i in di.keys():
        if di[i] == max_freq:
            maxx_ls.append(i)
    print(di)

    min = len(nums)
    
    for maxx in maxx_ls:
        max_f = max_freq
        seq = []
        for i in range(len(nums)):
            if nums[i] == maxx:
                idx = i
                break

        while(max_f != 0):
            seq.append(nums[idx])
            if nums[idx] == maxx:
                max_f -= 1
            idx += 1
        
        if len(seq) < min:
            min = len(seq)
    return min




def sortedSquares(self, nums: List[int]) -> List[int]:
    ls = [abs(i)**2 for i in nums]
    ls.sort()
    return ls
