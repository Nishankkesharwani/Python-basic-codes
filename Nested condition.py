a=int(input("enter value a:"))
b=int(input("enter value b:"))
c=int(input("enter value c:"))
if(a>b and a>c):
    print(a, "is greater")
else:
    if(b>c):
        print(b, " is greater")
    else:
        print(c,"is greater")    