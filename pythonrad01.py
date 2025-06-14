import random
import sqlite3

print('=================================\n||      Gerador de Senhas      ||\n=================================')

#bco de dados aqui
def criar_tabela_senhas():
    conn = sqlite3.connect('senhas_geradas.db') 
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            senha TEXT NOT NULL,
            data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def salvar_senha(senha):
    conn = sqlite3.connect('senhas_geradas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO senhas (senha) VALUES (?)", (senha,))
    conn.commit()
    conn.close()

def consultar_senhas():
    conn = sqlite3.connect('senhas_geradas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, senha, data_geracao FROM senhas ORDER BY data_geracao DESC")
    senhas = cursor.fetchall()
    conn.close()
    return senhas

criar_tabela_senhas()

num_senhas = int(input("Número de senhas: ") or 1)
tamanho_senha = 0

#aqui definir tamanho de senhas (8 caracteres)

while tamanho_senha < 8:
    tamanho_senha = int(input("Total de dígitos na senha: ") or "8")
    if tamanho_senha < 8:
        print('O mínimo de caracteres é 8.')

#aqui os caracteres que podem ser usados

especiais = [ '.', '+', '-', '@', '#', '*', '!', '?', '~']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#código função p gerar senhas

def geraSenha(a_senha, b_senha):
    senhas = []
    i = 1

    while i <= a_senha:
        senha = []


        while len(senha) < b_senha:
            senha.append(random.choice(especiais))
            if len(senha) == b_senha:
                 break
            senha.append(random.choice(numeros))
            if len(senha) == b_senha:
                break    
            senha.append(random.choice(letras_mai))
            if len(senha) == b_senha:
                break    
            senha.append(random.choice(letras_min))
            if len(senha) == b_senha:
                 break    
        senhas.append(senha)
        i = i + 1
    return senhas   
senhas_geradas = geraSenha(num_senhas, tamanho_senha)  

#aqui imprime as senhas

j = 1
for senha in senhas_geradas:
    password = ''.join(senha)
    print(f'senha{j}:{password} \n')


print('=================================\n')

