def get_values(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    li = []
    for i in doc:
      if i =="":
        continue
      li.append(int(i.strip()))
  return li

if __name__=="__main__":
  filename = "./input.txt"
  input = get_values(filename)
  input.append(0)
  input = sorted(input)
  inbuilt_adapter = input[-1]+3
  input.append(inbuilt_adapter)
  parse_ways = [0]*(max(input)+1)
  parse_ways[0]=1
  for i in input[1:]:
    parse_ways[i] += parse_ways[i-1]
    if i>=2:
      parse_ways[i] += parse_ways[i-2]
    if i>=3:
      parse_ways[i] += parse_ways[i-3]
  print(parse_ways[-1])
