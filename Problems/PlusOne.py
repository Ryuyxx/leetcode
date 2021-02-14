"""
2021/2/14

[Solved]
Runtime: 20 ms, faster than 99.71% of Python3 online submissions for Plus One.
Memory Usage: 14.2 MB, less than 49.92% of Python3 online submissions for Plus One.
"""



class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(i) for i in str(int(''.join(map(str, digits)))+1)]
