class Student_Details:
    Class=10

    def __init__(self):
        self.score=100
        self.age=23
        self.section='a'

    def Display(self):
        print(self.score,self.age,self.section)


sam=Student_Details()
#sam.Student_Details(100,23,'a')
#sam.age=23
#sam.score=100
#sam.section='a'
sam.Display()
