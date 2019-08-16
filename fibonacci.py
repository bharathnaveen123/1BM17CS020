a=0
b=1
count=0
li=[]
li.append(a)
li.append(b)
n=int(input("enter the no of elements:  "))
while(count<n-2):
    sum=a+b
    li.append(sum)
    a=b
    b=sum
    count=count+1

print(li)
