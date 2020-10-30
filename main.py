
def meny(): #visa menyn
  print('1. Aritmetiskt summa')
  print('2. Temp.omvandlare, C->F')
  print('3. Pos.tal')
  print('4. Avsluta')
  övn()

# underprogram
def summa():
  tal = int(input('Heltal? '))
  for n in range(tal):
    tal = tal + n
    print(tal, n)
  övn()
def temp():
  C = float(input('Celsius? '))
  F = 1.8 * C + 32
  print(F)
  övn()
def plus():
  n = int(input ('pos.tal? '))
  if n <= 0:
    plus()
  print(n)
  övn()

def övn(): # välj underprogram
  val = input('Välj!!!')
  if val == '1': 
    summa()
  elif val == '2':
    temp()
  elif val == '3':
    plus()
  elif val == '4':
    print('Tack & hej!')
  else:
    print('Nu brev det fel, va???')
    meny()

meny() # visa menyn