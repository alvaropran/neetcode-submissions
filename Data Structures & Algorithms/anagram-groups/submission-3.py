class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            # FIXED: Iterate over every character 'c' in string 's'
            for c in s: 
                count[ord(c) - ord("a")] += 1

            # Convert list to tuple to use as a dictionary key
            res[tuple(count)].append(s)
            
        return list(res.values())