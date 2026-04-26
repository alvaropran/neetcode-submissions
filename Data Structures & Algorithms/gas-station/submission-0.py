class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # if this isn't the case, a solution definitely exists
            return -1
        
        total = 0 
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # diff array

            if total < 0:
                total = 0
                res = i + 1 # move forwards

        return res