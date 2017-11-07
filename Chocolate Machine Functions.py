def trans_summary():
    price=float(input("What is the price of the chocolate bar you want?:"))
    money=float(input("How much money are you going to pay with?:"))
    ChangeDue=(money-price)
    print("Change Due:",ChangeDue)
def change_summary():
    global ChangeDue
