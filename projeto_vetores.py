#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PROJETO 1 - VETORES
# Fisica para Ciencia da Computacao
# roda com: python3 projeto_vetores.py

import sys

# se numpy/matplotlib nao estiver instalado, mostra um aviso mais
# facil de entender em vez do traceback gigante do python
try:
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # precisa disso pro grafico 3D
except ModuleNotFoundError as erro:
    print("=" * 60)
    print("ERRO: uma biblioteca necessaria nao esta instalada.")
    print(f"Detalhe: {erro}")
    print()
    print("Para corrigir, rode este comando no terminal, dentro da")
    print("pasta do projeto, e depois execute o programa novamente:")
    print()
    print("    pip3 install -r requirements.txt")
    print()
    print("Se aparecer erro dizendo 'externally-managed-environment',")
    print("rode este comando em vez do de cima:")
    print()
    print("    pip3 install -r requirements.txt --break-system-packages")
    print("=" * 60)
    sys.exit(1)


# guarda a ultima operacao feita, pra opcao "visualizar operacao" saber
# o que desenhar depois sem o usuario ter que digitar tudo de novo
ultima_operacao_tipo = None
ultima_operacao_dimensao = None
ultimo_vetor_a = None
ultimo_vetor_b = None
ultimo_resultado = None
ultimo_escalar = None


def ler_numero(mensagem):
    # aceita tanto ponto quanto virgula, tipo 3.5 ou 3,5
    while True:
        entrada = input(mensagem)
        entrada = entrada.strip().replace(",", ".")
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Erro: digite apenas numeros. Tente novamente.\n")


def ler_opcao_inteira(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem)
        entrada = entrada.strip()
        if entrada.isdigit():
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
        print(f"Erro: digite um numero inteiro entre {minimo} e {maximo}.\n")


def ler_vetor_2d():
    print("\n--- Criando vetor 2D ---")
    x = ler_numero("Digite X: ")
    y = ler_numero("Digite Y: ")
    vetor = np.array([x, y])
    print(f"Vetor criado: ({x}, {y})\n")
    return vetor


def ler_vetor_3d():
    print("\n--- Criando vetor 3D ---")
    x = ler_numero("Digite X: ")
    y = ler_numero("Digite Y: ")
    z = ler_numero("Digite Z: ")
    vetor = np.array([x, y, z])
    print(f"Vetor criado: ({x}, {y}, {z})\n")
    return vetor


def escolher_dimensao():
    print("\nEscolha a dimensao do vetor:")
    print("1 - 2D")
    print("2 - 3D")
    opcao = ler_opcao_inteira("Opcao: ", 1, 2)
    if opcao == 1:
        return "2D"
    return "3D"


def somar_vetores(vetor_a, vetor_b):
    return vetor_a + vetor_b


def subtrair_vetores(vetor_a, vetor_b):
    return vetor_a - vetor_b


def multiplicar_escalar(vetor, escalar):
    return vetor * escalar


def produto_escalar(vetor_a, vetor_b):
    return np.dot(vetor_a, vetor_b)


def produto_vetorial(vetor_a, vetor_b):
    # so faz sentido pra vetor 3D
    return np.cross(vetor_a, vetor_b)


# cores usadas nos graficos, pra ficar sempre igual
COR_A = "#e63946"
COR_B = "#2a9d8f"
COR_RESULTADO = "#264ede"
COR_UNICO = "#3a86ff"
COR_FUNDO_FIGURA = "#f7f7fb"
COR_FUNDO_EIXO = "#ffffff"


def calcular_limite(*vetores):
    # pega o maior valor entre os vetores pra escala do grafico nao
    # cortar a seta nem ficar com o desenho muito pequeno
    maior_valor = 1.0
    for vetor in vetores:
        maior_componente = np.max(np.abs(vetor))
        if maior_componente > maior_valor:
            maior_valor = maior_componente
    return maior_valor * 1.3


def estilizar_eixo_2d(eixo, titulo):
    eixo.axhline(0, color="#333333", linewidth=1.2, zorder=1)
    eixo.axvline(0, color="#333333", linewidth=1.2, zorder=1)
    eixo.grid(True, linestyle="--", alpha=0.4, color="#999999")
    eixo.set_facecolor(COR_FUNDO_EIXO)
    eixo.set_xlabel("Eixo X", fontsize=11)
    eixo.set_ylabel("Eixo Y", fontsize=11)
    eixo.set_title(titulo, fontsize=14, fontweight="bold", color="#1d3557", pad=14)
    eixo.set_aspect("equal")
    eixo.legend(frameon=True, fontsize=10, loc="upper left")


def estilizar_eixo_3d(eixo, titulo):
    eixo.set_xlabel("Eixo X", fontsize=11)
    eixo.set_ylabel("Eixo Y", fontsize=11)
    eixo.set_zlabel("Eixo Z", fontsize=11)
    eixo.set_title(titulo, fontsize=14, fontweight="bold", color="#1d3557", pad=14)
    eixo.legend(frameon=True, fontsize=10)
    # fundo mais claro nos paineis do grafico 3D
    eixo.xaxis.pane.set_facecolor("#f0f0f5")
    eixo.yaxis.pane.set_facecolor("#f0f0f5")
    eixo.zaxis.pane.set_facecolor("#f0f0f5")
    eixo.grid(True, linestyle="--", alpha=0.3)


def desenhar_seta_2d(eixo, vetor, cor, rotulo):
    eixo.quiver(0, 0, vetor[0], vetor[1], angles="xy", scale_units="xy",
                scale=1, color=cor, label=rotulo, width=0.012,
                headwidth=4, headlength=5, zorder=3)

    texto = f"({vetor[0]:.1f}, {vetor[1]:.1f})"
    eixo.annotate(texto, xy=(vetor[0], vetor[1]), xytext=(6, 6),
                  textcoords="offset points", fontsize=9, color=cor,
                  fontweight="bold")


def desenhar_seta_3d(eixo, vetor, cor, rotulo):
    eixo.quiver(0, 0, 0, vetor[0], vetor[1], vetor[2], color=cor,
                label=rotulo, linewidth=2.5, arrow_length_ratio=0.15)

    texto = f"({vetor[0]:.1f}, {vetor[1]:.1f}, {vetor[2]:.1f})"
    eixo.text(vetor[0], vetor[1], vetor[2], texto, fontsize=9, color=cor,
              fontweight="bold")


def plotar_vetor_2d(vetor, titulo="Vetor 2D"):
    limite = calcular_limite(vetor)

    figura, eixo = plt.subplots(figsize=(6, 6))
    figura.patch.set_facecolor(COR_FUNDO_FIGURA)

    rotulo = f"Vetor ({vetor[0]:.1f}, {vetor[1]:.1f})"
    desenhar_seta_2d(eixo, vetor, COR_UNICO, rotulo)

    eixo.set_xlim(-limite, limite)
    eixo.set_ylim(-limite, limite)
    estilizar_eixo_2d(eixo, titulo)

    plt.tight_layout()
    plt.show()


def plotar_vetor_3d(vetor, titulo="Vetor 3D"):
    limite = calcular_limite(vetor)

    figura = plt.figure(figsize=(7, 7))
    figura.patch.set_facecolor(COR_FUNDO_FIGURA)
    eixo = figura.add_subplot(111, projection="3d")

    rotulo = f"Vetor ({vetor[0]:.1f}, {vetor[1]:.1f}, {vetor[2]:.1f})"
    desenhar_seta_3d(eixo, vetor, COR_UNICO, rotulo)

    eixo.set_xlim([-limite, limite])
    eixo.set_ylim([-limite, limite])
    eixo.set_zlim([-limite, limite])
    estilizar_eixo_3d(eixo, titulo)

    plt.tight_layout()
    plt.show()


def plotar_operacao_2d(vetor_a, vetor_b, resultado, titulo, rotulo_a="Vetor A",
                        rotulo_b="Vetor B", rotulo_resultado="Resultado"):
    limite = calcular_limite(vetor_a, vetor_b, resultado)

    figura, eixo = plt.subplots(figsize=(6.5, 6.5))
    figura.patch.set_facecolor(COR_FUNDO_FIGURA)

    desenhar_seta_2d(eixo, vetor_a, COR_A, rotulo_a)
    desenhar_seta_2d(eixo, vetor_b, COR_B, rotulo_b)
    desenhar_seta_2d(eixo, resultado, COR_RESULTADO, rotulo_resultado)

    eixo.set_xlim(-limite, limite)
    eixo.set_ylim(-limite, limite)
    estilizar_eixo_2d(eixo, titulo)

    plt.tight_layout()
    plt.show()


def plotar_operacao_3d(vetor_a, vetor_b, resultado, titulo, rotulo_a="Vetor A",
                        rotulo_b="Vetor B", rotulo_resultado="Resultado"):
    limite = calcular_limite(vetor_a, vetor_b, resultado)

    figura = plt.figure(figsize=(7.5, 7.5))
    figura.patch.set_facecolor(COR_FUNDO_FIGURA)
    eixo = figura.add_subplot(111, projection="3d")

    desenhar_seta_3d(eixo, vetor_a, COR_A, rotulo_a)
    desenhar_seta_3d(eixo, vetor_b, COR_B, rotulo_b)
    desenhar_seta_3d(eixo, resultado, COR_RESULTADO, rotulo_resultado)

    eixo.set_xlim([-limite, limite])
    eixo.set_ylim([-limite, limite])
    eixo.set_zlim([-limite, limite])
    estilizar_eixo_3d(eixo, titulo)

    plt.tight_layout()
    plt.show()


def plotar_operacao_um_vetor_2d(vetor_original, vetor_novo, titulo):
    # usado so na multiplicacao por escalar, que tem 2 vetores e nao 3
    limite = calcular_limite(vetor_original, vetor_novo)

    figura, eixo = plt.subplots(figsize=(6, 6))
    figura.patch.set_facecolor(COR_FUNDO_FIGURA)

    desenhar_seta_2d(eixo, vetor_original, COR_A, "Vetor original")
    desenhar_seta_2d(eixo, vetor_novo, COR_RESULTADO, "Vetor multiplicado")

    eixo.set_xlim(-limite, limite)
    eixo.set_ylim(-limite, limite)
    estilizar_eixo_2d(eixo, titulo)

    plt.tight_layout()
    plt.show()


def plotar_operacao_um_vetor_3d(vetor_original, vetor_novo, titulo):
    limite = calcular_limite(vetor_original, vetor_novo)

    figura = plt.figure(figsize=(7, 7))
    figura.patch.set_facecolor(COR_FUNDO_FIGURA)
    eixo = figura.add_subplot(111, projection="3d")

    desenhar_seta_3d(eixo, vetor_original, COR_A, "Vetor original")
    desenhar_seta_3d(eixo, vetor_novo, COR_RESULTADO, "Vetor multiplicado")

    eixo.set_xlim([-limite, limite])
    eixo.set_ylim([-limite, limite])
    eixo.set_zlim([-limite, limite])
    estilizar_eixo_3d(eixo, titulo)

    plt.tight_layout()
    plt.show()


def mostrar_opcoes(nomes_unidades):
    for indice, nome in enumerate(nomes_unidades, start=1):
        print(f"{indice} - {nome}")


def escolher_unidade(nomes_unidades):
    mostrar_opcoes(nomes_unidades)
    opcao = ler_opcao_inteira("Escolha a unidade: ", 1, len(nomes_unidades))
    return nomes_unidades[opcao - 1]


def converter_com_fatores(fatores):
    # fatores = dicionario com quantas unidades "base" equivalem a 1
    # unidade daquele tipo (ex: 1 km = 1000 m, entao km:1000)
    nomes_unidades = list(fatores.keys())

    print("\nUnidade de origem:")
    unidade_origem = escolher_unidade(nomes_unidades)

    print("\nUnidade de destino:")
    unidade_destino = escolher_unidade(nomes_unidades)

    valor = ler_numero(f"\nDigite o valor em {unidade_origem}: ")

    valor_em_base = valor * fatores[unidade_origem]
    valor_convertido = valor_em_base / fatores[unidade_destino]

    print(f"\nResultado: {valor} {unidade_origem} = {valor_convertido:.6f} {unidade_destino}\n")


def converter_comprimento():
    fatores = {
        "mm": 0.001,
        "cm": 0.01,
        "dm": 0.1,
        "m": 1.0,
        "dam": 10.0,
        "hm": 100.0,
        "km": 1000.0,
        "polegada": 0.0254,
        "pe": 0.3048,
        "jarda": 0.9144,
        "milha": 1609.344,
    }
    converter_com_fatores(fatores)


def converter_massa():
    fatores = {
        "mg": 1e-6,
        "g": 1e-3,
        "kg": 1.0,
        "tonelada": 1000.0,
        "libra": 0.45359237,
    }
    converter_com_fatores(fatores)


def converter_tempo():
    fatores = {
        "ms": 0.001,
        "s": 1.0,
        "min": 60.0,
        "h": 3600.0,
        "dia": 86400.0,
    }
    converter_com_fatores(fatores)


def converter_velocidade():
    fatores = {
        "m/s": 1.0,
        "km/h": 1.0 / 3.6,
        "mph": 0.44704,
    }
    converter_com_fatores(fatores)


def converter_energia():
    fatores = {
        "J": 1.0,
        "kJ": 1000.0,
        "cal": 4.184,
    }
    converter_com_fatores(fatores)


def converter_forca():
    fatores = {
        "N": 1.0,
        "kN": 1000.0,
    }
    converter_com_fatores(fatores)


def converter_temperatura():
    # temperatura nao da pra converter so multiplicando por um fator
    # (a escala nao comeca do zero igual as outras), entao faz na mao
    unidades = ["Celsius", "Fahrenheit", "Kelvin"]

    print("\nUnidade de origem:")
    origem = escolher_unidade(unidades)
    print("\nUnidade de destino:")
    destino = escolher_unidade(unidades)

    valor = ler_numero(f"\nDigite o valor em {origem}: ")

    # passa tudo pra Celsius primeiro
    if origem == "Celsius":
        celsius = valor
    elif origem == "Fahrenheit":
        celsius = (valor - 32) * 5.0 / 9.0
    else:
        celsius = valor - 273.15

    # dai converte de Celsius pra unidade final
    if destino == "Celsius":
        resultado = celsius
    elif destino == "Fahrenheit":
        resultado = celsius * 9.0 / 5.0 + 32
    else:
        resultado = celsius + 273.15

    print(f"\nResultado: {valor} {origem} = {resultado:.4f} {destino}\n")


def converter_unidades():
    print("\n==============================")
    print("CONVERSAO DE UNIDADES")
    print("==============================")
    print("1 - Comprimento")
    print("2 - Massa")
    print("3 - Tempo")
    print("4 - Velocidade")
    print("5 - Temperatura")
    print("6 - Energia")
    print("7 - Forca")

    opcao = ler_opcao_inteira("Escolha a categoria: ", 1, 7)

    if opcao == 1:
        converter_comprimento()
    elif opcao == 2:
        converter_massa()
    elif opcao == 3:
        converter_tempo()
    elif opcao == 4:
        converter_velocidade()
    elif opcao == 5:
        converter_temperatura()
    elif opcao == 6:
        converter_energia()
    elif opcao == 7:
        converter_forca()


def opcao_criar_vetor_2d():
    vetor = ler_vetor_2d()
    print(f"Vetor 2D criado com sucesso: {vetor}\n")


def opcao_criar_vetor_3d():
    vetor = ler_vetor_3d()
    print(f"Vetor 3D criado com sucesso: {vetor}\n")


def registrar_operacao(tipo, dimensao, vetor_a, vetor_b, resultado, escalar=None):
    # salva a ultima operacao pra opcao "visualizar operacao" usar depois
    global ultima_operacao_tipo, ultima_operacao_dimensao
    global ultimo_vetor_a, ultimo_vetor_b, ultimo_resultado, ultimo_escalar

    ultima_operacao_tipo = tipo
    ultima_operacao_dimensao = dimensao
    ultimo_vetor_a = vetor_a
    ultimo_vetor_b = vetor_b
    ultimo_resultado = resultado
    ultimo_escalar = escalar


def opcao_somar_vetores():
    print("\n--- SOMA DE VETORES ---")
    dimensao = escolher_dimensao()

    print("\nVetor A:")
    vetor_a = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    print("Vetor B:")
    vetor_b = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    resultado = somar_vetores(vetor_a, vetor_b)
    print(f"\nA + B = {resultado}\n")

    registrar_operacao("soma", dimensao, vetor_a, vetor_b, resultado)


def opcao_subtrair_vetores():
    print("\n--- SUBTRACAO DE VETORES ---")
    dimensao = escolher_dimensao()

    print("\nVetor A:")
    vetor_a = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    print("Vetor B:")
    vetor_b = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    resultado = subtrair_vetores(vetor_a, vetor_b)
    print(f"\nA - B = {resultado}\n")

    registrar_operacao("subtracao", dimensao, vetor_a, vetor_b, resultado)


def opcao_multiplicar_escalar():
    print("\n--- MULTIPLICACAO POR ESCALAR ---")
    dimensao = escolher_dimensao()

    print("\nVetor:")
    vetor = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    escalar = ler_numero("Digite o escalar: ")
    resultado = multiplicar_escalar(vetor, escalar)
    print(f"\nVetor x {escalar} = {resultado}\n")

    # nao tem "vetor B" aqui, entao guarda o vetor original + o escalar
    registrar_operacao("escalar", dimensao, vetor, None, resultado, escalar)


def opcao_produto_escalar():
    print("\n--- PRODUTO ESCALAR ---")
    dimensao = escolher_dimensao()

    print("\nVetor A:")
    vetor_a = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    print("Vetor B:")
    vetor_b = ler_vetor_2d() if dimensao == "2D" else ler_vetor_3d()

    resultado = produto_escalar(vetor_a, vetor_b)
    print(f"\nProduto escalar A . B = {resultado}\n")
    print("Obs: o produto escalar e um numero, entao nao ha grafico para ele.\n")
    # nao registra como ultima operacao pq nao da pra desenhar um numero


def opcao_produto_vetorial():
    print("\n--- PRODUTO VETORIAL ---")
    print("Obs: o produto vetorial so existe para vetores 3D.\n")

    print("Vetor A:")
    vetor_a = ler_vetor_3d()

    print("Vetor B:")
    vetor_b = ler_vetor_3d()

    resultado = produto_vetorial(vetor_a, vetor_b)
    print(f"\nA x B = {resultado}\n")

    registrar_operacao("vetorial", "3D", vetor_a, vetor_b, resultado)


def opcao_visualizar_vetor():
    print("\n--- VISUALIZAR VETOR ---")
    dimensao = escolher_dimensao()

    if dimensao == "2D":
        vetor = ler_vetor_2d()
        plotar_vetor_2d(vetor, titulo="Vetor 2D")
    else:
        vetor = ler_vetor_3d()
        plotar_vetor_3d(vetor, titulo="Vetor 3D")


def opcao_visualizar_operacao():
    print("\n--- VISUALIZAR OPERACAO ---")

    if ultima_operacao_tipo is None:
        print("Nenhuma operacao foi feita ainda. Faca uma operacao antes de "
              "visualizar (opcoes 3 a 7 do menu de vetores).\n")
        return

    tipo = ultima_operacao_tipo
    dimensao = ultima_operacao_dimensao
    vetor_a = ultimo_vetor_a
    vetor_b = ultimo_vetor_b
    resultado = ultimo_resultado

    if tipo == "soma":
        titulo = "Soma de vetores"
        if dimensao == "2D":
            plotar_operacao_2d(vetor_a, vetor_b, resultado, titulo)
        else:
            plotar_operacao_3d(vetor_a, vetor_b, resultado, titulo)

    elif tipo == "subtracao":
        titulo = "Subtracao de vetores"
        if dimensao == "2D":
            plotar_operacao_2d(vetor_a, vetor_b, resultado, titulo)
        else:
            plotar_operacao_3d(vetor_a, vetor_b, resultado, titulo)

    elif tipo == "escalar":
        titulo = f"Multiplicacao por escalar ({ultimo_escalar})"
        if dimensao == "2D":
            plotar_operacao_um_vetor_2d(vetor_a, resultado, titulo)
        else:
            plotar_operacao_um_vetor_3d(vetor_a, resultado, titulo)

    elif tipo == "vetorial":
        titulo = "Produto vetorial (A x B)"
        plotar_operacao_3d(vetor_a, vetor_b, resultado, titulo)


def mostrar_menu_principal():
    print("\n==============================")
    print("PROJETO 1 - VETORES")
    print("==============================")
    print("1 - Conversao de unidades")
    print("2 - Vetores")
    print("0 - Sair")


def mostrar_menu_vetores():
    print("\n------------------------------")
    print("MENU DE VETORES")
    print("------------------------------")
    print("1 - Criar vetor 2D")
    print("2 - Criar vetor 3D")
    print("3 - Somar vetores")
    print("4 - Subtrair vetores")
    print("5 - Multiplicar vetor por escalar")
    print("6 - Produto escalar")
    print("7 - Produto vetorial")
    print("8 - Visualizar vetor")
    print("9 - Visualizar operacao")
    print("0 - Voltar ao menu principal")


def menu_vetores():
    while True:
        mostrar_menu_vetores()
        opcao = ler_opcao_inteira("\nEscolha uma opcao: ", 0, 9)

        if opcao == 0:
            break
        elif opcao == 1:
            opcao_criar_vetor_2d()
        elif opcao == 2:
            opcao_criar_vetor_3d()
        elif opcao == 3:
            opcao_somar_vetores()
        elif opcao == 4:
            opcao_subtrair_vetores()
        elif opcao == 5:
            opcao_multiplicar_escalar()
        elif opcao == 6:
            opcao_produto_escalar()
        elif opcao == 7:
            opcao_produto_vetorial()
        elif opcao == 8:
            opcao_visualizar_vetor()
        elif opcao == 9:
            opcao_visualizar_operacao()


def main():
    print("Bem-vindo ao Projeto 1 de Vetores!")

    while True:
        mostrar_menu_principal()
        opcao = ler_opcao_inteira("\nEscolha uma opcao: ", 0, 2)

        if opcao == 0:
            print("\nEncerrando o programa. Ate mais!")
            break
        elif opcao == 1:
            converter_unidades()
        elif opcao == 2:
            menu_vetores()


if __name__ == "__main__":
    main()