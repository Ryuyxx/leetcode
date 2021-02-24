"""
2021/02/22

88. Merge Sorted Array
[Solved]
Runtime: 32 ms, faster than 91.82% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.2 MB, less than 88.26% of Python3 online submissions for Merge Sorted Array.
"""

import unittest


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:], nums2[n:]
        nums1.extend(nums2)
        nums1.sort()

class Test(unittest.TestCase):
    def test1(self):
        i = [1,2,3,0,0,0]
        ii = 3
        i2 = [2,5,6]
        ii2 = 3
        e = [1,2,2,3,5,6]
        self.assertEqual(Solution().merge(i, ii, i2, ii2), e)
    def test2(self):
        i = [1]
        ii = 1
        i2 = []
        ii2 = 0
        e = [1]
        self.assertEqual(Solution().merge(i, ii, i2, ii2), e)



if __name__ == "__main__":
    unittest.main()
