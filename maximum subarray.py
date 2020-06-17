Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
==============================================================================================================================
method 1:
 class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #we are taking two varible total_sum and max_sum
    #total_sum will take care of sum till every index and max_sum will the max(total_sum, max_sum)
        total_sum = max_sum = nums[0]
        
     #in starting we are giving value to both total_sum and max_sum as value at index 0   
        for i in nums[1:]: #looping the array starting from index 1
            total_sum = max(i, total_sum + i) #computing total sum
            max_sum = max(total_sum, max_sum) # updating max_sum if total_sum is larger than max_sum
        return max_sum   
================================================================================================================================
method 2:

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                 nums[i] += nums[i-1]
       
        return max(nums)
        
