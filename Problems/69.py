"""
2021/02/18

[Solved]
Runtime: 24 ms, faster than 98.69% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.3 MB, less than 43.27% of Python3 online submissions for Sqrt(x).
"""

import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(pow(x, 1/2))



class Test(unittest.TestCase):
    def test1(self):
        i = 4
        e = 2
        self.assertEqual(e, Solution().mySqrt(i))
    def test2(self):
        i = 8
        e = 2
        self.assertEqual(e, Solution().mySqrt(i))


if __name__ == "__main__":
    unittest.main()
