import numpy as np

filename = './data/RV1.txt'

file = open(filename, 'r')

# loop over lines
single_line = file.readline()
elements_of_line = single_line.split()
position_vector = np.array([float(elements_of_line[0]), 
                            float(elements_of_line[1]),
                            float(elements_of_line[2])])
print(position_vector)
file.close()
