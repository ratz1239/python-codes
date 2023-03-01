binary = input('Enter a Binary number: ')
decimal = 0

l = len(binary)

for x in binary:
  l = l-1
  decimal += pow(2,1) * int(x)

print("Decimal of {p} is {q} ".format(p=binary, q=decimal))

