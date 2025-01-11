n=int(input("n: "))
i=2
a=1
while(i<=n//2):
    if(n%i==0):
        a=0
        break
    i=i+1
if(a==1):
    print(n,"is prime")
else:
    print(n,"is not a prime number")