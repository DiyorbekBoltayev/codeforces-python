def shundinmi(n):
        a = []
        a.append(0)
        a.append(1)
        for i in range(2, n):
            a.append(i + a[i - 1])

        no = True
        for i in range(1, n - 1):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (a[i] + a[j] + a[k]) == n:
                       return 1
        if no:
            return 0
son=int(input())
s=""
for i in range(son):
    s+=str(shundinmi(int(input())))
print(s)