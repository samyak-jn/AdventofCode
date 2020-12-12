def txt_to_array(filename):
    with open(filename) as f:
        mat = []
        data = f.read().splitlines()
        for i in data:
          tmp = list(i)
          num = "".join([i for i in tmp[1:]])
          mat.append([tmp[0],int(num)])
    return mat

def waypoint_relative_ship(input):
  wavepoint = {"N":1, "E":10, "S":0, "W":0}
  ship_dir = {"N":0, "S":0, "E":0, "W":0}
  for i in input:
    direction = i[0]
    magnitude = i[1]
    if (direction == "F"):
      for x, y in wavepoint.items():
        ship_dir[x] += wavepoint[x]*magnitude
    elif (direction == "R"):
      i = 0
      while(i != magnitude//90):
        d = {}
        for value, y in wavepoint.items():
          if (value == "N"):
            d["E"] = y
          elif (value == "E"):
            d["S"] = y
          elif (value == "S"):
            d["W"] = y
          elif (value == "W"):
            d["N"] = y
        del wavepoint
        wavepoint = d 
        i+=1
    elif (direction == "L"):
      i = 0
      while(i != magnitude//90):
        d = {}
        for value, y in wavepoint.items():
          if (value == "N"):
            d["W"] = y
          elif (value == "E"):
            d["N"] = y
          elif (value == "S"):
            d["E"] = y
          elif (value == "W"):
            d["S"] = y
        del wavepoint
        wavepoint = d
        i+=1
    else:
      wavepoint[direction] += magnitude
  res_distance = abs(ship_dir["E"]-ship_dir["W"]) + abs(ship_dir["N"]-ship_dir["S"])
  return res_distance

if __name__=="__main__":
  filename = "./input.txt"
  input = txt_to_array(filename)
  resultant_distance = waypoint_relative_ship(input)
  print(f"{resultant_distance} is the Manhattan distance between that location and the ship starting position.")
