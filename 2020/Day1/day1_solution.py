import math
import re

def txt_to_array(filename):
	with open(filename) as f:
		data = f.read().splitlines()
		data = list(map(int, data))
	return list(set(data))

def sum_multiply_2(array):
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i]+array[j] == 2020:
				print(array[i]*array[j])

def sum_multiply_3(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
	        for k in range(j+1,len(array)):
	        	if array[i]+array[j]+array[k] == 2020:
	        		print(array[i]*array[j]*array[k])

if __name__=="__main__":
	filename = './input.txt'
	input = txt_to_array(filename)
	sum_multiply_2(input)
	sum_multiply_3(input)
