def binary_search(l1,n):
    f=0                                 #Index Value Of First Element
    l=len(l1)-1                         #Index Value Of Last Element


    while f<=l:
        m=(f+l)//2                      #Index Value Of Middle Element
        if l1[m]<n:
            f=m+1
        elif l1[m]>n:
            l=m-1
        else:
            return m
    return -1        


l1=[10,22,45,52,69,83]                       #Sorted List
n=int(input("Enter Number To Search:"))
m=binary_search(l1,n)              #Function Call
if m!=-1:
    print("Number Found In",m+1,"Position")
else:
    print("Number Not Found")    