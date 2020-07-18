list1 = ["flower","flow","flight"]
res = ""
for temp in zip(*list1):
    temp_set = set(temp)
    if len(temp_set) == 1:
        res += temp[0]
print(res)