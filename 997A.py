s=input()
s=list(map(int,s.split()))
n=s[0]
k=s[1]
qadam=0
while k>qadam:
    if str(n)[-1]=='0':
        n=n//10
    else:
        n-=1
    qadam+=1

print(n)