import time

time_stamp = time.time()
print(f'O time stamp atual é de {time_stamp}')

tempo_atual = time.localtime()
print(tempo_atual)

tempo_formatado = time.localtime(time_stamp)
print(f'O tempo formatado é {tempo_formatado}')

tempo_formatado_string = time.strftime('%Y-%m-%d %H-%M:%S', tempo_atual)
print(f'\nTempo formatado com string: {tempo_formatado_string}\n')

time.sleep(2)