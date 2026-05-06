Projeto: Estruturas Lineares em Python

Desafio 1: Sistema de Votação

Problema: Simular uma votação entre três candidatos (Ana, Bruno e Carlos), registrando os votos até que o usuário digite "fim".

Funcionalidades:

Armazenamento de votos em listas
Validação de candidatos
Contagem de votos com "count()"
Identificação de vencedor ou empate
Estruturas utilizadas: Lista

Como executar: python desafio01_votacao.py

Exemplo de entrada: Entrada: Ana Bruno Ana fim

Saída: Ana: 2 votos Bruno: 1 voto Carlos: 0 votos Vencedor: Ana

Desafio 2: Editor com Desfazer(Pilha)

Problema: Simular um editor de texto simples que permite adicionar palavras e desfazer a última ação realizada.

Funcionalidades:

Inserção de palavras com "append()"
Remoção da última palavra com "pop()"
Exibição dp texto atual
Tratamento de pilha vazia
Menu interativo com "match-case"
Estrutura utilizada: Pilha(LIFO - Last In, Firts Out)

Como executar: python desafio02_editor_pilha.py

Exemplo: Digite: Olá Digite: mundo Desfazer: 2

Texto atual: Olá

Desafio 3: Fila de Atendimento

Problema: Simular uma fila de atendimento em uma secretaria respeitando a ordem de chegada.

Funcionalidades:

Entrada de alunos na fila com "append()"
Atendimento com "pop(0)"
Exibição da fila com posição (ordem de atendimento)
Tratamentp de fila vazia
Menu interativo com "match-case"
Estrutura utilizada: Fila (FIFO - First In, First Out)

Como executar: python desafio03_fila_atend.py

Exemplo: Entrada: Marco - entra na fila Ana - entra na fila

Saída: Fila atual: 1° - Marco 2° - Ana

Atendendo: Marco

Para que os exercícios 2 e 3 rodem, é necessário obter o Python 3.10
