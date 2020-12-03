
def txt_to_array(filename):
	with open(filename) as f:
		data = f.read().splitlines()
		data = list(data)
	return list(set(data))


if __name__=="__main__":
	filename = './input.txt'
	input = txt_to_array(filename)
	result = 0
	print(len(input))
	for i in input:
		j=i.split(" ")
		total = 0
		low = int(j[0].split("-")[0])
		high = int(j[0].split("-")[1])
		char = j[1].split(":")[0]
		passwd = list(j[2])
		if(passwd[low-1] == char and passwd[high-1] != char):
			result +=1
		elif(passwd[low-1] != char and passwd[high-1] == char):
			result +=1
	print(result)
