word="basketball"
count=0
print("Welcome to Guess the Word")
print("The word is",len(word),"letters long")
hintlist=["It is a ball sport","The sport involves a basket","LeBron James plays this sport","It is played on a court"]
i=0

while guess!=word:
    guess=str(input("Guess the word:"))
    if guess!=word:
        print(hintlist(i))
        i+1
        count+1
    else:
        print("The word was basketball","you took",count,"tries")











