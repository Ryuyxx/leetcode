digits = [1, 2, 3]
# Output: [1, 2, 4]

# digits = [4, 3, 2, 1]
# Output: [4, 3, 2, 2]

# digits = [0]
# Output: [1]


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(i) for i in str(int(''.join(map(str, digits)))+1)]


sol = Solution()
print(sol.plusOne(digits))


# Runtime: 20 ms, faster than 99.71% of Python3 online submissions for Plus One.
# Memory Usage: 14.2 MB, less than 49.92% of Python3 online submissions for Plus One.


# My messy idea
# int(str(digits).translate(str.maketrans({'[': '', ']': '', ',':'', ' ':''}))) + 1
