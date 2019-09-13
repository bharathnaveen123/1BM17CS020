f=open("file4.txt","w")
f1=open("file1.txt","r")
f2=open("file2.txt","r")
con1=f1.readline()
con2=f2.readline()
x=con1.split(" ")
y=con2.split(" ")

if(len(x)>len(y)):
    length=len(x)
else:
    length=len(y)
    
x[0]=x[0]+" "
y[0]=y[0]+" "

str=" "
for i in range(length):
    if(i>len(x)-1):
        n1=0
    else:
        n1=len(x[i])//2
        str1=x[i]
    if(i>len(y)-1):
        n2=0
    else:
        n2=len(y[i])//2
        str2=y[i]
    for i in range(n1):
        str=str+str1[i]
    for i in range(n2):
        str=str+str2[i]
    str+=" "
f1.close()
f2.close()
f.write(str)
f.close()
with open("file4.txt","r") as f4:
    cont=f4.readline()
    print(cont)
f4.close()

    

