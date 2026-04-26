class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: 
            count = [0] * 26 #26 letters to iterate through
            for c in s: 
                count[ord(c) - ord('a')] += 1 #the count gets the direct index of whatever the difference is, adds one 
            #now count looks like [1,0,0,1 etc]
            res[tuple(count)].append(s) #restuple count acts as a key to uniquely identify each [0,1,1], tuple since its immutable
        return list(res.values()) # we do .values since we only care about the word, not the key, and the list to make it like the desired outcome