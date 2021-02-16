"""
2021/02/11

35. Search Insert Position
[Solved]
Runtime: 48 ms, faster than 76.74% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.1 MB, less than 56.25% of Python3 online submissions for Search Insert Position.
"""

import unittest


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[::-1][0] < target: return len(nums)
        for v, i in enumerate(nums):
            if target <= i:
                return v



class Test(unittest.TestCase):
    def test1(self):
        i = [1, 3, 5, 6]
        ii= 5
        e = 2
        self.assertEqual(e, Solution().searchInsert(i, ii))
    def test2(self):
        i = [1, 3, 5, 6]
        ii= 2
        e = 1
        self.assertEqual(e, Solution().searchInsert(i, ii))
    def test3(self):
        i = [1, 3, 5, 6]
        ii= 7
        e = 4
        self.assertEqual(e, Solution().searchInsert(i, ii))
    def test4(self):
        i = [1, 3, 5, 6]
        ii= 0
        e = 0
        self.assertEqual(e, Solution().searchInsert(i, ii))
    def test5(self):
        i = [1]
        ii= 0
        e = 0
        self.assertEqual(e, Solution().searchInsert(i, ii))


if __name__ == "__main__":
    unittest.main()
