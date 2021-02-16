"""
2021/02/16

67. Add Binary
[Solved]
Runtime: 32 ms, faster than 77.81% of Python3 online submissions for Add Binary.
Memory Usage: 14.3 MB, less than 58.44% of Python3 online submissions for Add Binary.
"""

import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]


class Test(unittest.TestCase):
    def test1(self):
        i = "11"
        ii = "1"
        e = "100"
        self.assertEqual(e, Solution().addBinary(i, ii))
    def test2(self):
        i = "1010"
        ii = "1011"
        e = "10101"
        self.assertEqual(e, Solution().addBinary(i, ii))


if __name__ == "__main__":
    unittest.main()
