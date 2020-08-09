"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('foo.txt', 'r')
with open('foo.txt') as f:
    read_data = f.read()
    for info in read_data:
        print(info, end='')
    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

word = open('bar.txt', 'w')
word.write('hello world, take me your leader,\n i am a tree..from animal crossing.\n give me potato chips.')

text = open('bar.txt', 'r')
with open('bar.txt', 'r'):
    read_data = text.read()
    for info in read_data:
        print(info, end='')
    text.close()

