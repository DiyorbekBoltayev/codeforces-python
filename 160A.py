n=int(input())
a=list(map(int,input().split()))
s=sum(a)
a.sort(reverse=True)
cnt=0
money=0
for i in a:
    if money<=(s-money):
        money+=i
        cnt+=1
    else:
        break

print(cnt)