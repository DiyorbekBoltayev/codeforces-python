n=int(input())
ans=0
for i in range(n):
    s=input()
    s=s.split()
    if (int(s[0])+int(s[1])+int(s[2]))>1:
        ans+=1

print(ans)