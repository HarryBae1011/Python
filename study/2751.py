import sys

n = int(input())
list = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    list.append(tmp)

list.sort()

for i in range(n):
    print(list[i])
