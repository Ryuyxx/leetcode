"""
2021/02/24

136. Single Number
[Solved]
Runtime: 4008 ms, faster than 8.36% of Python3 online submissions for Single Number.
Memory Usage: 16.6 MB, less than 63.50% of Python3 online submissions for Single Number.
"""

import unittest


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums)==1:return nums[0]
        return [i for i in set(nums) if nums.count(i) == 1][0]



class Test(unittest.TestCase):
    def test1(self):
        i = [2,2,1]
        e = 1
        self.assertEqual(e, Solution().singleNumber(i))
    def test2(self):
        i = [4,1,2,1,2]
        e = 4
        self.assertEqual(e, Solution().singleNumber(i))
    def test3(self):
        i = [1]
        e = 1
        self.assertEqual(e, Solution().singleNumber(i))

if __name__ == "__main__":
    unittest.main()
