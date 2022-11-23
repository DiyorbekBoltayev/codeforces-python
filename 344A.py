n=int(input())

a=[]
for i in range(n):
    a.append((input()))
if n==1:
    print(1)
    exit()
ans=1
for i in range(1,n):
    if a[i][0]==a[i-1][1]:
        ans+=1

print(ans)