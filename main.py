def meny(): #visa menyn
  print('1. Aritmetiskt summa')
  print('2. Temp.omvandlare, C->F')
  print('3. Pos.tal')
  print('4. Avsluta')
  övn()

# underprogram
def summa(tal):
  for n in range(tal):
    tal = tal + n
  return tal  
def temp(C):
  F = 1.8 * C + 32
  return F
def plus(n):
  return n
  
def övn(): # välj underprogram
  val = input('Välj!!!')
  if val == '1': 
    tal = int(input('Heltal? '))
    print(summa(tal))
    övn()
  elif val == '2':
    t = float(input('Celsius? '))
    print(temp(t))
    övn()
  elif val == '3':
    x=0
    while x<=0:
      x = int(input('pos.tal? '))
    print(plus(x))
    övn()
  elif val == '4':
    print('Tack & hej!')
  else:
    print('Nu brev det fel, va???')
    meny()

meny() # visa menyn