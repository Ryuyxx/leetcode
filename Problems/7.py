# x = 123
# 321

# x = -123
# -321

# x = 210
# 21

# x = 0
# 0

# x = -10
# -1

x = 1534236469
# 0


# lst=[]
# flag = False
# for i in str(x):
#     if i == "-":
#         flag = True
#         continue
#     lst.append(int(i))
#
# lst = lst[::-1]
# lst = str(lst).translate(str.maketrans({'[': '', ']': '', ',':'', ' ':''}))
# if flag == False:
#     return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
# elif lst[0] == "0" and flag == True:
#     while lst[0] == "0":
#         lst = lst[1:]
#     lst = "-" + lst
#     return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
# elif lst[0] == "0":
#     while lst[0] == "0":
#         lst = lst[1:]
#     return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
# else:
#     lst = "-" + lst
#     return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)


# amelioration


## submit

if 2 ** 31 <= x or x <= -2 ** 31 - 1: return 0
if x >= 0:
    ans = int(str(x)[::-1])
    return 0 if 2 ** 31 <= ans or ans <= -2 ** 31 - 1 else ans
else:
    ans = int("-" + str(x)[1:][::-1])
    return 0 if 2 ** 31 <= ans or ans <= -2 ** 31 - 1 else ans

## local test

if 2 ** 31 <= x or x <= -2 ** 31 - 1: print(0)
if x >= 0:
    ans = int(str(x)[::-1])
    print(0) if 2 ** 31 <= ans or ans <= -2 ** 31 - 1 else print(ans)
else:
    ans = int("-" + str(x)[1:][::-1])
    print(0) if 2 ** 31 <= ans or ans <= -2 ** 31 - 1 else print(ans)
