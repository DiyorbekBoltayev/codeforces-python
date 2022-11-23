n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a=a[1:]+b[1:]
a=set(a)
if len(a) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
