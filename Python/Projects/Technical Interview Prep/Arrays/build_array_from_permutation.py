# Solution provided by IndecisionTree via LeetCode

from typing import List

def buildArray(nums: List[int]) ->List[int]:
    q = len(nums)

    for i in range(len(nums)):
        r = nums[i]
        b = nums[nums[i]] % q
        nums[i] = q * b + r
    
    for i in range(len(nums)):
        nums[i] = nums[i] // q
    
    return nums