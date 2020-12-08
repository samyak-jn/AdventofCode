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

def complete_acc(input):
  for i in range(len(input)):
    input_ = deepcopy(input)
    if input_[i][0] == "acc":
      continue
    else:
      if input_[i][0] == "jmp":
        input_[i][0] = "nop"
      else:
        input_[i][0] = "jmp"
    seen = set()
    pc = 0
    ac = 0 
    i=0
    seen = set()
    while(pc<len(input_)):
      if pc in seen:
        break
      seen.add(pc)
      if(input_[pc][0]=="nop"):
        pc+=1
      elif(input_[pc][0]=="acc"):
        ac+=input_[pc][1]
        pc+=1
      elif(input_[pc][0]=="jmp"):
        pc+=input_[pc][1]
      i+=1
    else:
      print("Your loops has been terminated successfully!")
      return ac

if __name__=="__main__":
  filename = "./input.txt"
  input = get_keys(filename)
  result = complete_acc(input)
  print("Your accumulator value is", result)

