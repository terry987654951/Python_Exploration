# Name: Yuan-Hao Cheng
# ID: 933-048-737
# ONID: chengyua@oregonstate.edu

import sys, string, random

# Open the file. w means write, and + means create if necessary
f= open("first.txt","w+")
for i in range(10):
# Reference: https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
# Generate a lowercase character
    f.write(random.choice(string.ascii_lowercase))
f.write('\n')
# Reference: https://stackoverflow.com/questions/17440815/text-file-reading-and-printing-data
# Open file in read mode
f = open("first.txt", 'r')
# Copy content to a data (string)
data = f.read()
# Close the file
f.close()
# Print it out
for line in data:
    sys.stdout.write(line)


f= open("second.txt","w+")
for i in range(10):
    f.write(random.choice(string.ascii_lowercase))
f.write('\n')
f = open("second.txt", 'r')
# Copy content to a data (string)
data = f.read()
# Close the file
f.close()
# Print it out
for line in data:
    sys.stdout.write(line)

f= open("third.txt","w+")
for i in range(10):
    f.write(random.choice(string.ascii_lowercase))
f.write('\n')
f = open("third.txt", 'r')
# Copy content to a data (string)
data = f.read()
# Close the file
f.close()
# Print it out
for line in data:
    sys.stdout.write(line)


# Reference: https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
# Reference: https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
a = random.randint(1, 42)
b = random.randint(1, 42)
print (a)
print (b)
print(a*b)
