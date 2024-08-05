const btnCarregar = document.getElementById('btn-carregar');
const btnCarregarMundos = document.getElementById('btn-carregar-mundos');
const btnPersonagem = document.getElementById('btn-personagem');
const inputNome = document.getElementById('Nome');
const inputMundo = document.getElementById('Mundo');
const btnDeletar = document.getElementById('btn-deletar');

const resultado = document.getElementById('resultado');

btnCarregar.addEventListener('click', carregarDados);
btnCarregarMundos.addEventListener('click', carregarMundos);
//console.log(inputNome.value);
btnPersonagem.addEventListener('click', ()=>{enviarPersonagem(inputNome.value, inputMundo.value)})
btnDeletar.addEventListener('click', deletarDataCenters)

function carregarDados() {
    //fetch('https://universalis.app/api/v2/data-centers')
    fetch('http://127.0.0.1:5000/data_centers',{method: "GET"} )
        .then(response => response.json())
        .then(dados => {
            const html = dados.map(dc => {
                return `
                    <h2>${dc.name}</h2>
                    <p>Região: ${dc.region}</p>
                    
                `;
            }).join('');
            resultado.innerHTML = html;
        })
        .catch(erro => console.error(erro));
}

function carregarMundos() {
    fetch('http://127.0.0.1:5000/worlds',{method: "GET"} )
        .then(response => response.json())
        .then(dados => {
            const html = dados.map(w => {
                return `
                    <h2>${w.WORLDname}</h2>
                    <p>Região: ${w.region}</p>
                    <p>Data Center: ${w.DCname} ID: ${w.WORLDid}</p>
                    
                    
                `;
            }).join('');
            resultado.innerHTML = html;
        })
        .catch(erro => console.error(erro));
}

function enviarPersonagem(nome, wID) {
    dados = {name: nome, WORLDid: wID}
    //console.log(dados);
    fetch('http://127.0.0.1:5000/set_characters',{method: "POST", headers:{'Content-Type': 'application/json'}, body:JSON.stringify(dados)} )
        .catch(erro => console.error(erro));
}

function deletarDataCenters(){
    fetch('http://127.0.0.1:5000/delete_DCs',{method: "DELETE"} )
        .catch(erro => console.error(erro));
}