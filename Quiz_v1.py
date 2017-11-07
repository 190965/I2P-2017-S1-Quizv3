#variables
score=0
#question functions
def q1():
    global score
    q1=str(input("Q1. What country has cities that includes Jerusalem and Tel Aviv?"))
    if q1=="Israel".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Israel")

def q2():
    global score
    q2=str(input("Q2. What object whose gravity is so strong that light cannot escape from it?"))
    if q2=="Black Hole".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Black Hole")

def q3():
    global score
    q3=str(input("Who was the Roman dictator that was assassinated on the Ides of March?"))
    if q3=="Julius Caesar".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Julius Caesar")

def q4():
    global score
    q4=str(input("Who was the first French Emperor?"))
    if q4=="Napoleon".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Napoleon Bonaparte")

def q5():
    global score
    q5=str(input("What is the worlds largest island?"))
    if q5=="Greenland".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Greenland")

def q6():
    global score
    q6=str(input("What country's capital is Baku?"))
    if q6=="Azerbaijan".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Azerbaijan")

def q7():
    global score
    q7=str(input("Toussaint L'Ouverture led a slave revolt in what Caribbean country?"))
    if q7=="Haiti".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Haiti")

def q8():
    global score
    q8=str(input("What language is thought to have been spoken by Jesus?"))
    if q8=="Aramaic".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Aramaic")

def q9():
    global score
    q9=str(input("What was the first Nazi Concentration Camp?"))
    if q9=="Dachau".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Dachau")

def q10():
    global score
    q10=str(input("What German city is the capital of the state of Bavaria?"))
    if q10=="Munich".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Munich")

def q11():
    global score
    q11=str(input("Which Syrian city was the most populous before the civil war?"))
    if q11=="Aleppo".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Aleppo")

def q12():
    global score
    q12=str(input("What is the capital of Denmark?"))
    if q12=="Copenhagen".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Copenhagen")

def q13():
    global score
    q13=str(input("Which Chinese dynasty did Li Yuan establish? (exclude 'dynasty' in your answer)"))
    if q13=="Tang".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Tang")

def q14():
    global score
    q14=str(input("Which South American country's capital is Quito?"))
    if q14=="Ecuador".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Ecuador")

def q15():
    global score
    q15=str(input("Who was Plato's most famous student?"))
    if q15=="Aristotle".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Aristotle")




#Intro
print("Welcome to the General Knowledge Quiz")
name=str(input("What is your name? :"))
print("Let's start",name,)


#Running the Question functions
q1()
q2()
q3()
q4()
q5()
q6()
q7()
q8()
q9()
q10()
q11()
q12()
q13()
q14()
q15()
print("""
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗██╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗██║
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║╚═╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝

""")
print("Good Job",name,"you got a score of",score,"/15",round((score/15)*100,2),"% !")

