n = int(input())
ans = 0
current = 0
for i in range(n):
    s = list(map(int, input().split()))
    current -= s[0]
    current += s[1]
    if current > ans:
        ans = current

print(ans)
