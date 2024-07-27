class Solution(object):
    def letterCombinations(self, digits):
        digit_to_chars = ['','','abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = ['']
        if not digits:
            return []
        for i in digits:
            letters = digit_to_chars[int(i)]
            result = [(prefix + letter) for prefix in result for letter in letters]
        return result
    
sol = Solution()
r = sol.letterCombinations("7777")
print(r)