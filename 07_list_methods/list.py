#question ask ppl to enter year month and date
year=int(input("Enter year: "))
month=int(input("Enter month: "))
date=int(input("Enter date: "))

#example
#2000
#1
#30
#output will be 2000, January, 30

month_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(year, month_list[month-1], date)
