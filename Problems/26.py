"""
2021/02/07

26. Remove Duplicates from Sorted Array
重複を消して残った個数を返す
(なお、numsは後から参照されるため、破壊的変更を内部でする必要あり)

[Solved]
Runtime: 100 ms, faster than 34.26% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.9 MB, less than 56.07% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

import unittest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


class Test(unittest.TestCase):
    def test1(self):
        i =  [1, 1, 2]
        e = 2
        # nums = [1,2]
        self.assertEqual(e, Solution().removeDuplicates(i))
    def test2(self):
        i = [0,0,1,1,1,2,2,3,3,4]
        e = 5
        # nums = [0,1,2,3,4]
        self.assertEqual(e, Solution().removeDuplicates(i))


if __name__ == "__main__":
    unittest.main()
