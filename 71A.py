n=int(input())
ans=[]
for i in range(n):
    s=input()
    if len(s)<=10:
        ans.append(s)
    else:
        ans.append("{}{}{}".format(s[0],len(s)-2,s[-1]))
for i in ans:
    print(i)