import threading

# Definição e inicialização de uma nova thread
def minha_funcao():
    print("Thread secundária iniciada")

thread = threading.Thread(target=minha_funcao)
thread.start()  # Inicia a thread
thread.join()   # Aguarda a thread terminar

# Verificação do número de threads ativas
numero_threads = threading.active_count()
print("Número de threads ativas:", numero_threads)

# Obtenção da lista de todas as threads ativas
threads_ativas = threading.enumerate()
print("Threads ativas:", threads_ativas)

# Obtendo e definindo o nome da thread atual
thread_atual = threading.current_thread()
print("Nome da thread atual:", thread_atual.name)
thread_atual.name = "MinhaThread"
print("Novo nome da thread atual:", thread_atual.name)

# Verificando se uma thread está viva
thread_viva = thread_atual.is_alive()
print("A thread atual está viva?", thread_viva)

# Aguardando a finalização de uma thread
thread.join()

# Definição de uma função para execução em uma thread
def imprimir_numero(numero):
    print("Número:", numero)

# Criando e iniciando várias threads
for i in range(5):
    t = threading.Thread(target=imprimir_numero, args=(i,))
    t.start()

# Criando uma classe de thread personalizada
class MinhaThread(threading.Thread):
    def run(self):
        print("Thread personalizada iniciada")

# Iniciando uma instância da classe de thread personalizada
minha_thread = MinhaThread()
minha_thread.start()
minha_thread.join()
