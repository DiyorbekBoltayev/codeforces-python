s1=input()
s2=input()
s3=''
for i in range(len(s1)):
    if s1[i]==s2[i]:
        s3+='0'
    else:
        s3+='1'
print(s3)