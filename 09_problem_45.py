class Solution(object):
    def jump(self, nums):
        n = len(nums)
        jumps = current_end = farthest = 0 
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        return jumps
nums = [2,3,1,1,4,5,6,1,0,0,1,6,6,7]
sol = Solution()
r = sol.jump(nums)
print(r)