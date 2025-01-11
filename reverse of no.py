n=int(input("n: "))
rn=s=n1=0
while(n>0):
    rn=rn*10+n%10
    n1=n1+1
    s=s+n%10
    n=n//10
print('reverse no: ',rn)
print('nod: ',n1)
print('sod: ',s)
