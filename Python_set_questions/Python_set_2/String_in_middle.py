s1 = "Ault"
s2 = "Kelly"

newStr = ""

for i in range(0,len(s1)):
    if len(s1)%2==0 and i==len(s1)/2:
        newStr+=s2
        newStr+=s1[i]
    elif len(s1)%2!=0 and i==len(s1)/2+1:
        newStr+=s2
    else:
        newStr+=s1[i]

print(newStr)
