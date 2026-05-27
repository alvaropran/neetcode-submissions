class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses we visited
        visitSet = set()
        def dfs(crs):
            # base case
            if crs in visitSet:
                return False
            if preMap[crs] == []: # no prereq so valid
                return True

            # new course
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs) # we dont want to falsely say this is bad
            preMap[crs] = [] # marks as already solved and safe
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True

