def txt_to_array(filename):
        with open(filename) as f:
                data = f.read().splitlines()
                data = list(data)
        return list(data)

def check_seatid(str):
	input = str
	low_r, low_c = 0, 0
	high_r, high_c= 127, 7
	act_c =act_r = res = 0
	for i in range(len(input)):
		if i<7:
			if(input[i]=="F"):
				high_r = (high_r+low_r)//2
				act_r = high_r
			elif(input[i]=="B"):
				low_r=((high_r+low_r)//2)+1
				act_r = low_r
		else:
			if(input[i]=="L"):
				high_c = (high_c+low_c)//2
				act_c = high_c
			elif(input[i]=="R"):
				low_c=((high_c+low_c)//2)+1
				act_c = low_c
	return act_r*8+act_c

if __name__=="__main__":
		filename = './input.txt'
		input = txt_to_array(filename)
		li = []
		for i in input:
			li.append(check_seatid(i))
		li.sort()
		for i in range(li[0], li[-1]):
			if i not in li:
				print("Your Seat ID is", i)
