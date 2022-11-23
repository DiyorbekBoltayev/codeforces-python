n=int(input())
ans=0
for i in range(n):
    s=list(map(int,input().split()))
    if s[1]-s[0]>1:
        ans+=1

print(ans)
