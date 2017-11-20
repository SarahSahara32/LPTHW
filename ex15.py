from sys import argv

script, filename = argv

# open the textfile with the filename I typed in
txt = open(filename)

# print the info text with the filename
print "Here's your file %r:" % filename
# command of printing the text in the textfile
print txt.read()

# print the text
print "Type the filename again:"
# user should type file name again
file_again = raw_input("> ")

# depending on raw_input the file will be opened again
txt_again = open(file_again)

# text from the file will be printed again
print txt_again.read()

# recommendation to close on txt. and txt_again
txt.close()
txt_again.close()
