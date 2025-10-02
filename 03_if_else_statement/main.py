#if else statement

#2 more forms of if else statement
#1. if elif else
#2. nested if statement

#nested if statement-if statements inside an if statements
number=int(input("Enter a positive integer: "))
color =input ("Enter your favorite color, red, yellow, blue, or pink: ")
if (number%2==0):
    print("You chose an even number!!")
    print("you must like barcelona!!")
    if (color=="red"):
        print("You chose the color red")
        print("You like english class?")
    elif (color=="yellow"):
        print("You chose the color yellow")
        print("You like music??")
    elif (color=="blue"):
        print("You chose the color blue")
        print("You like chess??")
    else:
        print("You chose the color pink")
        print("You like pineapple pizza")
else:
    print("you chose an odd number!!")
    print("You must like walking!")
    if (color=="red"):
        print("You chose the color red")
        print("You like english class?")
    elif (color=="yellow"):
        print("You chose the color yellow")
        print("You like music??")
    elif (color=="blue"):
        print("You chose the color blue")
        print("You like chess??")
    else:
        print("You chose the color pink")
        print("You like pineapple pizza")




          
