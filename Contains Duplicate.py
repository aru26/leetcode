class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in range(len(nums)):
            if(nums[i] in a):
                return True
            else:
                a.add (nums[i])
        return False
             
        
