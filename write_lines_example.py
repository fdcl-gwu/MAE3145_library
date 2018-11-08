# Write to a text file line by line

import numpy as np

# open the file
file = open("test.txt", 'w')
# loop over lines and write each line to the file
string = ""

for index in range(10):
    string = string + "Here is line {}\n".format(index)

    # file.write("Here is line {}\n".format(index))

# close file

file.write("\n")
file.write(string)

file.close()
