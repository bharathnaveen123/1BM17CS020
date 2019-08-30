def fun(str):
   str1=str.split(" ")
   str1.reverse()
   return str1
    
def fun1(str):
    str1=str[::-1]
    return str1 


str=input("enter string       :")
print("original string   :",str)
test=fun(str)
print("words in a reversr order :  ",test)
print("\ncharacters in the reverse order  :  ",fun1(str))

