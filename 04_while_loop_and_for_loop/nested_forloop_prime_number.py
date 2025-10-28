while(True):
    primenumber=True #reset
    number=int(input("Enter a number and I will you it is a prime number or not: "))
    if (number<0):
        break
    for a in range(2, number, 1):
        if (number%a==0):
            primenumber=False
            print("It is not a prime number")
            print("it is ",a, "x", number/a)
            break

    #if I run the whole for loop, and the primenumber is still True
    if (primenumber==True):
        print(number, "is a prime number")

    #task for today, try to modify the program such that the use
    #can keep entering new number, only press -1 to stop

