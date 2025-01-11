a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
f=((a+b+c)/300)*100
if(100>=f>=90):
    print('garde is A and perce. is',f)
if(90>=f>=75):
    print('grade is B and perce. is',f)
if(75>=f>=60):
    print('grade is C and perce. is',f)
if(60>=f>=40):
    print('grade is D and perce. is',f)
if(f<=40):
    print('fail',f)


