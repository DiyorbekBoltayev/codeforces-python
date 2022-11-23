n = int(input())
a = list(map(int, input().split()))


uzun=1
eng_uzun=1
for i in range(1,n):
    if a[i-1]<=a[i]:
        uzun+=1
        if uzun>eng_uzun:
            eng_uzun=uzun
    else:
        uzun=1

print(eng_uzun)