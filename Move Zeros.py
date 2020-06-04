class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
                
                """
                Take two pointer i and j and increase i if and only i f  swapping is 
                performed on nums[i] and nums[j].
                swapping is performed with a non-zero and a zero value as per question.
                
                """
