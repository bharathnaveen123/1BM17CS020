import string
import random 
special=string.punctuation
num=string.digits
let = string.ascii_letters

tot=""
tot=special+num+let
str1=""
n=int(input("enter the length   :"))
for i in range(n):
    x=random.choice(tot)
    str1=str1+x

print("password     :",str1)
