import glob

# listar todos os arquivos em um diretório

files = glob.glob('*')
print('Arquivos do diretório atual:')
for arquivo in files:
  print(arquivo)

# listar todos os arquivos txt em um diretório

txt_files = glob.glob('.txt*')
print('Arquivos .txt do diretório atual:')
for txt in txt_files:
  print(txt)

# listar todos os diretorios em um diretório

diretorios = glob.glob('*/')
print('Diretórios em um diretório:')
for dir in diretorios:
  print(dir)