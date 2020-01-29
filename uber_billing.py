sp=int(input("enter starting point"))
ep=int(input("enter end point"))
diff=ep-sp
print(diff)
print("choose your ride")
print("0.AUTO \n1.HATCHBACK \n2.SUV")
while(1):
    ride=int(input("select"))
    if(ride==0):
        print("amt" ,diff*8)
        break
    elif(ride==1):
        print("amt", diff*12)
        break
    elif(ride==2):
        print("amt",diff*20)
        break
    else:
        print("invalid ride option")
    
print("your ride is on the way")
