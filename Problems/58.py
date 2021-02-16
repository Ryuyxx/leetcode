"""
2021/2/13

58. Length of Last Word
[Solved]
Runtime: 24 ms, faster than 95.53% of Python3 online submissions for Length of Last Word.
Memory Usage: 14.4 MB, less than 39.49% of Python3 online submissions for Length of Last Word.

Better 1 line sol
return len(s.strip().split(' ')[-1])
"""

import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        import re
        if s.strip() == '': return 0
        else: return len(re.findall(r'\S+', s)[-1])


class Test(unittest.TestCase):
    def test1(self):
        i = "Hello World"
        e = 5
        self.assertEqual(e, Solution().lengthOfLastWord(i))
    def test2(self):
        i = " "
        e = 0
        self.assertEqual(e, Solution().lengthOfLastWord(i))



if __name__ == "__main__":
    unittest.main()
