
def txt_to_array(filename):
    with open(filename) as f:
        mat = []
        data = f.read().splitlines()
        for i in data:
          mat.append(list(i))
    return mat

def no_of_trees(res, slope):
	trees = 0
	x=y=0
	while(x<len(res)):
		check = res[x][y]
		if check == "#":
			trees+=1
		x+=slope[0]
		y+=slope[1]
		y%=len(res[0])
	return trees

if __name__=="__main__":
	filename = './input.txt'
	input = txt_to_array(filename)
	print("Ans to solution 1:", no_of_trees(input, [1,3]))
	print("Ans to solution 2:", no_of_trees(input, [1,3])*no_of_trees(input, [1,1])* no_of_trees(input, [1,5])* no_of_trees(input, [1,7])* no_of_trees(input, [2,1]))
