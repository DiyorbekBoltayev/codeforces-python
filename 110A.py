s = input()
soni = 0
for i in s:
    if i == '7' or i == '4':
        soni += 1
soni=str(soni)

for i in soni:
    if i!='7' and i!='4':
        print('NO')
        exit()

print('YES')
