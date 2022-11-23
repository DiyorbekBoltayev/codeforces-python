n=int(input())
s=list(map(int,input().split()))
b=s.copy()
for i in range(n):
    b[s[i]-1]=i+1

print(*b)

