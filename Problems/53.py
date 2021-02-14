nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
nums = [1]
# Output: 1
# nums = [0]
# Output: 0
# nums = [-1]
# Output: -1
nums = [-100000]


# Output: -100000


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        c, g = nums[0], nums[0]
        for i in nums[1:]:
            c = max(c + i, i)
            g = max(c, g)
        return g


sol = Solution()
sol.maxSubArray(nums)
