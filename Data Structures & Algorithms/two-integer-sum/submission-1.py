class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums): 
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference], i] # current index of the difference in hashmap
            hashmap[num] = i 


            
        
            