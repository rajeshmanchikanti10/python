""" class for list"""
class operation_withlist():
    def __init__(self,*args):
        self.numbers=[]
        for i in args:
            self.numbers.append(i)
    def show_list(self):
        print(self.numbers)

"""class for tuples """
class operation_withtuples:
    def __init__(self,*args):
        self.numbers=[]
        for i in args:
            self.numbers.append(i)
        self.numbers=tuple(self.numbers)

    def getvalue(self,i):
        return self.numbers[i]

"""class for dictionaries"""    
class operation_with_dictonary:
    def __init__(self,**kwargs):
        self.details={}
        for key,value in kwargs.items():
            self.details[key]=value
        
    def _showname(self):
        print(self.details['name'])
    def _showage(self):
        print(self.details['age'])
    def _deleteitem(self,key):
        self.details.pop(key)
        print(self.details)
            


"""list"""
l1=operation_withlist(1,2,3,4,5,6)
l1.show_list()



"""tuple"""
t1=operation_withtuples(1,2,3,4,5,6)
print(t1.getvalue(0))
print(t1.getvalue(3))


"""dictionary"""
d1=operation_with_dictonary(name='rajesh',age=20,hobbies="playing basketball,badminton,cricket,listening music")
d1._deleteitem('hobbies')
d1._deleteitem('age')
d1._deleteitem('name')
        
            
            
