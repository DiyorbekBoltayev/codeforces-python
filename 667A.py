n = list(map(int, input().split()))
h = n[1]
n = n[0]
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i > h:
        ans += 2
    else:
        ans += 1

print(ans)
