# num=int(input("enter the number"))
# i=1
# while i<=10:
#     print(num,"X",i,"=",i*num)
#     i=i+1


a=int(input("enter"))
i=1
count=0
while a<i:
    if a%i==0:
        count+=1
    i+=1
if (count==2):
    print("prime")
else:
    print("not a prime")
    


