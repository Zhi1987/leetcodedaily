# https://leetcode.com/problems/matchsticks-to-square/

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        
        total = sum(nums)
        if total%4 != 0: return False
        
        l = len(nums)
        tgt = total//4
        nums.sort(reverse=True)
        sums = [0]*4
        memo = {}
        
        return self.dfs(l, sums, nums, tgt, 0, memo)
    
    def dfs(self,l, sums, nums, tgt, idx, memo):
        
        if l == idx:
            return sums[1] == sums[2] == sums[3] == tgt
        
        if (idx, tuple(sorted(sums))) in memo:
            return memo[(idx, tuple(sorted(sums)))]
        
        for i in range(4):      
            if sums[i] + nums[idx] <= tgt:
                sums[i]+=nums[idx]
                if self.dfs(l,sums, nums, tgt, idx+1, memo):
                    return True         
                sums[i]-=nums[idx]
                
        memo[(idx, tuple(sorted(sums)))] = False        
        return False
