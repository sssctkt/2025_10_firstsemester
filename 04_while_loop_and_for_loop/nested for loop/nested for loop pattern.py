#objective: understand some "simple" nested for loop pattern

row=int(input("Enter the number of row: "))
for a in range(1, row+1, 1):
    for b in range(row, a-1, -1):
        print("*", end="") #end="" means continue on the same line
    print() #next line
