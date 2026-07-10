# Projeto 1 - Vetores

Projeto desenvolvido para a disciplina **Fisica para Ciencia da Computacao**.

## Repositorio

O codigo deste projeto esta disponivel no GitHub em:

**https://github.com/arthur-engsoftware/projetodefisicaempython**

Para baixar o projeto na sua maquina:

```bash
git clone https://github.com/arthur-engsoftware/projetodefisicaempython.git
cd projetodefisicaempython
```

## Objetivo

O programa permite:

- Converter unidades de medida (comprimento, massa, tempo, velocidade, temperatura, energia e forca);
- Criar vetores de 2 dimensoes (2D) e 3 dimensoes (3D);
- Realizar operacoes com vetores: soma, subtracao, multiplicacao por escalar, produto escalar e produto vetorial;
- Visualizar os vetores e as operacoes em graficos, usando setas desenhadas no plano (2D) ou no espaco (3D).

Todo o codigo foi escrito usando apenas **funcoes** (sem classes, sem lambda, sem decorators), para praticar logica de programacao em Python.

## Bibliotecas utilizadas

- [NumPy](https://numpy.org/) — usada para representar os vetores e fazer os calculos (soma, produto escalar, produto vetorial, etc).
- [Matplotlib](https://matplotlib.org/) — usada para desenhar os vetores em graficos 2D e 3D.

## Como instalar as bibliotecas

Este projeto tem um arquivo `requirements.txt` com as bibliotecas necessarias. Assim, em vez de instalar uma por uma, basta rodar um unico comando.

Voce pode instalar as bibliotecas **direto no sistema** (mais simples) ou dentro de um **ambiente virtual (venv)** (mais organizado, recomendado se voce mexe com varios projetos Python). As duas formas estao explicadas abaixo.

### Opcao 1 - Instalar direto no sistema (mais simples)

**Windows**

Abra o Prompt de Comando (cmd) ou o PowerShell, entre na pasta do projeto e digite:

```
pip install -r requirements.txt
```

**Linux**

Abra o terminal, entre na pasta do projeto e digite:

```
pip3 install -r requirements.txt
```

Caso o `pip3` nao esteja instalado, use antes:

```
sudo apt update
sudo apt install python3-pip
```

Em versoes mais novas do Ubuntu, o sistema pode bloquear a instalacao com o erro `externally-managed-environment`. Se isso acontecer, use:

```
pip3 install -r requirements.txt --break-system-packages
```

### Opcao 2 - Instalar dentro de um venv (ambiente virtual)

Um **venv** e uma "caixa" isolada com sua propria copia do Python e das bibliotecas, separada do resto do sistema. Isso evita que as bibliotecas de um projeto entrem em conflito com as de outro.

**1. Criar o venv** (so precisa fazer isso uma vez, dentro da pasta do projeto):

```
python3 -m venv venv
```

Isso cria uma pasta chamada `venv` com uma copia do Python dentro.

**2. Ativar o venv** (precisa fazer isso toda vez que abrir um terminal novo):

```
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate          # Windows
```

Quando o venv estiver ativo, o prompt do terminal passa a mostrar `(venv)` no comeco da linha. Isso confirma que esta usando o Python de dentro da caixinha, e nao o do sistema.

**3. Instalar as bibliotecas dentro do venv:**

```
pip install -r requirements.txt
```

**4. Rodar o programa normalmente:**

```
python3 projeto_vetores.py
```

**5. Quando terminar de usar, para sair do venv:**

```
deactivate
```

Se fechar o terminal e abrir de novo mais tarde, lembre-se de ativar o venv de novo (passo 2) antes de rodar o programa, ou o Python nao vai encontrar o numpy e o matplotlib instalados nele.

## Como executar

### Windows

```
python projeto_vetores.py
```

ou, dependendo de como o Python foi instalado:

```
python3 projeto_vetores.py
```

### Linux

```
python3 projeto_vetores.py
```

O programa e todo baseado em um menu de texto no terminal, que fica em execucao ate o usuario escolher a opcao `0 - Sair`.

## Funcionalidades do menu

O programa agora tem dois niveis de menu: o menu principal e o submenu de vetores.

```
==============================
PROJETO 1 - VETORES
==============================
1 - Conversao de unidades
2 - Vetores
0 - Sair
```

Ao escolher a opcao `2 - Vetores`, abre o submenu:

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

Escolhendo `0` no submenu de vetores, o programa volta para o menu principal (sem fechar o programa).

### 1 - Conversao de unidades

Abre um submenu com sete categorias: Comprimento, Massa, Tempo, Velocidade, Temperatura, Energia e Forca. O usuario escolhe a unidade de origem, a unidade de destino e digita o valor a ser convertido.

Unidades de comprimento suportadas: mm, cm, dm, m, dam, hm, km, polegada, pe, jarda, milha.

Unidades de massa: mg, g, kg, tonelada, libra.

Unidades de tempo: ms, s, min, h, dia.

Unidades de velocidade: m/s, km/h, mph.

Unidades de temperatura: Celsius, Fahrenheit, Kelvin.

Unidades de energia: J, kJ, cal.

Unidades de forca: N, kN.

### 2 e 3 - Criar vetor 2D / 3D

Pede as coordenadas do vetor (X, Y ou X, Y, Z) e mostra o vetor criado na tela.

### 4 a 8 - Operacoes com vetores

Cada operacao pergunta se o vetor e 2D ou 3D (exceto o produto vetorial, que so existe em 3D), pede os vetores necessarios e mostra o resultado do calculo.

### 9 - Visualizar vetor

Pede um vetor (2D ou 3D) e desenha uma seta representando esse vetor, com eixos, grade, titulo e legenda.

### 10 - Visualizar operacao

Desenha a ultima operacao feita (soma, subtracao, multiplicacao por escalar ou produto vetorial), mostrando o(s) vetor(es) original(is) e o resultado, cada um com uma cor diferente. Se nenhuma operacao tiver sido feita ainda, o programa avisa o usuario.

Obs: o produto escalar nao pode ser visualizado, pois o resultado dele e um numero, e nao um vetor.

## Tratamento de erros

O programa nao fecha quando o usuario digita algo errado. Sempre que uma entrada invalida e digitada (por exemplo, uma letra no lugar de um numero, ou uma opcao que nao existe no menu), o programa mostra uma mensagem de erro e pede a informacao novamente.

## Exemplo de uso

```
Escolha uma opcao: 2   (entra no menu de Vetores)

------------------------------
MENU DE VETORES
------------------------------
Escolha uma opcao: 1

--- Criando vetor 2D ---
Digite X: 3
Digite Y: 4
Vetor criado: (3.0, 4.0)
Vetor 2D criado com sucesso: [3. 4.]
```

```
Escolha uma opcao: 3   (Somar vetores, dentro do menu de Vetores)

--- SOMA DE VETORES ---

Escolha a dimensao do vetor:
1 - 2D
2 - 3D
Opcao: 1

Vetor A:
Digite X: 1
Digite Y: 2

Vetor B:
Digite X: 3
Digite Y: 4

A + B = [4. 6.]
```

Depois de fazer uma operacao, basta escolher a opcao `9 - Visualizar operacao` no submenu de vetores para ver o grafico com os vetores usados e o resultado.

## Visual dos graficos

Os graficos foram estilizados para ficar mais faceis de ler:

- Cada vetor tem uma cor fixa (vermelho para o Vetor A, verde-agua para o Vetor B, azul para o Resultado);
- As coordenadas de cada vetor aparecem escritas perto da ponta da seta;
- O fundo do grafico e da figura usa tons claros para destacar as setas;
- Titulo em negrito e legenda com caixa, para facilitar a identificacao de cada vetor.
