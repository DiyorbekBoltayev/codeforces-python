s=input()
ind=0
a='hello'
for i in a:
    if i in s:
        k=s.find(i)
        s=s[k+1:]
    else:
        print('NO')
        exit()

print('YES')