import string

trocar = 'wy'
substituir = 'gf'
excluir = 'u'
frase_antiga = 'weeksyourweeks'

traducao = frase_antiga.maketrans(trocar, substituir, excluir)
frase_nova = frase_antiga.translate(traducao)
print('Tradução')
print(f'A frase antiga é: {frase_antiga}')
print(f'A frase nova é {frase_nova}')
print('')