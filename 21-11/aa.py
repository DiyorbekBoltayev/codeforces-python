n = int(input())
a = list(map(int, input().split()))
s = 0
for i in a:
    s += i - 1

print(s)
