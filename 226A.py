n = int(input())
s = input()
ans = 'z'
for i in s:
    if ans[-1] != i:
        ans += i
print(len(s)-len(ans)+1)
