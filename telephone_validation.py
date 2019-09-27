class call_details():
    def __init__(self,called_no,called_to,dur,type1):
        self.from1=called_no
        self.to=called_to
        self.d=dur
        self.typ=type1
class util():
    def __init__(self):
        self.list_of_call_objects=None

    def parsecust(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            called_no,called_to,dur,type1=map(str,i.split(","))
            self.list_of_call_objects.append(call_details( called_no,called_to,dur,type1))
call1='9900108766,9740133256,25,std'
call2='9900108966,9740033256,35,local'
call3='9910108766,9740183256,20,isd'
list_of_call_string=[call1,call2,call3]
print(list_of_call_string)
util().parsecust(list_of_call_string)                                             
                                       
