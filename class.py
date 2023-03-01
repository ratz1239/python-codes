#template


class Student_Details:
    Class=10
    #constructor
    def __init__(self,score,age,section):
        self.ascore=score
        self.aage=age
        self.asection=section
        
    def Display(self):
        print("Age is {} with {} and {}".format(self.aage,self.asection,self.a  score))

#instances
ritvik=Student_Details(100,23,'a')
angad=Student_Details(200,24,'b')
#instance variables

'''
ritvik.age=24
ritvik.score=100
ritvik.section='a'
b=ritvik.Class
print(b)

angad.age=23
angad.score=120
angad.section='c'
angad.Class=10


print(ritvik.Class)
angad.Class=12
print(angad.Class)
#ritvik.Class=12
print(ritvik.Class)

Student_Details.Class=13
print(abc.Class)
print(ritvik.Class)

ritvik.Display()
angad.Display()
'''
#a=angad.__dict__
#print(Student_Details.__dict__)
angad.Display()
