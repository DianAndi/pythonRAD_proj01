from flask import Flask, render_template, request, redirect, url_for
from senhas_ut import criar_tabela_senhas, geraSenha, consultar_senhas

app = Flask(__name__)

# Cria tabela ao iniciar o app
criar_tabela_senhas()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    qtd = int(request.form.get('quantidade', 1))
    tamanho = int(request.form.get('tamanho', 8))
    if tamanho < 8:
        tamanho = 8
    senhas = geraSenha(qtd, tamanho)
    return render_template('index.html', senhas=senhas)

@app.route('/senhas')
def historico():
    senhas = consultar_senhas()
    return render_template('senhas.html', senhas=senhas)

if __name__ == '__main__':
    app.run(debug=True)
