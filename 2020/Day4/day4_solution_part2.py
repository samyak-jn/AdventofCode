def get_keys(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    res = []
    li = []
    d={}
    for i in doc:
    # print(i)
      for k in i.split(" "):
        if k!="":
         d[k.split(":")[0]] = k.split(":")[1]
        else:
          d={}
        li.append(d)
      if(i == ""):
        res.append(li[:-1])
        li = []
        continue
    res.append(li)
  return res

def isvalid(dict_):
  li = list(dict_.keys())
  if 'cid' in li:
    li.remove("cid")
  if (len(li)>=7):
    return 1
  return 0

if __name__=="__main__":
  filename = './input.txt'
  input = get_keys(filename)
  total = 0
  act = []
  for i in input:
    act.append(i[0])
  for i in act:
    if(isvalid(i)):
      flag = True
      if not(int(i["byr"])>=1920 and int(i["byr"])<=2002):
        flag = False
      if not(int(i["iyr"])>=2010 and int(i["iyr"])<=2020):
        flag = False
      if not(int(i["eyr"])>=2020 and int(i["eyr"])<=2030):
        flag = False
      if(i["hgt"].endswith("cm")):
        check = int(i["hgt"].split("cm")[0])
        if not(check>=150 and check<=193):
          flag = False
      elif(i["hgt"].endswith("in")):
        check = int(i["hgt"].split("in")[0])
        if not(check>=59 and check<=76):
          flag = False
      else:
        flag=False
      if(i["hcl"].startswith("#")):
        master = ["0", "1", "2", "3", "4","5","6","7","8","9","a","b","c","d","e","f"]
        check = i["hcl"].split("#")[1]
        if not (set(list(check))).issubset(set(master)):
          print(check)
          flag = False
      else:
        flag = False
      master = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
      if (i["ecl"] not in master):
        flag=False
      # else False
      if (len(list(i["pid"])) != 9):
        flag = False
      if(flag):
        total+=1

print(total)
