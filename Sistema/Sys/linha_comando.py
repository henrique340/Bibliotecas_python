import sys

qnt_argumentos = len(sys.argv)
print(f'O total de argumentos são: {qnt_argumentos}')

print(f'O nome do script Python é: {sys.argv[0]}')

print('Argumentos passados:', end='')
for i in range(1, qnt_argumentos):
  print(sys.argv[i], end='')

soma = 0
for i in range(1, qnt_argumentos):
  soma += int(sys.argv[i])
print(f'\nResultado: {soma}')