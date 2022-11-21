n = int(input())
a = list(map(int, input().split()))


def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


ans = find_lcm(a[0], a[1])
for i in range(1, n):
    ans = find_lcm(ans, a[i])

ans -= 1


def f(m):
    qoldiq = 0
    for i in a:
        qoldiq += m % i

    return qoldiq


print(int(f(ans)))
