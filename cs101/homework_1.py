# Question 2
# Write out Python code that prints out the number of hours in 7 weeks:

num_of_weeks = 7
days_in_week = 7
hours_in_day = 24

print num_of_weeks * days_in_week * hours_in_day

# Question 4
#Write Python code that stores the distance 
#in meters that light travels in one 
#nanosecond in the variable, nanodistance. 

#These variables are defined for you:
speed_of_light = 299800000. #meters per second
nano_per_sec = 1000000000. #1 Billion

#After your code,running
#print nanodistance
#should output 0.2998

nanodistance = speed_of_light / nano_per_sec

print nanodistance

# Question 6
#Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
#write Python code that prints out udacious
#without using any quote characters in
#your code.

#DO NOT USE IMPORT

udacious = s[0:2] + t[3:]

print udacious

# Question 7
text = "first hoo"
text.find('hoo')

# Question 8
#Assume text is a variable that
#holds a string. Write Python code
#that prints out the position
#of the second occurrence of 'zip'
#in text, or -1 if it does not occur
#at least twice.

#For example,
#   text = 'all zip files are zipped' -> 18
#   text = 'all zip files are compressed' -> -1
text = "all zip files are zipped"
print text.find('zip', text.find('zip')+3)

# Problem 9
#Given a variable, x, that stores
#the value of any decimal number,
#write Python code that prints out
#the nearest whole number to x.

#You can assume x is not negative.

# x = 3.14159 -> 3 (not 3.0)
# x = 27.63 -> 28 (not 28.0)

x = 3.14159

print str(round(x))[0:str(round(x)).find('.')]
