s=input()
s=list(map(int,s.split()))
a=s[0]
b=s[1]
yil=0;
while b>=a:
    a*=3
    b*=2
    yil+=1

print(yil)