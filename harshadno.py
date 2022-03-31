sum=0
n=int(input("enter a number :- "))
num=n
while num>0:
    rem=num%10
    sum+=rem
    num=num//10
if n%sum==0:
    print(n," is a HARSHAD number ")
else:
    print(n,"is not a harshad number ")


