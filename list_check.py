def fun(a,n,key):
    l=0
    h=n-1
    f=0
    while(l<=h):
        mid=(l+h)//2
        if(a[mid]==key):
            f=1
            break
        elif(a[mid]>key):
            h=mid-1
        else:
            l=mid+1
    if(f!=1):
        return -1
    return mid+1
   


l1=[]
n=int(input("enter the no of elements  :"))
for i in range(n):
   a=int(input("enter  :"))
   l1.append(a)
l1.sort()
key=int(input("enter the no to search :"))
pos=fun(l1,n,key)
if(pos!=-1):
    print("number ",key,"position is  :",pos)
else :
    print("not found")
    

