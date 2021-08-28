n=int(input("enter alphabet"))
i=1
while i<=n:
    j=1
    a=97
    while j<=n:
        print(chr(a),end=" ")
        j=j+1
        a=a+1
    print()
    i+=1
