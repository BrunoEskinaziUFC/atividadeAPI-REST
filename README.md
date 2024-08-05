# atividadeAPI-REST
Repositório da atividade de API REST da disciplina de Sistemas Distribuídos no curso de Sistemas e Mídias Digitais da UFC.

A primeira parte desta atividade consiste em criar um cliente que acesse uma API remota de uma calculadora (disponível em: https://calculadora-fxpc.onrender.com/operations), sendo capaz de executar os comandos POST de soma, subtação, multiplicação e divisão acessíveis na API. Nossa equipe criou um cliente python que acessa a API e printa no console as operações disponíveis, em seguida, executa todas essas em sequência.

Na segunda parte, foi feita uma pequena aplicação web que utiliza uma API REST para armazenar dados sobre o MMORPG Final Fantasy XIV: Online. Os dados são recolhidos de uma API externa, chamada Universalis (disponível em: https://docs.universalis.app/), que contém dados diversos sobre o MMORPG, como nomes dos data centers e seus servidores associados. Nossa API armazena em um banco de dados local alguns dados do Universalis para fazer consultas GET, POST e DELETE em um cliente web.

A aplicação possui 4 consultas CRUD as quais são:
1) Listagem de todos os Data Centers do jogo, puxando da API Universalis e registrando no banco de dados
2) Listagem de todos os mundos(servidores) do jogo e seus respectivos Data Centers, puxando da API Universalis e registrando no banco de dados
3) Registração de um personagem, dado seu nome único e um mundo a sua escolha
4) Deleção de todos os Data Centers armazenados no banco de dados.

Membros:
-Bruno Eskinazi (473967)
-Eduarda Tavares (472432)
-Pedro Henrique (508892)
