num = 13;

count=0
for i in range(2,num+1):
    if num%i==0:
        count+=1
    
if count==1:
    print(num,"is a prime Number")
else:
    print(num,"is not a prime Number")
    