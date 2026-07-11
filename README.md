# Projeto 1 - Vetores

Projeto da disciplina **Fisica para Ciencia da Computacao**.

Repositorio: https://github.com/arthur-engsoftware/projetodefisicaempython

---

## Como executar (Linux) — jeito mais facil

Abra o terminal dentro da pasta do projeto e rode:

```bash
chmod +x executar.sh
./executar.sh
```

Pronto. Esse script confere se falta alguma biblioteca, instala automaticamente se precisar, e já abre o programa.

## Como executar (Windows)

```
pip install -r requirements.txt
python projeto_vetores.py
```

---

## Se preferir instalar manualmente (sem o script)

```bash
pip3 install -r requirements.txt
python3 projeto_vetores.py
```

Se aparecer o erro `externally-managed-environment`, use:

```bash
pip3 install -r requirements.txt --break-system-packages
```

---

## O que o programa faz

- Converte unidades de medida (comprimento, massa, tempo, velocidade, temperatura, energia, forca)
- Cria vetores 2D e 3D
- Faz operacoes com vetores: soma, subtracao, multiplicacao por escalar, produto escalar, produto vetorial
- Desenha os vetores e os resultados em graficos (Matplotlib)

O codigo usa apenas **funcoes** (sem classes), pensado para nivel de aluno iniciante em Python.

## Menu do programa

```
==============================
PROJETO 1 - VETORES
==============================
1 - Conversao de unidades
2 - Vetores
0 - Sair
```

A opcao `2 - Vetores` abre um segundo menu:

```
------------------------------
MENU DE VETORES
------------------------------
1 - Criar vetor 2D
2 - Criar vetor 3D
3 - Somar vetores
4 - Subtrair vetores
5 - Multiplicar vetor por escalar
6 - Produto escalar
7 - Produto vetorial
8 - Visualizar vetor
9 - Visualizar operacao
0 - Voltar ao menu principal
```

Cada grafico abre em uma janela separada. Para o programa continuar, **feche a janela do grafico** e o menu volta a aparecer no terminal.

## Exemplo rapido

```
Escolha uma opcao: 2       (entra no menu de Vetores)
Escolha uma opcao: 3       (Somar vetores)
Escolha a dimensao: 1      (2D)

Vetor A -> Digite X: 1   Digite Y: 2
Vetor B -> Digite X: 3   Digite Y: 4

A + B = [4. 6.]
```

Depois é só escolher `9 - Visualizar operacao` para ver o grafico da soma.

## Tratamento de erros

O programa nunca fecha sozinho por causa de entrada errada (letra no lugar de numero, opcao que nao existe). Ele mostra uma mensagem e pede de novo.

---

## Ambiente virtual (venv) — opcional

Nao e necessario para rodar o projeto. Um venv e uma "caixa" isolada com copia propria do Python, usada quando se quer separar as bibliotecas de projetos diferentes. Se quiser usar:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 projeto_vetores.py
deactivate   # para sair do venv quando terminar
```
