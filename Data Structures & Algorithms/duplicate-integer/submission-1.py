class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True
            # Our goal is to add this
            hashset.add(n)
        return False
            
