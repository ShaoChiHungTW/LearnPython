# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:14:34 2017

@author: Kiki Hung
"""
#字上色
from termcolor import colored
print(colored("Learn Python The Hard Way", "green"))
print "-"*20
#Ex3
print(colored("Exercise 3 Numbers and Math", "red"))
print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
#30
print "Roosters", 100 - 25 * 3 % 4
# %餘數 97
print "Now I will count the eggs:"
print 3+2+1-5+4%2-1/4+6
#1+0-0.25+6=7.25
print "Is it true that 3 + 2 < 5 - 7 ? "
#Python會直接判斷,不用寫判斷式print
#a = 3+2;
#if a < 5 - 7:
#    print "True."
#else:
#    print "False."
print 3+2 < 5-7
print "What is 3 + 2 ?" , 3+2
print "What is 5 - 7 ?" , 5-7
print "Oh, that's why it's false."
print "How about some more?"
print "Is 5 greater than -2 ?", 5>-2
print "Is 5 greater or equal than -2 ?" , 5>=-2
print "Is 5 less or equal than -2 ?" , 5<=-2
print "-"*20
#Ex4
print(colored("Exercise 4 Variables and Names", "red"))
cars = 100;
space_in_a_car = 4.0;
drivers = 30;
passengers = 90;
cars_not_driven = cars - drivers;
cars_driven = drivers;
carpool_capacity = cars_driven * space_in_a_car;
average_passengers_per_car = passengers / cars_driven;
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print"-"*20
#Ex5
print(colored("Exercise 5 More Variables and Printing", "red"))
my_name = "Kiki Hung"
my_age = 18
my_height = 157
my_weight = 48
my_eyes = "Black"
my_teeth = "White"
my_hair = "Brown"

print " Let's talk about %s." % my_name
print " I am %d cm tall." % my_height
print " I am %d kg weight." % my_weight
print " I got %s eyes and %s hair." %(my_eyes, my_hair)
print "If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age+my_height+my_weight)
print "-"*20
#Ex6
print(colored("Exercise 6 Strings and Text", "red"))
x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)
print x
print y
#%r 會加引號
print "I said: %r" %x
print "I also said: '%s'." %y
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"
print joke_evaluation %hilarious
w = "This is the left side of ..."
e = "a string with a right side."
print w+e
print "-"*20
#Ex7
print(colored("Exercise 7 More Printing" , "red"))
print "Mary had a little lamb."
print "Its fleece was white as %s." %'snow'
sn = "snow"
print "Its fleece was white as %r." % sn
print "And everywhere that Mary went."
print "." * 10
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
#Removing comma 會直接換行
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12
print "-"*20

#Ex8
print(colored("Exercise 8 Printing, Printing", "red"))
formatter = "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False , True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter %( "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
print "-"*20

#Ex9
print(colored("Exercise 9 Printing, Printing, Printing", "red"))
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days:" , days
print "Here are the months:", months
print """There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6."""
#"""可任意行數"""
#%r是原始呈現
print "-"*20

#Ex10
print(colored("Exercise 10 What was that?" , "red"))
#多加一個\ 以免混淆引號
print "I am 6'2\' tall."
print 'I am 6\'2" tall.'
#\t 空格空格
tab_cat = "\t I'm tabbed in."
#\non 換行
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
  * cat food* fish
    \t* catnip \n\t* Grass
  """
print tab_cat
print persian_cat
print backslash_cat
print fat_cat   















