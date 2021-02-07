# s = "()"
# true
# s = "()[]{}"
# true
# s = "(]"
# False
# s = "([)]"
# False
# s = "{[]}"
# True
s = "["
# False
s = "(("
# False
s = "){"
# False

if len(s) < 2: print("error")
d = {'(':')', '{':'}', '[':']'}

tmp = []
for i in s:
    if i in d.keys():
        tmp.append(d[i])
    elif len(tmp) == 0: print("error")
    else:
        if i == tmp[::-1][0]:
            tmp.pop(-1)
        else:
            print("error")
if len(tmp) != 0: print("error")
