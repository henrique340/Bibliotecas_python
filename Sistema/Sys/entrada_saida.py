import sys

# stdin -> funciona para mostrar um input
for linha in sys.stdin:
  if 'q' == linha.rstrip():
    break
  print(f'input: {linha}')

print(exit)

# stdout -> mostra a saída (tipo um print)

sys.stdout.write('Geeks')

# stderr -> exceção

def print_stderr(*a):
  print(*a, file = sys.stderr)
print_stderr('Hello World')