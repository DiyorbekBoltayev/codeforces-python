n = int(input())
s = ''
t1 = 'I hate'
t2 = 'I love'
for i in range(n):
    if i % 2 == 0:
        s += t1
    else:
        s += t2
    if i != n - 1:
        s += ' that '
    else:
        s += ' it'

print(s)