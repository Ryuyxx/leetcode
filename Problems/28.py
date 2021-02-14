haystack = "hello"
needle = "ll"
# Output: 2
haystack = "aaaaa"
needle = "bba"
# Output: -1
haystack = ""
needle = "a"


# Output: -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (haystack == "" and needle == "") or needle == "": return 0
        return haystack.find(needle)


sol = Solution()
sol.strStr(haystack, needle)

# Runtime: 32 ms, faster than 73.62% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.4 MB, less than 49.90% of Python3 online submissions for Implement strStr().
