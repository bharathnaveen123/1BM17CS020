class check():
    def __init__(self):
        pass

    def valid(self,st):
        l=list(st)
        for i in range(len(l)):
            if(l[i]=='(' and l[i+1]!=')'):
                return -1
            elif(l[i]=='{' and l[i+1]!='}'):
                return -1
            elif(l[i]=='[' and l[i+1]!=']'):
                return -1

            i=i+1
            
        return 1
            
               
s=input("enter  :")
c=check()
x=c.valid(s)
if(x==1):
    print("valid")
else:
    print("invalid")
