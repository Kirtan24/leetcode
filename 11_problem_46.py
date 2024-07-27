class Solution(object):
    def permute(self, nums):
        if not nums:
            return []
        
        result = [[]]
        for num in nums:
            result = [prefix[:i] + [num] + prefix[i:] for prefix in result for i in range(len(prefix) + 1)]
        return result
    
sol = Solution()
r = sol.permute([1,2,3])
print(r)