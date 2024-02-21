import os 
os_name = os.name
print(f'Sistema operacional: {os_name}')

username = os.environ.get('USERNAME')
print(f'Nome do usuário: {username}')