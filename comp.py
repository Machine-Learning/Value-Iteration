import numpy as np

file1 = open('1.txt', 'r')
Lines1 = file1.readlines()
file1.close()

file2 = open('2.txt', 'r')
Lines2 = file2.readlines()
file2.close()

value = np.zeros((5,3,4,len(all_states),health+1))


for line 