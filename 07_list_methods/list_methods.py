#list
"""
#review
a_list=["history", 30] #len is 2
#print(a_list[2]) #error, because it is out of range
#index starts from 0

#list has two speical properties
#1. list mutatable
#2. aliasing (two names refer to the same thing)

another_list=a_list #aliasing-->the behaviour will be different from
#regular variable

a_list[1]=10 #mutatable
print(another_list) #it's behaviour is "opposite" to the regular variable
"""
#list methods, like the string methods, is to manipulate the list
#however, this time, some list descriptions DO NOT have the word "return"

a=[1,2,3,4,1, 2, 3, 4]
list.append(a, 77) #long way

print(a)
a.append("Friday!!") #short way
print(a)
#if you look at the list description, and the description does not have
#the word "return", the list has been edited, which you do not need to assign
#the method to anything
answer=list.index(a,1, 3, 5) #look at the index of content 1,
#starting from index 3 to 5
#if you see, it behaves exactly like string methods
print(answer)
answer=a.index(1, 3, 5)
print(answer)












