list1 = [1,2,3]
a = [str(i) for i in list1]
print(a)
b = int(''.join(a))

b += 1
print(b)
list2 = []
for i in str(b):
    print(i)
    list2.append(i)
print(list2)