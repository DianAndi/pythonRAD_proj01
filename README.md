# 🔐 Gerador de Senhas com Flask

Este é um projeto de aplicação web simples, criado com [Flask](https://flask.palletsprojects.com/), para gerar senhas aleatórias com letras, 
números e caracteres especiais, salvando o histórico das senhas geradas em um banco de dados SQLite.

---

## 📸 Visual

> 💻 Interface simples, com formulário para gerar senhas e uma página de histórico.  

---

## 📚 Funcionalidades

- ✅ Geração de senhas aleatórias seguras com:
  - Letras maiúsculas e minúsculas
  - Números
  - Caracteres especiais
- ✅ Escolha do número de senhas e tamanho mínimo (mínimo de 8 caracteres)
- ✅ Salvamento automático das senhas geradas em um banco de dados SQLite
- ✅ Página para consultar o histórico completo das senhas geradas
- ✅ Interface web simples com HTML, CSS e Flask

---

## ⚙️ Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- HTML5 + CSS3

---

## 🗂️ Estrutura do Projeto

- gerador_senhas_flask/
- app.py               # Arquivo principal Flask
- senha_utils.py       # Funções de geração e banco de dados
- requirements.txt     # Dependências do projeto
- .gitignore           # Arquivos ignorados pelo Git
- templates/           # Páginas HTML
  - index.html
  - senhas.html
- static/              # Arquivos estáticos (CSS)
  - style.css


---

## 🚀 Exectando o projeto localmente  

### 1. Clone o repositório  

gitclone: https://github.com/seuusuario/gerador-senhas-flask.git  
cd gerador-senhas-flask



### 2. Crie um ambiente virtual (opcional, mas recomendado)  

python -m venv venv  
source venv/bin/activate    # Linux/Mac  
venv\Scripts\activate       # Windows  



### 3. Instale as dependências  

pip install -r requirements.txt  



### 4. Rodar o app

python app.py


---
## 🧪 Como usar
Vá para a página inicial (/)

Escolha a quantidade e o tamanho das senhas

Clique em Gerar

Veja o resultado abaixo do formulário

Histórico de senhas geradas aparecem no formulário abaixo
