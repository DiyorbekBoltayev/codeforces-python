s = input()
s = list(map(int, s.split()))
k = s[0] # 1 banan puli
n = s[1] # unda bo pul
m = s[2] # garak bann soni
qarz=0
olindi=0
while m>0:
        m-=1
        n-=(olindi+1)*k
        olindi+=1

if n<0:
    print(0-n)
else:
    print(0)
