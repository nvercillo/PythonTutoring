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

def dec2hex(x):
    chars = {}
    for i in range(0, 10):
      chars[i] = i
    chars[10] = "A"
    chars[11] = "B"
    chars[12] = "C"
    chars[13] = "D"
    chars[14] = "E"
    chars[15] = "F"
    if x ==0:
      return "0"  
    res = ""
    while x>0:
      res += str(chars[x%16])
      x /= 16
      x= floor(x)
    res+= "H"
    return res[::-1]

