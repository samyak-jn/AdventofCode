def get_keys(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    res = []
    li = []
    for i in doc:
      if i != "":
        li.append(i)
      else:
        res.append(li)
        li=[]
  return res

if __name__=="__main__":
  filename = './input.txt'
  input = get_keys(filename)
  sum = 0
  result = []
  for i in input:
    check = "".join(i)
    result.append(list(set(list(check))))
  for i in result:
    sum+=len(i)
  print(f"Your puzzle answer was {sum}.")
