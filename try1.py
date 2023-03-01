import pdb

pdb.set_trace()
a=int(input("Enter 1:"))
b=input("Enter 2:")

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Cannot Be Divided By Zero")
else:
    print("Division Done")
finally:
    print("Thanks For Using Code")
