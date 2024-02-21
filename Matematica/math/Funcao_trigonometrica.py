import math

while True:
  print('Funções trigonométricas')
  print('''[1] Seno
  [2] Cosseno
  [3] Tangente
  [4] Arco seno
  [5] Arco cosseno
  [6] Arco tangente
  [7] Sair
  ''')
  opc = int(input('Digite a opção desejada: '))

  if opc == 1:
    num = int(input('Digite o número para calcular: '))
    resultado = math.sin(num)
    print(f'O resultado é {resultado}')
  elif opc == 2:
    num = int(input('Digite o número para calcular: '))
    resultado = math.cos(num)
    print(f'O resultado é {resultado}')
  elif opc == 3:
    num = int(input('Digite o número para calcular: '))
    resultado = math.tan(num)
    print(f'O resultado é {resultado}')
  elif opc == 4:
    num = int(input('Digite o número para calcular: '))
    resultado = math.asin(num)
    print(f'O resultado é {resultado}')
  elif opc == 5:
    num = int(input('Digite o número para calcular: '))
    resultado = math.acos(num)
    print(f'O resultado é {resultado}')
  elif opc == 6:
    num = int(input('Digite o número para calcular: '))
    resultado = math.atan(num)
    print(f'O resultado é {resultado}')
  elif opc == 6:
    break
  else:
    print('Opção inválida')