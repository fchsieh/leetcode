class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(remain, comb, start):
            if remain < 0: return
            if remain == 0: res.append(list(comb)) # answer found
                
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                # start backtracking
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
            
        backtrack(target, [], 0)
        return res