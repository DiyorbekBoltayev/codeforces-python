soz=input()
katta=0
kichik=0
for i in soz:
    if i>='A' and i<='Z':
        katta+=1
    else:kichik+=1

if katta>kichik:
    print(soz.upper())
else: print(soz.lower())