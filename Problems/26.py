# 重複を消して残った個数を返す
# (なお、numsは後から参照されるため、破壊的変更を内部でする必要あり)
nums = [1,1,2]
# 2, nums = [1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
# 5, nums = [0,1,2,3,4]


i=0
while i < len(nums)-1:
    if nums[i] == nums[i+1]:
        del nums[i]
    else:
        i += 1
print(len(nums))
