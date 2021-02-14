nums = [1, 3, 5, 6]
target = 5
# Output: 2
nums = [1, 3, 5, 6]
target = 2
# Output: 1
nums = [1, 3, 5, 6]
target = 7
# Output: 4
nums = [1, 3, 5, 6]
target = 0
# Output: 0
nums = [1]
target = 0


# Output: 0


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[::-1][0] < target: return len(nums)
        for v, i in enumerate(nums):
            if target <= i:
                return v


sol = Solution()
sol.searchInsert(nums, target)

# Runtime: 48 ms, faster than 76.74% of Python3 online submissions for Search Insert Position.
# Memory Usage: 15.1 MB, less than 56.25% of Python3 online submissions for Search Insert Position.
