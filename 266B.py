s = list(map(int, input().split()))
n = s[0]
t = s[1]
s = list(input())
for i in range(t):
    j = 1
    while j < n:
        if s[j] == 'G' and s[j - 1] == 'B':
            s[j], s[j - 1] = s[j - 1], s[j]
            j+=1
        j+=1


print("".join(s))
