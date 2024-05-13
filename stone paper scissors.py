import random

userwon=0
computerwon=0
ties=0

options=['stone', 'paper', 'scissors']

while True:
    userinput= input("Choose Between 'Stone', 'Paper' , Scissors or Q to Quit " ).lower()
    if userinput=='q':
        break
    if userinput not in options:
        print("Invalid")
        continue
    randomnum= random.randint(0,2)
    comp= options[randomnum]
    if userinput=='stone' and comp=='scissors':
        userwon+=1
        print("You won")
    elif userinput=='paper' and comp=='stone':
        userwon+=1
        print("You won")
    elif userinput=='scissors' and comp=='paper':
        userwon+=1
        print("You won")
    elif userinput==comp:
        ties+=1
        print("oops! same!")
    else:
        computerwon+=1
        print("I won Bro")


if computerwon>userwon:
    print("You know who's the real boss You won:", userwon, "& I won", computerwon)

if computerwon<userwon:
    print("You're the real boss You won:", userwon, "& I won:", computerwon)

if computerwon==userwon:
    print("we matched",ties, "times")