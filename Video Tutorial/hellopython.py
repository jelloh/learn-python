# Tutorial:
# https://www.youtube.com/watch?v=N4mEzFDjqtA

import random # Random Number Generator
import sys
import os # Operating System (?? not sure)

print("Hello World")

# Comment
'''
Multiline Comment
'''

name = "Teddy Bear"
print(name)

# 5 main data types:
# Numbers String Lists Tuples Dictionaries/Maps

# 7 Operators:
# + - * / % ** //
# ** -> power
# // -> floor division (like integer division pretty much)

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

# Order of Operation Matters

# This is a String
quote = "\"Always remember you are unique\""
#print(quote)

multi_line_quote = '''just
like
everyone
else'''
#print(multi_line_quote)

new_string = quote + multi_line_quote
#print(new_string)

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
# I guess this is similar to the printf in java

#print("%s %s %s" % ('hello there', quote, '\nhihihihihi'))

# Gets rid of the newline at the end of the print statement
print("I don't like ", end="")
print("newlines")

# This would put a newline at the end of the first statement
print("I don't like ", end="\n")
print("newlines")

# Below would print 5 new lines. oh man. very cool.
print('\n' * 5)
print('hi')

print('hi' * 5) # Print 5 'hi's right beside eachother

# --------------------------------------------------------------
# ------------------- LISTS -----------------------------------
grocery_list = ['Juice', 'Tomatoes', 'Icecream',
                'Potatoes']

print('First Item', grocery_list[0])
grocery_list[0] = "Green Juice" # To Change Values
print('First Item', grocery_list[0])

print(grocery_list[1:3]) # Prints a subset of a list
# Displays: ['Tomatoes', 'Icecream']
# 1 is INCLUSIVE, 3 is EXCLUSIVE

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
print(to_do_list)
# LISTS INSIDE LISTSSS. WOAHHHh

print((to_do_list[0][1]))
# Uses first list, and then 2nd item in that list
# Basically 2d arrays

# Append Items
grocery_list.append('Onions') # Adds Onions to the end of grocery_list
print(to_do_list)

grocery_list.insert(1, "Pickle")
print(to_do_list)
grocery_list.remove("Pickle")

grocery_list.sort()
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list
print(len(to_do_list2)) # length of list
print(max(to_do_list2)) # Prints "Wash Car"
print(min(to_do_list2)) # Prints "Cash Check"



#---------------------------------------------------------
#--------------- TUPLES ----------------------------------
# You cannot change a Tuple after it's created

pi_tuple = (3,1,4,1,5,9)
print(pi_tuple)

new_tuple = list(pi_tuple) # converts a tuple to a list
print(new_tuple)

new_list = tuple(new_tuple) # converts a list to a tuple
print(new_list)

# Similar as lists:
# len(tuple) min(tuple) max(tuple)


#----------------------------------------------------------------
#--------------- DICTIONARIES  ----------------------------------
# AKA Maps. Same thing.
# Made up of values with a UNIQUE KEY for each Item
# Similar to lists, but you cant combine any, etc..

# Dictionary of super villians
# 1st = villian name, 2nd = secret identity (?)
super_villians = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}

print(super_villians['Captain Cold']) # Prints "Leonard Snart"

del super_villians['Fiddler'] # Deletes Fiddler

print(super_villians['Pied Piper']) # Prints Thomas Peterson
super_villians['Pied Piper'] = 'Hartley Rathaway'
print(super_villians['Pied Piper']) # Prints Hartley Rathaway


# I'VE BEEN SPELLING VILLAINS WRONG THIS WHOLE TIME. OOPS
print(len(super_villians))
print(super_villians.get("Pied Piper"))
print(super_villians.keys())
print(super_villians.values())


#----------------------------------------------------------------
#--------------- CONDITIONALS  ----------------------------------

# if else elif

age = 21

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

if age >= 21 :
    print('You are old enough to do stuff')
elif age >= 16 :
    print('You are old enough to drive a car')
else :
    print("You are not old enough to drive")

# and or not <- logical Operators

if ((age >= 1) and (age <= 18)) :
    print("you get a birthday")
elif ((age == 21) or (age >= 65)) :
    print("You get a birthday")
elif not(age == 30) :
    print("You don't get a birthday")
else :
    print("You get a party. yay")



#----------------------------------------------------------------
#--------------------- LOOPS  ----------------------------------

# FOR LOOPS ------------------
# Goes from 0 to 9
for x in range(0, 10):
    print(x, ' ', end="")

print('\n')

# Using grocery list from above
for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x)

# nested for loops with 2d array
num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0, 3):
    for y in range(0,3):
        print(num_list[x][y])

# WHILE LOOPS ------------------

random_num = random.randrange(0, 100) # from 0 to 99

# originally: (random_num != 15) ... just changed it around for fun
while(not random_num == 15):
    print(random_num)
    random_num = random.randrange(0, 100)

print(random_num)

i = 0; # iterator
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break # breaks out of loops
    else: # This last else is just for demonstration purpose. same outcome with or without it (b/c the 'continue')
        i += 1 # i = i + 1
        continue # breaks out of current iteration

    i += 1
# end while loop

#----------------------------------------------------------------
#--------------------- FUNCTIONS  ----------------------------------

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

# Make sure you define functions before you call to used

print(addNumber(1,4))
string = addNumber(1, 4)
# print(sumNum) wouldnt work b/c SCOPE stuff

# -------------------------
# Getting inupt from USER
'''
print('What is your name')
name = sys.stdin.readline() #why we import sys stuff at the beginning
print('Hello', name)

'''

long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4]) # 0 inclusive, 4 EXCLUSIVE
print(long_string[-5:]) # print last 5 characters
print(long_string[:-5]) # prints everything up until the 5th to last characters
print(long_string[:4] + " be there") # so you can concact with + too
print("%c is my %s letter and my number %d number is %.3f" %
       ('X','favorite',1,.14))

print(long_string.capitalize())
print(long_string.find("Floor")) #returns index. this is case sensitive*
print(long_string.isalpha()) # all letters. T/F
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())
quote_list = long_string.split(" ") # Converts string to list, with " " being the delimiter
print(quote_list)



#----------------------------------------------------------------
#--------------------- FILE I/O  ---------------------------------
'''
test_file = open("test.txt", "wb") # "wb" is to write to a FILE#
                                   # "ab+" to read and append to FILE
print(test_file.mode) # prints mode ("wb")
print(test_file.name) # prints name

test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close() # closes FILE


# Read info from a file:
test_file = open("test.txt", "r+") # reading and writing (r+)

text_in_file = test_file.read() # read from the file and save it in var
print(text_in_file) #print file based on the var above

os.remove("test.txt") # removes i guess?
'''


#----------------------------------------------------------------
#--------------------- OBJECT ORIENTED STUFF  ---------------------------------

class Animal:
    __name = None # None symbollizes lack of a value. can also use ""
    __height = 0
    __weight = 0
    __sound = 0   # 2 underscores means PRIVATE variable

    # This is a CONSTRUCTOR
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    # self is to refer to the object itself (that specific object)
    def set_name(self, name):
        # I added this if statement
        if(name.isalpha()):
            self.__name = name
        else:
            print("Invalid name. No changes made")

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    # Used for demontrating Polymorphism
    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                      self.__height,
                                                                      self.__weight,
                                                                      self.__sound)



# Out of class

cat = Animal("Whiskers", 33, 10, 'Meow')
print(cat.toString())


# INHERITANCE O.O

#In this, you are inheriting from the Animal class
class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        # Now to have name, height... etc handled by the Animal super class
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    # With this, we are overwriting the superclass's (Animal) toString method
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {} His owner is {}".format(self.get_name(),
                                                                               self.get_height(),
                                                                               self.get_weight(),
                                                                               self.get_sound(),
                                                                               self.__owner)



    # Method overloading.
    def multiple_sounds(self, how_many=None): # Means it is okay to leave it empty for how_many
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


# end class

spot = Dog("Spot", 53, 27, "Ruff", "Bob")
print(spot.toString())
print(spot.get_name())
print(spot.get_owner())

# POLYMORPHISMMMMM

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat) # Prints Animal (calls the animal verson of get_type)
test_animals.get_type(spot) # Prints Dog  (calls the dog verson of get_type, even
                                        #    tho dog belons to animal class)

spot.multiple_sounds(4)
spot.multiple_sounds()
