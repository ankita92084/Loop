n=int(input("enter number"))
orig=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if orig==sum:
    print("artmstrong number")
else:
    print("not armstrong")