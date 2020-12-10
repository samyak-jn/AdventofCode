#!/usr/bin/python3

def get_values(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    li = []
    for i in doc:
      if(i==''):
      	continue
      li.append(int(i.strip()))
  return li

if __name__=="__main__":
  filename = "./input.txt"
  input = get_values(filename)
  input = sorted(input)
  inbuilt_adapter = input[-1]+3
  d = {1:0,2:0,3:0}
  if(input[0]!=0):
    d[input[0]] = 1
  for i in range(len(input)):
    check = input[i]
    for j in range(i, len(input)):
      if(input[j] == check+1):
        d[1]+=1
        break
      if(input[j] == check+2):
        d[2]+=1
        break
      if(input[j] == check+3):
        d[3]+=1
        break
  d[inbuilt_adapter-check] += 1
  print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences {d[1]*d[3]}.")
