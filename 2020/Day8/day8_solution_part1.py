def get_keys(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    li = []
    for i in doc:
      operation = i.split(" ")[0].strip()
      value = int(i.split(" ")[1].strip())
      li.append([operation, value])
     # res.append(li)
  return li

def compute_acc(input):
  pc = 0
  ac = 0
  i = 0
  while(i!=1000):
    if(input[pc][0]=="visited"):
      return ac
  #  print(input[pc][0], pc, ac)
    i+=1
    if(input[pc][0]=="nop"):
      input[pc][0] = "visited"
      pc+=1
    elif(input[pc][0]=="acc"):
      input[pc][0] = "visited"
      ac+=input[pc][1]
      pc+=1
    elif(input[pc][0]=="jmp"):
      input[pc][0] = "visited"
      pc+=input[pc][1]

if __name__=="__main__":
  filename = "./input.txt"
  input = get_keys(filename)
  result = compute_acc(input)
  print("Your accumulator value is", result)
