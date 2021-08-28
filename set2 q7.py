user=int(input("enter number"))
reverse=0
while user>0:
    reminder=user%10
    reverse=reverse*10+reminder
    user=user//10
print(reverse)
reverwse=reverse-1

