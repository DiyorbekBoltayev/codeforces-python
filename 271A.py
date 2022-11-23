n = input()
a = int(n)
s = list(n.split())


def is_unique(s):
    return len(s) == len(set(s))


while True:
    a += 1
    if is_unique(str(a)):
        print(a)
        break
