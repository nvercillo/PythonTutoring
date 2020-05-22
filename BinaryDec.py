
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

def bin2dec(x):
    string = str(x)
    dec = 0;
    for i in range(0,len(string)):
      if string[i] =="1":
        dec += 2**(len(string)-1-i)
    return dec



# print(dec2bin(0))
# print (dec2bin(15))
# print (dec2bin(999999999))
