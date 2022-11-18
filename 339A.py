s = input()
s = list(map(str, s.split('+')))
s.sort()
m = ''
for i in s:
    m += "+{}".format(i)
print(m[1:])
