def f(n):
    for i in range(n//2+1):
        print("- "*n)
        if(i!=n//2):
            print("|   "*4)

n=int(input("enter no of rows:"))    
f(n)
