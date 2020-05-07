# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            if dict[num]>len(nums)//2:
                return num
            else:
                dict[num]+=1

#optimized solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        
