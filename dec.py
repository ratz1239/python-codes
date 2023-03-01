

def nozero(func,a,b):
    func()
    def check(a,b):
        if b==0:
            print("invalid input")
        else:
            return a/b
    return check

@nozero
def div(a,b):
    return a/b

div=nozero
a=int(input("enter"))
b=int(input("enter"))


print(div(a,b))