#while
# while <condition>(bool):
# while True

#for

'''
for index in <range>

1.list
l = [1,2,3,4,5]
for i in l:
    print(i)

2.string
s = 'hello'
for i in s:
    print(i)

3.range(start(init:0), end, interval(init:1))
from start -> end-1, +interval for each time

for i in range(1, 10, 2):
    print(i)
for i in range(4):
    print(i)
for i in range(1, 10):
    print(i)
for i in range(10,0,-1):
    print(i)
'''

#continue(skip) break(stop)

for i in range(10):
    if i % 3 == 0:
        continue
    if i == 7:
        break
    print(i)