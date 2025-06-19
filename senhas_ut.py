import sqlite3
import random
from datetime import datetime

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

def geraSenha(qtd, tamanho):
    especiais = ['.', '+', '-', '@', '#', '*', '!', '?', '~']
    numeros = [str(n) for n in range(10)]
    letras_min = list('abcdefghijklmnopqrstuvwxyz')
    letras_mai = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    senhas = []

    for _ in range(qtd):
        senha = []
        while len(senha) < tamanho:
            senha.append(random.choice(especiais))
            if len(senha) == tamanho: break
            senha.append(random.choice(numeros))
            if len(senha) == tamanho: break
            senha.append(random.choice(letras_mai))
            if len(senha) == tamanho: break
            senha.append(random.choice(letras_min))
        senha_final = ''.join(senha)
        senhas.append(senha_final)
        salvar_senha(senha_final)
    return senhas
