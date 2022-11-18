s=input()
if s=='7' or s=='4':
    print('NO')
    exit()

for i in s:
    if i!='7' and i!='4':
        print('NO')
        exit()

print('YES')