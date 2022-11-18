s = input()
s = list(map(int, s.split()))
n = s[0]
m = s[1]
a = s[2]
ans = 0
boyi = n // a;
if n % a != 0:
    boyi += 1
eni = m // a;
if m % a != 0:
    eni += 1
print(eni * boyi)
