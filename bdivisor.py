def fun(a):
    l1=[]
    for i in range(1,a//2+1):
        if i!=0:
            if a%i==0:
                l1.append(i)

    return l1



a=int(input("enter the no   :"))
l=[]
l=fun(a)
l.append(a)
print("divisors of the no  ",a,"  are  :",l)
