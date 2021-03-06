# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
# then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        temp = nums[:]
        temp.sort()
        lis = []
        
        for i in range(len(nums)):
    
            if temp[i] != nums[i]:
                lis.append(i)
                
        if len(lis) == 0:
            return 0
        else:
            return lis[-1]-lis[0] + 1
