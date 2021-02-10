# s = "III"
# 3

# s = "IV"
# 4

# s = "IX"
# 9

# s = "LVIII"
# 58

# s = "MCMXCIV"
# 1994

d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
if not 1 <= len(s) <= 15: print(0)
ans = 0
for i, v in enumerate(s):
    if i < len(s)-1 and d[v] < d[s[i+1]]:
        ans -= d[v]
    else:
        ans += d[v]

print(ans)
