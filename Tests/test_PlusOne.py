import unittest
import sys
sys.path.append('../')
from Problems import PlusOne



class TestPlusOne(unittest.TestCase):
    def test1(self):
        i = [1, 2, 3]
        e = [1, 2, 4]
        self.assertEqual(e, PlusOne.Solution().plusOne(i))
    def test2(self):
        i = [4, 3, 2, 1]
        e = [4, 3, 2, 2]
        self.assertEqual(e, PlusOne.Solution().plusOne(i))
    def test3(self):
        i = [0]
        e = [1]
        self.assertEqual(e, PlusOne.Solution().plusOne(i))




if __name__ == "__main__":
    unittest.main()
