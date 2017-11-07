v_password=str(input("What is the password?:"))
v_count=1
while v_password !="password123":
    print("Incorrect Password")
    print("You have entered:", v_count,"times")
    v_count+=1
    if v_count > 4:
        print("Sorry you have entered",v_count, "times, you're kicked")
        break
    else:
        v_password=str(input("Please Input Password Again"))
else:
    print("Access Granted")

