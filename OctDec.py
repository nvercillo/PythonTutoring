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

def oct2dec(x):
    string = str(x)
    dec = 0;
    for i in range(0,len(string)):
      if string[i] !="0":
        dec += 8**(len(string)-1-i) * int(string[i])
    return dec


print(oct2dec(15253))
print(oct2dec(16))
