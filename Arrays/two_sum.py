# Runtime: 1771 ms, faster than 21% of Python3 submissions
# Memory Usage: 18 MB, beats 87% of Python3 submissions

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
#                return nums
                if target == nums[i]+nums[j]:
                    answer = [i,j]
                    return answer
