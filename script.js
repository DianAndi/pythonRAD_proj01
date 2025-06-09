/* script.js */
document.addEventListener('DOMContentLoaded', () => {
const numSenhasInput = document.getElementById('num_senhas');
const tamanhoSenhaInput = document.getElementById('tamanho_senha');
const gerarSenhasBotao = document.getElementById('gerar_senhas');
const senhasGeradasLista = document.getElementById('senhas_geradas_lista');

const especiais = ['.', '+', '-', '@', '#', '*', '!', '?', '~'];
const numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
const letrasMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const letrasMai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
const todosCaracteres = especiais.concat(numeros, letrasMin, letrasMai);

function gerarSenha(tamanho) {
    let senha = [];
    for (let i = 0; i < tamanho; i++) {
        senha.push(todosCaracteres[(Math.floor(Math.random() * todosCaracteres.length))]);
    }
    return senha.join('');
}

gerarSenhasBotao.addEventListener('click', () => {
    const numSenhas = parseInt(numSenhasInput.value) || 1;
    const tamanhoSenha = parseInt(tamanhoSenhaInput.value) || 8;

    if (tamanhoSenha < 8) {
        alert('O tamanho mínimo da senha é 8 caracteres.');
        return;
    }

    senhasGeradasLista.innerHTML = ''; // Limpa a lista anterior

    for (let i = 0; i < numSenhas; i++) {
        const senha = gerarSenha(tamanhoSenha);
        const listItem = document.createElement('li');
        listItem.textContent = senha;
        senhasGeradasLista.appendChild(listItem);
    }
});