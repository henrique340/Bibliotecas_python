import math

while True:
  print(f'''
[1] Menor número inteiro
[2] Maior número inteiro
[3] Parte inteira
[4] Sair
''')
  
  opc = int(input('Digite a sua opção: '))

  if opc == 1:
    x = float(input('Digite o número: '))
    resultado = math.ceil(x)
    print(resultado)
  elif opc == 2:
    x = float(input('Digite o número: '))
    resultado = math.floor(x)
    print(resultado)
  elif opc == 3:
    x = float(input('Digite o número: '))
    resultado = math.trunc(x)
    print(resultado)
  elif opc == 4:
    break
  else:
    print('Digite uma opção válida')