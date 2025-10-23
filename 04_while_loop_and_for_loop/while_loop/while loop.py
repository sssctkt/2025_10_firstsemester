"""
1.difference between while loop and for loop
2.keyword break 
3. we can design a little game
"""

#break--immediately exit the loop it is in (one level) 
#for loop--use it when you know how many times it will loop 
#while loop --use it if you are lookng for a specific case to get out
print("let's play an interesting game!!!")
while(True):
    answer=input("Do you want to do homework?? yes or no: ")
    if (answer=="yes"):
        break 

print("Then do your homework")
