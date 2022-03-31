# n=int(input("enter number"))
# orig=n
# sum=0
# while n>0:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if orig==sum:
#     print("armstrong number")
# else:
#     print("not armstrong")




# n=int(input("enter number "))
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if n==sum:
#     print("armstrong ")
# else:
#     print("not armstrong")


for i in range(1,1001):
    num=i
    n=len(str(i))
    sum1=0
    i=str(i)
    for digit in i:
        sum1=sum1+int(digit)**n
        if sum1==num:
            print(num)
            