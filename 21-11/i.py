bset = set()
s = int(input())
s = list(map(int, input().split()))

for i in s:
    bset.add(i)

print(len(bset))
