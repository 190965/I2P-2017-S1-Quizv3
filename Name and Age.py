name=(input("What is your name:"))
print(name)
age=(int(input("How old are you?:")))
print(age)
print("Hi", name, "you are", age, "years old")
days=age*365
hours=days*24
minutes=hours*60
seconds=minutes*60
print(name,"You have been alive for",days,"days,",hours,"hours,",minutes,"minutes,",seconds,"seconds")
