"""
2021/02/18

[Solved]
フィボナッチ数列
Runtime: 28 ms, faster than 82.58% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.2 MB, less than 47.43% of Python3 online submissions for Climbing Stairs.
"""

import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 0
        for x in range(n): a, b = a+b, a
        return a

class Test(unittest.TestCase):
    def test1(self):
        i = 2
        e = 2
        self.assertEqual(e, Solution().climbStairs(i))
    def test2(self):
        i = 3
        e = 3
        self.assertEqual(e, Solution().climbStairs(i))
    def test3(self):
        i = 4
        e = 5
        self.assertEqual(e, Solution().climbStairs(i))


if __name__ == "__main__":
    unittest.main()
