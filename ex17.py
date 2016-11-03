from sys import argv; from os.path import exists; script, from_file, to_file, = argv

print ("copying from %s to %s" % (from_file, to_file))

indata = open(from_file).read()

print ("the input file is %d bytes long" % len(indata), "\n", "does the output file exist? %r" % exists(to_file), "\n", "ready, hit RETURN to continue, CTRL-C to abort" ); input()

out_file = open(to_file, 'w').write(indata)

print ("alright, all done")
