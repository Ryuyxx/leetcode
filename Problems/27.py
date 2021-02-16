"""
2021/02/09

27. Remove Element
[Solved]
Runtime: 28 ms, faster than 93.18% of Python3 online submissions for Remove Element.
Memory Usage: 14.4 MB, less than 16.68% of Python3 online submissions for Remove Element.
"""

import unittest


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len([i for i in nums if i == val])): nums.remove(val)
        return len(nums)



class Test(unittest.TestCase):
    def test1(self):
        i = [3, 2, 2, 3]
        ii = 3
        e = 2
        # nums = [2,2]
        self.assertEqual(e, Solution().removeElement(i, ii))
    def test2(self):
        i =  [0, 1, 2, 2, 3, 0, 4, 2]
        ii = 2
        e = 5
        # nums = [0,1,4,0,3]
        self.assertEqual(e, Solution().removeElement(i, ii))



if __name__ == "__main__":
    unittest.main()
