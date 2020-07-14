from queue import LifoQueue

stark = []
list = []
s = '{ } ]  {'
list.append(s)
for i in s:
    if i not in ' ':
        stark.append(i)
print(stark)
s = stark[0]+stark[-1]
print(s)
