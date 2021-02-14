nums = [3, 2, 2, 3]
val = 3
# Output: 2, nums = [2,2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


# Output: 5, nums = [0,1,4,0,3]


class Solution:
    def removeElement(self, nums, val) -> int:
        for i in range(len([i for i in nums if i == val])): nums.remove(val)
        return len(nums)


# check
sol = Solution()
print(sol.removeElement(nums, val), nums)

# Runtime: 28 ms, faster than 93.18% of Python3 online submissions for Remove Element.
# Memory Usage: 14.4 MB, less than 16.68% of Python3 online submissions for Remove Element.
