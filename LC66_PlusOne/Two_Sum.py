class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for index,num in enumerate(nums):
            if target-num in result:
                return [index,result[target-num]]
            else:
                result[num]=index    