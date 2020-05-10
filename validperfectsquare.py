# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        
        left,right=2,num//2
        
        while left<=right:
            mid=(left+right)//2
            sqr=mid**2
            if sqr==num:
                return True
            elif sqr>num:
                right=mid-1
            else:
                left=mid+1
        return False
        
        