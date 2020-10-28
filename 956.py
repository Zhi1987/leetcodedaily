"""
https://leetcode.com/problems/tallest-billboard/
https://leetcode.com/problems/tallest-billboard/discuss/204160/C%2B%2B-16-ms-DFS-%2B-memo
"""
class Solution(object):
    def tallestBillboard(self, rods):
        mem = {}
        return self.dfs(0,0,0,mem,rods)
    
    def dfs(self,i,s1,s2,mem,rods):
        if i == len(rods):
            return s1 if (s1 == s2) else -1
        
        if (i,abs(s1 - s2)) not in mem:
            
            m = max(
            self.dfs(i + 1, s1 + rods[i], s2, mem, rods),
            self.dfs(i + 1, s1 , s2 + rods[i], mem, rods),
            self.dfs(i + 1, s1, s2, mem, rods))
            if m == -1:
                mem[(i,abs(s1-s2))] = -1
            else:
                mem[(i,abs(s1-s2))] = m - max(s1,s2)
        if mem[(i,abs(s1-s2))] != -1:
            return max(s1,s2) + mem[(i,abs(s1-s2))]
        else:
            return -1
