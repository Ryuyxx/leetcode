"""
2021/02/21

83. Remove Duplicates from Sorted List
[Attempted]

"""

import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:





class Test(unittest.TestCase):
    def test1(self):
        i = ListNode(next=[1,1,2])
        e = ListNode(next=[1,2])
        self.assertEqual(e, Solution().deleteDuplicates(i))
    def test2(self):
        i = ListNode(next=[1,1,2,3,3])
        e = ListNode(next=[1,2,3])
        self.assertEqual(e, Solution().deleteDuplicates(i))



if __name__ == "__main__":
    unittest.main()
