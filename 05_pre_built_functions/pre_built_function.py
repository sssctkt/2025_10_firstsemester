#pre-built function
#simple string and list methods
#user defined function

#pre-built function
#what is a function in python? a block that does a specific task for you
#it helps to reuse the code

#example
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the fourth number: "))
"""
instead of doing it by yourself
if (a>b and a>c):
    print(a)
elif (b>a and b>c):
    print(b)
else:
    print(c)

you can use pre-built functions made by others
as long as you know them
"""
#1. max() 2. min()
#task, find the maximum of a and b, then find the minimum of c and d
#then find the maximum of these 2 results
#all in one line
answer=max(max(a,b), min(c,d))
print(answer)
