import math

while True:
  print('Conversor de angulos')
  print('''[1] Para converter radianos para graus
[2] Para converter graus para radiano
[3] Para sair
''')

  opc = int(input('Digite a sua opção: '))
  if opc == 1:
    num = float(input('Digite o número do ângulo em radianos: '))
    resultado = math.degrees(num)
    print(f'O valor do ângulo em graus é: {resultado:.2f}')
  elif opc == 2:
    num = float(input('Digite o número do ângulo: '))
    resultado = math.radians(num)
    print(f'O valor do ângulo em radianos é: {resultado:.2f}')
  elif opc == 3:
    break
  else:
    print('Digite uma opção válida')