d={}
choice=0
while True:
    print("1.Create","2.Update","3.Delete","4.Display","5.Exit",sep='\n')
    choice=int(input("Choose:"))
    if choice==1:
        i=input("Enter Name:")
        d[i]=list(input("Enter DOB:").split("/"))
    elif choice==2:
        i=input("Enter Name:")
        if i in d:
            d[i]=list(input("Enter DOB:").split("/"))
            print("Updated")
        else:
            print("Name Not Found")
    elif choice==3:
        i=input("Enter Name:")
        if i in d:
            d.pop(i)
            print("Deleted")
        else:
            print("Name Not Found")
    elif choice==4:
        print(d)
    else:
        break
    
