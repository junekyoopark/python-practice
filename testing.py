#data should be expressed as arrays?
from algorithm import Test

class Student:
    def __init__(self, name):
        self.name = name
        
class Subjects:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        
class Schedule:
    def __init__(self):
        self.result = []
        
    def schedule(self):
        self.result.append("hi")
        return self.result
        
stud1 = Student('jake')
result1 = Schedule()



result1.schedule()

x = Test(stud1.name)

print (stud1.name)
print (result1.result)
print (x.text)