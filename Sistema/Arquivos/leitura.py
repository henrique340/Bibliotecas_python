import sys
import os.path

fn = input('Nome do arquivo: ').strip()

if not os.path.exists(fn):
  print('Tente novamente outra vez')
  sys.exit()

for i, s in enumerate(fn):

  print(i + 1, s, end='')
  