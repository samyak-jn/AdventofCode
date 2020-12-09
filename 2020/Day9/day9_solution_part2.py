def get_values(filename):
  with open(filename) as f:
    data = f.read()
    doc = data.split("\n")
    li = []
    for i in doc:
      li.append(int(i.strip()))
  return li

def check_sum(nums, k):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == k:
        return True
  return False

def return_culprit(input):
  for i in range(25,len(input)):
    tmp = input[i-25:i]
    if (check_sum(tmp, input[i]) is False):
      return input[i]

def check_set_for_num(num):
  for j in range(20):
    for i in range(j, len(input)):
      tmp = input[i-j:i]
      if(sum(tmp) == num and len(tmp)>=2):
        sorted(tmp)
        res = tmp[0]+tmp[-1]
        return res

if __name__=="__main__":
  filename = "./input.txt"
  input = get_values(filename)
  print("Your answer to the part1 is", return_culprit(input))
  print("Your answer to the part1 is", check_set_for_num(return_culprit(input)))
