strs = ["flower","flow","flight"]
# "fl"

# strs = ["dog","racecar","car"]
# ""

p=""
if len(strs) == 0: return ""
for i in range(len(min(strs, key=len))):
    temp = [s for s in strs if s.startswith(p + strs[0][i])]
    if len(temp) == len(strs):
        p += strs[0][i]
    else:
        break

print(p)
