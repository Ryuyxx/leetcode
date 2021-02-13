s = "Hello World"
# Output: 5
s = " "
# Output: 0



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        import re
        if s.strip() == '': return 0
        else: return len(re.findall(r'\S+', s)[-1])



sol = Solution()
sol.lengthOfLastWord(s)


# fastest sol
# return len(s.strip().split(' ')[-1])
