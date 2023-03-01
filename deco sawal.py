class A:
    a=4

    def disp():
        print(a)
    @classmethod
    def change_a(cls,f):
        cls.a=f

abc=A()
abc.a=10

abc.change_a(3)
#A.disp()
