x = 121
# true
#
# x = -121
# false
#
# x = 10
# false
#
# x = -101
# false
#
# x = 2147483648
# x = -2147483650

# if not -2**31-1 <= x <= 2**31-1 : print(0)
return list(str(x)) == list(str(x))[::-1]
