#data should be expressed as arrays?
from algorithm import Test

class Student:
    
    stud_list = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stud_list.append(self)
        
class Subjects:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        
class Schedule:
    def __init__(self):
        self.result = []
        
    def schedule(self):
#        for x in Student:
#            print (Student.name)
        
        self.result.append("hi")
        return self.result
    
        
stud1 = Student('jake',19)
stud2 = Student('mark',21)



result1 = Schedule()






result1.schedule()

x = Test(stud1.name)

print (stud1.name)
print (stud1.age)
print (result1.result)
print (x.text)
print (Student.stud_list)


#if 