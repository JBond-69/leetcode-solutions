class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
#                return nums
                if target == nums[i]+nums[j]:
                    answer = [i,j]
                    return answer
