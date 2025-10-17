#loop (while loop and for loop)

#why do we learn loop??

#according to the structred program theorem
#given any solvable programming questions

#as long as you know these 3 things:
#1. next step (sequence)
#2. decision (if else statement) (selection)
#3. loop (iteration)

#goal of this program
#is to create a "FAIR" random number genenerator to select student
import random
number=1
while(number!=7):
    number=random.randint(1, 20)

print("this fair ranodm generator selects the number: ",number)
