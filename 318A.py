s=list(map(int,input().split()))
n=s[0]
k=s[1]
toq=0
juft=0
if n%2==0:
    toq=n//2
    juft=toq
else:
    toq=n//2+1
    juft=toq-1
if k>toq:
    k-=toq
    print(k*2)
else:
    print(2*k-1)


