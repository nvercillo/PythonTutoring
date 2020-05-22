def floor(num):
  s= str(num)
  x = ""
  i =0
  if num <0:
    i=1
  while i < len(s):
    if s[i] =='.':
      break
    x+=s[i]
    i+=1
  return int(x)

def dec2oct(x):
  if x ==0:
    return "0"  
  res = ""
  while x>0:
    res += str(x%8)
    x /=8
    x= floor(x)
  res+= 'O'
  return res[::-1]
