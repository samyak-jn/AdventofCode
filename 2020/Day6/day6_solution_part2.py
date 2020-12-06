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
  sum=0
  for i in input:
    if(len(i) == 1):
      sum+=len(list(i[0]))
    else:
      tmp = []
      for j in i:
        tmp.append(list(j))
      result = set(tmp[0])
      for s in tmp[1:]:
        result.intersection_update(s)
      sum+=len(result)
  print("Your puzzle answer was", sum)
