list1 = ['1', '2', '', '3', '4', '']
while True:
    list1.remove('')
    if "" not in list1:
        break
print(list1)


import sys
for arg in sys.argv:
    print(arg)