class admission:
    def __init__(self,i):
       self.id=0
       self.age=0
       self.marks=0

    def get_val(self):
        self.id=int(input("ID:"))
        self.age=int(input("age:"))
        self.marks=int(input("marks:"))
        l1=[]
        l1.append(self.age)
        l1.append(self.marks)
        return l1

    def validate_marks(self,x):
        if(x>=0 and x<101):
           return True
        else:
            return False

    def validate_age(self,x):
        if(x>20):
           return True
        else:
            return False
    def check_qualification(self,age,mark,x):
        if(age==True and mark==True):
            if(x>=65):
                return True
            else:
                return False
        else:
            return False
    def pri(self):
        print("ID  :",self.id)
        print("Age  :",self.age)
        print("Marks  :",self.marks)
        
    

        
a=[]
for i in range(2):
    a.append(admission(i))

for i in range(2):
    print("enter student details:")
    l=a[i].get_val()
    age=a[i].validate_age(l[0])
    mark=a[i].validate_marks(l[1])
    c=a[i].check_qualification(age,mark,l[1])
    if(c==True):
        print("Admission accepted")
    else:
        print("Admission denied")

    
for i in range(2):
    a[i].pri()
