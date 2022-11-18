n = int(input())
bir, ikki, uch = 0, 0, 0
for i in range(n):
    s=input()
    s=list(map(int,s.split()))
    bir+=s[0]
    ikki+=s[1]
    uch+=s[2]

if bir==ikki==uch==0:
    print('YES')
else:print('NO')
