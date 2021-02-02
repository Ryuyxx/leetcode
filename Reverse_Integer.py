# x = 123
# 321

# x = -123
# -321

# x = 2200
# 21

# x = 0
# 0

# x = -10
# -1

x = 1563847412
# 0

if x == 0: return 0

lst=[]
flag = False
for i in str(x):
    if i == "-":
        flag = True
        continue
    lst.append(int(i))

lst = lst[::-1]
lst = str(lst).translate(str.maketrans({'[': '', ']': '', ',':'', ' ':''}))
if flag == False:
    # if -2147483648 <= abs(int(lst)) >= (1<<31)-1 : lst = 0
    # return int(lst)
    return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
elif lst[0] == "0" and flag == True:
    while lst[0] == "0":
        lst = lst[1:]
    lst = "-" + lst
    return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
elif lst[0] == "0":
    while lst[0] == "0":
        lst = lst[1:]
    return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
else:
    lst = "-" + lst
    return 0 if -2147483648 <= abs(int(lst)) >= (1<<31)-1 else int(lst)
