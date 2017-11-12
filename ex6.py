# string for variable x
x = "There are %d types of people." % 10
# string for variable binary
binary = "binary"
# string for variable do_not
do_not = "don't"
# string for variable y with two variables included
y = "Those who know %s and those who %s." % (binary, do_not)

# print variable x
print x
# print variable y
print y

# print string including the string for variable x
print "I said: %r." % x
# print string including the string for variable y
print "I also said: '%s'." % y

# variable hilarious defined as false
hilarious = False
# variable joke_evaluation defined as string
joke_evaluation = "Isn't that joke so funny?! %r"

# print variable joke_evaluation and refer to var hilarious for the %
print joke_evaluation % hilarious

# string for var w
w = "This is the left side of..."
# string for var e
e = "a string with a right side."

# print string w plus e 
print w + e
