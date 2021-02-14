"""
2021/02/00

[Attempted]


Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
"""

import unittest


class Solution:
    def countAndSay(self, n: int) -> str:



class Test(unittest.TestCase):
    def test1(self):
        i = 1
        e = "1"
        self.assertEqual(e, Solution().countAndSay(i))
    def test2(self):
        i = 4
        e = "1211"
        self.assertEqual(e, Solution().countAndSay(i))
    def test3(self):
        i =
        e =
        self.assertEqual(e, Solution().countAndSay(i))
    def test4(self):
        i =
        e =
        self.assertEqual(e, Solution().countAndSay(i))


if __name__ == "__main__":
    unittest.main()
