# 27/08/26
# BEM VINDO PROFESSOR LAZARO NOGUEIRA!! FIQUE A VONTADE, TENTEI USAR MINHA CRIATIVIDADE.
# ====================================================================================
#                        LABORATORIO DE PROGRAMAÇÃO
#  Eleição para selecionar o novo chefe CBI -- (UNIVERSO THE MENTALIST - NETFLIX)
# AUTOR(A): RA1237663 - Elza Vitória Mendes Silva Aquino.
# FRASE: "Lógica e observação resolvem qualquer mistério da vida -- e qualquer código."
# ====================================================================================

# Códigos de entrada:
# 0 encerra a votação, enquanto os códigos de 1 a 6 representam as opções de voto.

votos_para_jane = 0
votos_lisbon = 0
votos_cho = 0
votos_rigsby = 0
votos_nulos = 0
votos_brancos = 0
total_de_votos = 0

# Menu

print("=" * 55)  # o atalho para multiplicação da atribuição  "="
print("    ELEIÇÃO: CONSULTOR CHEFE DA CBI (CALIFORNIA)    ")
print("=" * 55)
print("1 - Patrick Jane")
print("2 - Teresa Lisbon")
print("3 - Kimball Cho")
print("4 - Wayne Rigsby")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar Votação e Exibir Resultados")
print("-" * 55)

# Estrutura condicional e repetição ENQUANTO( PORTUGUES )
# ENQUANTO (VALOR TRUE FIXO)
while True:
    voto = int(input("\nDigite o código do seu voto: "))

    # Estrutura condicional SE...
    if voto == 0:
        print("\nCaso encerrado! Processando as evidências e votos...")
        break  # encerrar o nosso loop ENQUANTO.

    elif voto == 1:
        votos_para_jane += 1
        total_de_votos += 1

    elif voto == 2:
        votos_lisbon += 1
        total_de_votos += 1

    elif voto == 3:
        votos_cho += 1
        total_de_votos += 1

    elif voto == 4:
        votos_rigsby += 1
        total_de_votos += 1

    elif voto == 5:
        votos_nulos += 1
        total_de_votos += 1

    elif voto == 6:
        votos_brancos += 1
        total_de_votos += 1

    else:
        print("Código inválido! Por favor, digite um valor entre 0 e 6.")

# Processamento e Cálculos

if total_de_votos > 0:

    # --Fórmula para calcular as porcentagens dos votos nulos e brancos.--
    percentual_nulos = (votos_nulos / total_de_votos) * 100
    percentual_brancos = (votos_brancos / total_de_votos) * 100

    # Função para descobrir o vencedor dessa eleição.
    # Função Max é para reunir quem tem mais votos.
    maior_votacao = max(
        votos_para_jane,
        votos_lisbon,
        votos_cho,
        votos_rigsby
    )

    if maior_votacao == 0:
        vencedor = "Nenhum candidato recebeu votos válidos."

    elif votos_para_jane == maior_votacao:
        vencedor = "Patrick Jane"

    elif votos_lisbon == maior_votacao:
        vencedor = "Teresa Lisbon"

    elif votos_cho == maior_votacao:
        vencedor = "Kimball Cho"

    else:
        vencedor = "Wayne Rigsby"

    # Console === Tabela de resultado dos votos de todos candidatos:

    print("\n" + "=" * 55)
    print("           RESULTADO FINAL DA ELEIÇÃO CBI CALIFORNIA")
    print("=" * 55)

    print(f"Total de votos em Patrick Jane:   {votos_para_jane}")
    print(f"Total de votos em Teresa Lisbon:  {votos_lisbon}")
    print(f"Total de votos em Kimball Cho:    {votos_cho}")
    print(f"Total de votos em Wayne Rigsby:   {votos_rigsby}")

    print("-" * 55)

    print(f"Total de votos Nulos:             {votos_nulos}")
    print(f"Total de votos em Branco:         {votos_brancos}")
    print(f"Total Geral de Votos:             {total_de_votos}")

    print("-" * 55)

    print(f"Porcentagem de Nulos:             {percentual_nulos:.2f}%")
    print(f"Porcentagem de Brancos:           {percentual_brancos:.2f}%")

    print("=" * 55)
    print(f"NOVO LÍDER DA CBI:                {vencedor}")
    print("=" * 55)

else:
    print("\nNenhum voto foi registrado no sistema da CBI.")

# "Existe uma grande diferença entre saber o caminho e percorrer o caminho." - Morpheus (Matrix)
# Prontinho:) ! Muito obrigado professor LAZARO NOGUEIRA
