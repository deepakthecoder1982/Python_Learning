str1 = "PyNaTive"
LowerCase = ''
UpperCase = ''
for i in str1:
    if i.islower():
        LowerCase+=i
    else:
        UpperCase+=i

print("Final Solution :-",LowerCase+UpperCase)
