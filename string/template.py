import string

# criando uma string template 

frase_antiga = string.Template('$aviso aconteceu em $quando')

# preenchendo com um dicionário 

substituicao = frase_antiga.substitute({'aviso':'falta de luz', 'quando':'03 de Abril de 2002'})

print('A frase antiga é: $aviso aconteceu em $quando')
print(f'A nova frase é: {substituicao}')