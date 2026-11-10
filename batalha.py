
import random


def calcular_dano(ataque, defesa, critico=False):
    """Dano = ataque - defesa, mas nunca menos que 1.
    Se for um golpe crítico, o dano dobra.
    Exemplos: calcular_dano(18, 3) -> 15    calcular_dano(18, 3, True) -> 30
              calcular_dano(5, 12) -> 1"""
    # TODO
    dano = max(1, ataque - defesa)
    if critico:
        dano = dano * 2
    return dano


def aplicar_dano(vida, dano):
    """Devolve a vida depois do golpe (nunca fica negativa).
    Exemplos: aplicar_dano(60, 15) -> 45    aplicar_dano(10, 15) -> 0"""
    # TODO
    return max(0, vida - dano)


def curar(vida, vida_max, cura=30):
    """Devolve a vida depois de tomar uma poção (nunca passa de vida_max).
    Exemplos: curar(50, 100) -> 80    curar(90, 100) -> 100"""
    # TODO
    return min(vida_max, vida + cura)


def barra_de_vida(vida, vida_max, tamanho=10):
    """Monta uma barra de texto com 'tamanho' caracteres, por exemplo:
        barra_de_vida(60, 100) -> "[######----] 60/100"
    Quantidade de '#':  vida * tamanho // vida_max   (o resto é '-')
    Use um laço for com range(tamanho)."""
    # TODO
    quantidade = vida * tamanho // vida_max
    barra = ""

    for i in range(tamanho):
        if i < quantidade:
            barra += "#"
        else:
            barra += "-"

    return f"[{barra}] {vida}/{vida_max}"


def classificar_resultado(vida, vida_max):
    """Diz como foi a batalha olhando a vida que sobrou para o herói:
        vida igual a 0              -> "Derrota"
        vida igual a vida_max       -> "Vitória perfeita"
        vida >= metade de vida_max  -> "Vitória"
        senão                       -> "Vitória apertada" """
    # TODO: use if / elif / else
    if vida == 0:
        return "Derrota"
    elif vida == vida_max:
        return "Vitória perfeita"
    elif vida >= vida_max / 2:
        return "Vitória"
    else:
        return "Vitória apertada"


def ler_acao():
    """Mostra as ações e repete a pergunta ATÉ a pessoa digitar 1, 2 ou 3.
    Devolve o texto digitado ("1", "2" ou "3").
        1 - Atacar   2 - Tomar poção   3 - Fugir
    Se digitar outra coisa, mostre "Ação inválida!" e pergunte de novo."""
    # TODO: use while True e return
    while True:
        print("\n1 - Atacar")
        print("2 - Tomar poção")
        print("3 - Fugir")

        acao = input("Escolha uma ação: ")

        if acao == "1" or acao == "2" or acao == "3":
            return acao
        else:
            print("Ação inválida!")


def batalha(heroi, inimigo, pocoes=3):
    """Executa a batalha e devolve um dicionário com o resultado:
       {"resultado": "vitoria" | "derrota" | "fuga", "turnos": ...,
        "vida_restante": ..., "pocoes": quantas poções sobraram}
    """
    turno = 0
    while heroi["vida"] > 0 and inimigo["vida"] > 0:
        turno = turno + 1
        print(f"\n--- Turno {turno} ---")
        print(f"{heroi['nome']:<12} {barra_de_vida(heroi['vida'], heroi['vida_max'])}")
        print(f"{inimigo['nome']:<12} {barra_de_vida(inimigo['vida'], inimigo['vida_max'])}")

        acao = ler_acao()
        if acao == "1":
            # TODO: 1) sorteie o crítico:  critico = random.randint(1, 10) == 10
            #       2) calcule o dano com calcular_dano(ataque do herói, defesa do inimigo, critico)
            #       3) atualize a vida do inimigo com aplicar_dano
            #       4) mostre quanto de dano foi causado (avise se foi crítico)
            critico = random.randint(1, 10) == 10

            dano = calcular_dano(heroi["ataque"], inimigo["defesa"], critico)

            inimigo["vida"] = aplicar_dano(inimigo["vida"], dano)

            if critico:
                print(f"Golpe crítico! Você causou {dano} de dano!")
            else:
                print(f"Você causou {dano} de dano!")

        elif acao == "2":
            # TODO: se ainda houver poções: diminua 1, cure o herói com curar() e avise
            #       quantas restam. Se não houver: mostre "Você não tem mais poções!"
            if pocoes > 0:
                pocoes -= 1
                heroi["vida"] = curar(heroi["vida"], heroi["vida_max"])
                print("Você tomou uma poção!")
                print(f"Vida atual: {heroi['vida']}")
                print(f"Poções restantes: {pocoes}")
            else:
                print("Você não tem mais poções!")

        else:
            # TODO: mostre que o herói fugiu e devolva (return) o dicionário com
            #       "resultado": "fuga" (veja o formato no início desta função)
            print("O herói fugiu da batalha!")
            return {
                "resultado": "fuga",
                "turnos": turno,
                "vida_restante": heroi["vida"],
                "pocoes": pocoes
            }

        # TODO: se o inimigo ainda estiver vivo, ele ataca o herói
        #       (dano = calcular_dano(ataque do inimigo, defesa do herói), sem crítico)
        if inimigo["vida"] > 0:
            dano = calcular_dano(inimigo["ataque"], heroi["defesa"])
            heroi["vida"] = aplicar_dano(heroi["vida"], dano)
            print(f"{inimigo['nome']} causou {dano} de dano!")

    if heroi["vida"] > 0:
        resultado = "vitoria"
    else:
        resultado = "derrota"
    print("\n" + classificar_resultado(heroi["vida"], heroi["vida_max"]) + "!")
    return {"resultado": resultado, "turnos": turno,
            "vida_restante": heroi["vida"], "pocoes": pocoes}


# Este bloco só roda quando executamos ESTE arquivo (python batalha.py).
# Quando outro arquivo faz "import batalha", ele NÃO roda.
if __name__ == "__main__":
    heroi = {"nome": "Gork", "vida": 100, "vida_max": 100, "ataque": 18, "defesa": 5}
    inimigo = {"nome": "Goblin", "vida": 60, "vida_max": 60, "ataque": 12, "defesa": 3}
    final = batalha(heroi, inimigo)
    print(final)

