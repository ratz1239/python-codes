# Python program to illustrate functions
# can be treated as objects
'''
def shout(text):
	return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))
'''
#-----------------------------------------------------------------
'''
def A(t):
    return t+t

def B(t):
    return t*3

def new(f,l):
    var=f(t)+l(txt)
    print(var)
t="asdfg"
txt="hjbhj"
new(B,A)
#new(A)
'''
#-----------------------------------------------------------------
'''
# Python program to illustrate functions
# Functions can return another function

def A(x):
    def B(y):
    	return x+y

    return B
                #B return hoke Z ban gya 
Z=A(15) #x ki value yaha 15 mil jaati hai
            
print(Z(10)) #ye 10 value B wale func ko jaa rahi hai

'''
#-----------------------------------------------------------------
'''
# Python program to illustrate functions
# Functions can return another function

def A(x):               
    def C(z):
        def B(m):
            return m+" 3.9"     #yaha nested func bane hai,toh andar wale func ko call krne ke liye pehle bahar wala call krna hoga 
        return B    
    return C

txt="hello"
z="python"
m="1234"
Z=A(txt)    #yaha Z, A ka return wala func hai
Y=Z(z)      #yaha Y, C ka return wala func hai
q=Y(m)      #yaha q, B ka return hai
#z(" ")
#Y=A(txt)
print(Z(" world"))
print(Y(" python"))
'''

# defining a decorator
def hello_decorator(func):
    print("Chal")
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1


#@hello_decorator
#@inner1
def function_to_be_used():
	print("This is inside the function !!")



function_to_be_used = hello_decorator(function_to_be_used)
print(function_to_be_used())

