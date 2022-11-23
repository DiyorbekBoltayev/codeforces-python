n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i/100

print("%.5f" %(s/n*100))