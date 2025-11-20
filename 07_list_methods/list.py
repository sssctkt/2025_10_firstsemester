#difference between list and string

#string
#sentence="ontario"
#sentence[0]="a"
#print(sentence) #you cannot do this in python
#because string is immutatable

a_list=["kwan", "computer sci", 40]
a_list[2]=90
print(a_list)
#because list is mutatable, you can do the above

#review, regular variable (int, float, string)
a=5
b=a
a=23456
print(b)

another_list=["kwan", 90]
p=another_list
another_list[1]=20
print(p) #list works differently



