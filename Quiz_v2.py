#variables
score=0
game=0

#list for q4 because it has two possibilities
q4list=["napoleon","napoleon bonaparte"]
#question functions
def q1():
    global score
    q1=str(input("Q1. What country has cities that includes Jerusalem and Tel Aviv?")).lower()
    if q1=="Israel".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Israel")

def q2():
    global score
    q2=str(input("Q2. What object whose gravity is so strong that light cannot escape from it?")).lower()
    if q2=="Black Hole".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Black Hole")

def q3():
    global score
    q3=str(input("Q3. Who was the Roman dictator that was assassinated on the Ides of March?")).lower()
    if q3=="Julius Caesar".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Julius Caesar")

def q4():
    global score
    q4=str(input("Q4. Who was the first French Emperor?")).lower()
    if q4.lower() in q4list:
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Napoleon Bonaparte")

def q5():
    global score
    q5=str(input("Q5. What is the worlds largest island?")).lower()
    if q5=="Greenland".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Greenland")

def q6():
    global score
    q6=str(input("Q6. What country's capital is Baku?")).lower()
    if q6=="Azerbaijan".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Azerbaijan")

def q7():
    global score
    q7=str(input("Q7. Toussaint L'Ouverture led a slave revolt in what Caribbean country?")).lower()
    if q7=="Haiti".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Haiti")

def q8():
    global score
    q8=str(input("Q8. What language is thought to have been spoken by Jesus?")).lower()
    if q8=="Aramaic".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Aramaic")

def q9():
    global score
    q9=str(input("Q9. What was the first Nazi Concentration Camp?")).lower()
    if q9=="Dachau".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Dachau")

def q10():
    global score
    q10=str(input("Q10. What German city is the capital of the state of Bavaria?")).lower()
    if q10=="Munich".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Munich")

def q11():
    global score
    q11=str(input("Q11. Which Syrian city was the most populous before the civil war?")).lower()
    if q11=="Aleppo".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Aleppo")

def q12():
    global score
    q12=str(input("Q12. What is the capital of Denmark?")).lower()
    if q12=="Copenhagen".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Copenhagen")

def q13():
    global score
    q13=str(input("Q13. Which Chinese dynasty did Li Yuan establish? (exclude 'dynasty' in your answer)")).lower()
    if q13=="Tang".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Tang")

def q14():
    global score
    q14=str(input("Q14. Which South American country's capital is Quito?")).lower()
    if q14=="Ecuador".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Ecuador")

def q15():
    global score
    q15=str(input("Q15. Who was Plato's most famous student?")).lower()
    if q15=="Aristotle".lower():
        score+=1
        print("Correct")
    else:
        print("Incorrect, the answer was Aristotle")




#Intro+Yes or No Option
print("Welcome to the General Knowledge Quiz")
name=str(input("What is your name? :"))
qplay=str(input("Do you want to play? (yes/no)")).lower()
if qplay==("no").lower():
    print("Bye, Have a great time!")
    quit()
elif qplay==("yes").lower():
    print("Ok")
    print("Let's start",name)
else:
    print("It was an easy question, just a yes or no, come on man")
    quit()


#Running the Question functions
while game==0:
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
    break

print("""
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗██╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗██║
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║╚═╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝

""")
print("Good Job",name,"you got a score of",score,"/15",round((score/15)*100,2),"% !")

