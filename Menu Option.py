def menu():
    choice=0
    while choice!="1"and"2"and"3"and"4":
        choice=input("""Choose from the following options for your meal: (1-3)
        1. Chicken Burger
        2. Beef Burger
        3. Lamb Burger
        """)
        if choice=="1":
            option1()
            break
        elif choice=="2":
            option2()
            break
        elif choice=="3":
            option3()
            break
        else:
            print("Exiting the Restaurant")
            break

def option1():
    print("You have chosen the Chicken Burger")
def option2():
    print("You have chosen the Beef Burger")
def option3():
    print("You have chosen the Lamb Burger")

menu()
