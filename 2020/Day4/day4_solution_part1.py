def get_keys(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    res = []
    li = []
    for i in doc:
    # print(i)
      for k in i.split(" "):
        li.append(k.split(":")[0])
      if(i == ""):
        res.append(li[:-1])
        li = []
        continue
    res.append(li)
  return res

def isvalid(li):
  if 'cid' in li:
    li.remove("cid")
  #print(li)
  if (len(li)>=7):
    return 1
  return 0

if __name__=="__main__":
        filename = './input.txt'
        input = get_keys(filename)
        result = 0
        for i in input:
          result+=isvalid(i)
         # print(i, isvalid(i))
        print(result)
