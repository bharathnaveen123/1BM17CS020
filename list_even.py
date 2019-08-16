l1=[]
l2=[]
a=int(input("enter the no of elements:"))
for i in range(a):
    n=int(input("enter :"))
    l1.append(n)
for i in  l1:
    if(i%2==0):
        l2.append(i)

print("even elements are  :")
print(l2)
        
