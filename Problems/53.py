"""
2021/02/12

53. Maximum Subarray
[Solved]
Runtime: 64 ms, faster than 78.58% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.9 MB, less than 82.12% of Python3 online submissions for Maximum Subarray.
"""

import unittest


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        c, g = nums[0], nums[0]
        for i in nums[1:]:
            c = max(c + i, i)
            g = max(c, g)
        return g


class Test(unittest.TestCase):
    def test1(self):
        i = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        e = 6
        self.assertEqual(e, Solution().maxSubArray(i))
    def test2(self):
        i = [1]
        e = 1
        self.assertEqual(e, Solution().maxSubArray(i))
    def test3(self):
        i = [0]
        e = 0
        self.assertEqual(e, Solution().maxSubArray(i))
    def test4(self):
        i = [-1]
        e = -1
        self.assertEqual(e, Solution().maxSubArray(i))
    def test4(self):
        i = [-100000]
        e = -100000
        self.assertEqual(e, Solution().maxSubArray(i))


if __name__ == "__main__":
    unittest.main()
