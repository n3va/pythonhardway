# import variable argv
from sys import argv
# unpacks argv so it gets assigned to variables i can work with: script and filename
script, filename = argv

# defines opening the filename as txt
txt = open(filename)

# prints heres your "filename" and contents
print ("Here's your file %r:" % filename)
print (txt.read())

# prints file again
print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())

# closes text
txt_again.close()
