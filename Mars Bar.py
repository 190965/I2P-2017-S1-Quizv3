#Mars Bar
def fq():
    a=str(input("Would you like a mars bar? (Y/N):"))
    if a==str.upper("y"):
        print("Here is a mars bar")
    elif a==str.lower("y"):
        print("Here is a mars bar")
    elif a==str.upper("n"):
        print("I guess you don't want a mars bar")
    elif a==str.lower("n"):
        print("I guess you don't want a mars bar")
    else:
        print("I don't recognize your answer")
        fq()

fq()

#Prime Number Checker
def fpn():
    n=int(input("Put in a number to check if it's prime:"))
    for i in range(2,n):
        if n % i != 0:
            print("The number is prime")
            break
        else:
            print("The number isn't prime")
            break
fpn()








