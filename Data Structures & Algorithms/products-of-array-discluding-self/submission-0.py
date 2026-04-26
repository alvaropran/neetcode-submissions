class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1 #initial to keep it steady, start to end
        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 #initial to keep it steady, end to start
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix #prefix x postfix
            postfix *= nums[i]
        return res

        