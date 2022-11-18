s=str(input())
s=list(map(str,s))
ans=[]
for i in s:
    if i not in ans:
        ans.append(i)

if(len(ans)%2==0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')