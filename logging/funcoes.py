import logging
import math

# Configuração básica do sistema de log
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Criando um objeto logger com um nome específico
logger = logging.getLogger('raiz_quadrada')
logger.setLevel(logging.DEBUG)  # Definindo o nível de log para DEBUG

# Criando um handler para escrever logs em um arquivo
handler = logging.FileHandler('raiz_quadrada.log')
handler.setLevel(logging.DEBUG)  # Definindo o nível de log para DEBUG

# Criando um formatador de log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)  # Definindo o formatador para o handler

# Adicionando o handler ao logger
logger.addHandler(handler)

def calcular_raiz_quadrada(numero):
    try:
        resultado = math.sqrt(numero)
        logger.info(f"A raiz quadrada de {numero} é {resultado}")
        return resultado
    except ValueError:
        logger.error(f"Erro ao calcular a raiz quadrada de {numero}: Valor negativo")
        return None

def main():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    resultado = calcular_raiz_quadrada(numero)
    if resultado is not None:
        print(f"A raiz quadrada de {numero} é {resultado}")
    else:
        print("Erro: Valor negativo inserido. Verifique o arquivo de log para mais informações.")

if __name__ == "__main__":
    main()

