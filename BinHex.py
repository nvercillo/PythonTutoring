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

def hex2dec(x):
    chars = {}
    for i in range(0, 10):
      chars[str(i)] = i
    chars["A"] = 10
    chars["B"] = 11
    chars["C"] = 12
    chars["D"] = 13
    chars["E"] = 14
    chars["F"] = 15
    string = str(x)
    dec = 0;
    for i in range(0,len(string)):
      if string[i] != "0":
        dec += 16**(len(string)-1-i) * chars[string[i]];
    return dec


print(hex2dec('2A'))
print(hex2dec('C0FFEE'))
