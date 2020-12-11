import copy

def txt_to_array(filename):
    with open(filename) as f:
        mat = []
        data = f.read().splitlines()
        for i in data:
          mat.append(list(i))
    return mat

def get_adjacent_count(x, y, input):
  total = 0
  # going up, the row will decrease while coloumn will be intact
  for i in range(y-1, -1, -1):
    if(input[i][x] == "#"):
      total+=1
      break
    elif(input[i][x] == "L"):
      break
  # going up, the row will increase while coloumn will be intact
  for i in range(y+1, len(input), 1):
    if(input[i][x] == "#"):
      total+=1
      break
    elif(input[i][x] == "L"):
      break
  # going left, the row will be intact while coloumn will decrease
  for i in range(x-1, -1, -1):
    if(input[y][i] == "#"):
      total+=1
      break
    elif(input[y][i] == "L"):
      break
  # going right, the row will be intact while coloumn will increase
  for i in range(x+1, len(input[0]), 1):
    if(input[y][i] == "#"):
      total+=1
      break
    elif(input[y][i] == "L"):
      break
# now diagnols will have 4 sides to go through upper left, upper right, down left, down right
  upper_left = False
  upper_right = False
  down_left = False
  down_right = False
  for i in range(1, min(len(input[0]), len(input))):
    #upper left
    tmpx = x-i
    tmpy = y-i
    if not (tmpx<0 or tmpy<0) and not upper_left:
      if input[tmpy][tmpx] == "#":
        total+=1
        upper_left = True
      elif input[tmpy][tmpx] == "L":
        upper_left = True
    #upper right
    tmpx = x+i
    tmpy = y-i
    if not (tmpx>=len(input[0]) or tmpy<0) and not upper_right:
      if input[tmpy][tmpx] == "#":
        total+=1
        upper_right = True
      elif input[tmpy][tmpx] == "L":
        upper_right = True
    #down left
    tmpx = x-i
    tmpy = y+i
    if not (tmpx<0 or tmpy>=len(input)) and not down_left:
      if input[tmpy][tmpx] == "#":
        total+=1
        down_left = True
      elif input[tmpy][tmpx] == "L":
        down_left = True
    #down right
    tmpx = x+i
    tmpy = y+i
    if not (tmpx>=len(input[0]) or tmpy>=len(input)) and not down_right:
      if input[tmpy][tmpx] == "#":
        total+=1
        down_right = True
      elif input[tmpy][tmpx] == "L":
        down_right = True
  return total


def fill_seat(input):
  tmp = copy.deepcopy(input)
  for i in range(len(input)):
    for j in range(len(input[i])):
      if tmp[i][j] == ".":
        continue
      if tmp[i][j] == "L":
        if get_adjacent_count(j, i, input) == 0:
          tmp[i][j] = "#" 
      if tmp[i][j] == "#":
        if get_adjacent_count(j, i, input) >= 5:
          tmp[i][j] = "L"
  return tmp

def count_seat(input):
  total = 0
  for i in range(len(input)):
    for j in range(len(input[i])):
      if(input[i][j]=="#"):
        total+=1
  return total

if __name__=="__main__":
  filename = "./input.txt"
  input = txt_to_array(filename)
  prev = copy.deepcopy(input)
  next = copy.deepcopy(input)

  check = 0
  while(prev!=next or check ==0):
    prev = copy.deepcopy(next)
    next = fill_seat(next)
    check+=1

  count = count_seat(next)
  print(f'{count} seats end up occupied!')
