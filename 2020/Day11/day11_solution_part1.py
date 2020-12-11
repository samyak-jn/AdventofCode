import copy

def txt_to_array(filename):
    with open(filename) as f:
        mat = []
        data = f.read().splitlines()
        for i in data:
          mat.append(list(i))
    return mat

def get_adjacent(x, y):
  # 3*3-1 = 8 pairs, 1 seld (At center)
    return [
            {'x':(x - 1), 'y':(y - 1)},
            {'x':x, 'y':(y - 1)},
            {'x':(x + 1), 'y':(y - 1)},
            {'x':(x - 1), 'y':y},
            {'x':(x + 1), 'y':y},
            {'x':(x - 1), 'y':(y + 1)},
            {'x':x, 'y':(y + 1)},
            {'x':(x + 1), 'y':(y + 1)},
            ]



def get_adjacent_count(x, y, input):

    total = 0
    max_row = len(input)
    max_col = len(input[0])

    adjacents = get_adjacent(x, y)
    for i in adjacents:
        if(i['x'] < 0 or i['x'] >= max_col):
            continue
        if(i['y'] < 0 or i['y'] >= max_row):
            continue
        if input[i['y']][i['x']] == "#":
            total += 1
    return total;

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
        if get_adjacent_count(j, i, input) >= 4:
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
