method 1:
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result

method 2:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = []
        for i in range(len(num)):
            ans^=nnums[i]
