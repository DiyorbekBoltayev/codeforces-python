s=input()
s=s.lower()
unli=['a','o','u','e','i','y']
for i in range(len(s)):
    if s[i] in unli:
        continue
    else:
        print(".{}".format(s[i]),end='')
