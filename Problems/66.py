"""
2021/2/14

66. Plus One
[Solved]
Runtime: 20 ms, faster than 99.71% of Python3 online submissions for Plus One.
Memory Usage: 14.2 MB, less than 49.92% of Python3 online submissions for Plus One.
"""

import unittest


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(i) for i in str(int(''.join(map(str, digits)))+1)]



class Test(unittest.TestCase):
    def test1(self):
        i = [1, 2, 3]
        e = [1, 2, 4]
        self.assertEqual(e, Solution().plusOne(i))
    def test2(self):
        i = [4, 3, 2, 1]
        e = [4, 3, 2, 2]
        self.assertEqual(e, Solution().plusOne(i))
    def test3(self):
        i = [0]
        e = [1]
        self.assertEqual(e, Solution().plusOne(i))



if __name__ == "__main__":
    unittest.main()
