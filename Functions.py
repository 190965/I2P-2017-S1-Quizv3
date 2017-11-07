#Challenge 1
def fsum():
    int1=int(input("Give me a number:"))
    int2=int(input("Give me a number:"))
    vtotal=int1+int2
    return vtotal
print(fsum())

def f_sum(int1,int2):
    return int1 + int2

vTotal= f_sum(21,423)
print("The total is:",vTotal)

#Challenge 2
def f_print_largest(int1,int2):
    if int1>int2:
        print(int1,"is larger")
    elif int2>int1:
        print(int2,"is larger")

callable(f_print_largest(23,34))

#Challenge 3
def F_largest(x,y,z):
    if x>y and x>z:
        print(x,"is the largest")
    elif y>x and y>z:
        print(y,"is the largest")
    elif z>x and z>y:
        print(z,"is the largest")

callable(F_largest(8,233,232))



