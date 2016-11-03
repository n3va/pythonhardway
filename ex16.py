
from sys import argv

script, filename = argv
# calls name of file from what you write in terminal
print ("we're going to erase %r." % filename)
print ("if you don't want that, hit CTRL-C (^C).")
print ("if you do want that, hit RETURN.")
# prompts input for RETURN or CTRL-C
input("?")
# opens file in write mode: 'w'
print ("opening the file...")
target = open(filename, 'w')
# deletes contents of file
print ("truncating the file. goodbye!")
target.truncate()

print ("now i'm going to ask you for three lines")
# prompts text input for new contents of file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file")
# writes above contents into file
tw = target.write
tw(line1)
tw("\n")
tw(line2)
tw("\n")
tw(line3)
tw("\n")
# closes file
print ("and finally, we close it.")
target.close()
