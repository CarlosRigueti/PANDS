# Uses a variable to greet
# Author: Carlos Rigueti

name = "Carlos"
print ('hello ' + name )

# This won't work
age = 30
#Print ('Your age is ' + age)
print ('your age is ' + str(age))
print ('Hello {} \tYour age is {}'.format(name, age))