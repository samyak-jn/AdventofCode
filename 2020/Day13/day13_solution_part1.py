def txt_to_array(filename):
    with open(filename) as f:
        mat = []
        data = f.read().splitlines()
        timestamp = int(data[0])
        bus_IDs = data[1].split(",")
    return timestamp, bus_IDs

def fastbus(timestamp, bus_IDs):
  available_bus = []
  for i in bus_IDs:
    if i != "x":
      available_bus.append(int(i))
  flag = True
  check = timestamp
  while(flag):
    mod = [check%i for i in available_bus]
    if 0 in mod:
      index = mod.index(0)
      return (check - timestamp)*available_bus[index]
      flag = False
    else:
      check+=1

if __name__=="__main__":
  filename = "./input.txt"
  timestamp, bus_IDs = txt_to_array(filename)
  earliest_bus = fastbus(timestamp, bus_IDs)
  print(f"{earliest_bus} is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus.")
