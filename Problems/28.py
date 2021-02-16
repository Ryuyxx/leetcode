"""
2021/02/10

28. Implement strStr()
[Solved]
Runtime: 32 ms, faster than 73.62% of Python3 online submissions for Implement strStr().
Memory Usage: 14.4 MB, less than 49.90% of Python3 online submissions for Implement strStr().
"""

import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (haystack == "" and needle == "") or needle == "": return 0
        return haystack.find(needle)



class Test(unittest.TestCase):
    def test1(self):
        i = "hello"
        ii = "ll"
        e = 2
        self.assertEqual(e, Solution().strStr(i, ii))
    def test2(self):
        i =  "aaaaa"
        ii = "bba"
        e = -1
        self.assertEqual(e, Solution().strStr(i, ii))
    def test3(self):
        i = ""
        ii =  "a"
        e = -1
        self.assertEqual(e, Solution().strStr(i, ii))


if __name__ == "__main__":
    unittest.main()
