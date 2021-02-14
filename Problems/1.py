# nums = [2,7,11,15]
# target = 9
# Output: [0,1]

# nums = [3,2,4]
# target = 6
# # Output: [1,2]
#
# nums = [3,3]
# target = 6
# # Output: [0,1]

nums = [2, 5, 5, 11]
target = 10

for v, i in enumerate(nums):
    for j in range(len(nums)):
        if j == 0 or j == v: continue
        if i + nums[j] == target:
            print([v, j])
            break
    else:
        continue
    break
