s=input("Enter String:")
countu=0
countl=0
countd=0
counts=0
l=len(s)
for i in range(0,l):
    if s[i].isupper() is True:
        countu+=1
    if s[i].islower() is True:
        countl+=1
    if s[i].isnumeric() is True:
        countd+=1
    if s[i].isspace() is True:
        counts+=1
print("Upper Case:",countu)
print("Lower Case:",countl)
print("Digits:",countd)
print("White Spaces:",counts)
