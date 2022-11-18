s = input()
s = list(map(int, s.split()))
n = s[0]
k = s[1]
s = input()
s = list(map(int, s.split()))
ans = 0
s.insert(0,0)
for i in range(len(s)):
    if(s[i]>=s[k] and s[i]>0):
        ans+=1
print(ans)