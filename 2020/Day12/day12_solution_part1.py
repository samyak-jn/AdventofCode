def txt_to_array(filename):
    with open(filename) as f:
        mat = []
        data = f.read().splitlines()
        for i in data:
          tmp = list(i)
          num = "".join([i for i in tmp[1:]])
          mat.append([tmp[0],int(num)])
    return mat

def ship_distance(input):
  direction_dic = {"N":0, "S":0, "E":0, "W":0}
  ship_dir = "E"
  for i in input:
    direction = i[0]
    magnitude = i[1]
    if (direction == "F"):
      direction_dic[ship_dir] += magnitude
    elif (direction == "R"):
      i = 0
      while(i != magnitude//90):
        if (ship_dir == "N"):
          ship_dir = "E"
        elif (ship_dir == "E"):
          ship_dir = "S"
        elif (ship_dir == "S"):
          ship_dir = "W"
        elif (ship_dir == "W"):
          ship_dir = "N"
        i+=1
        direction = ship_dir
    elif (direction == "L"):
      i=0
      while(i != magnitude//90):
        if (ship_dir == "N"):
          ship_dir = "W"
        elif (ship_dir == "W"):
          ship_dir = "S"
        elif (ship_dir == "S"):
          ship_dir = "E"
        elif (ship_dir == "E"):
          ship_dir = "N"
        i+=1
        direction = ship_dir
    else:
      direction_dic[direction] += magnitude
    res_distance = abs(direction_dic["E"]-direction_dic["W"]) + abs(direction_dic["N"]-direction_dic["S"]) 
  return res_distance

if __name__=="__main__":
  filename = "./input.txt"
  input = txt_to_array(filename)
  resultant_distance = ship_distance(input)
  print(f"{resultant_distance} is the Manhattan distance between that location and the ship starting position.")
