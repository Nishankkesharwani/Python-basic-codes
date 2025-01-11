n=int(input("n: "))
i=2
a=0
while(i<=n//2):
    if(n%i==0):
        a=1
    i=i+1
if(a==0):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")