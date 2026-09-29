import math


def calcular_volume():
    Ab = float(input("área da base: "))
    h = float(input("altura da pirâmide: "))
    volume = (Ab * h) / 3
    print(f"Volume: {volume}")


def calcular_area_total():
    Ab = float(input("área da base: "))
    Al = float(input("área lateral: "))
    At = Ab + Al
    print(f"Área Total: {At}")


def calcular_area_lateral():
    n_lados = int(input("número de lados da base: "))
    A_face = float(input("área de uma face lateral: "))
    Al = n_lados * A_face
    print(f"Área Lateral: {Al}")


def calcular_area_face():
    base_face = float(input("medida da aresta da base: "))
    g = float(input("medida do apótema da pirâmide (altura da face): "))
    A_face = (base_face * g) / 2
    print(f"Área da Face Lateral: {A_face}")


def calcular_tronco():
    h = float(input("altura do tronco: "))
    AB = float(input("área da base maior: "))
    Ab = float(input("área da base menor: "))
    V_tronco = (h / 3) * (AB + Ab + math.sqrt(AB * Ab))
    print(f"Volume do Tronco de Pirâmide: {V_tronco}")


def calcular_aresta_base():
    n_lados = int(input("número de lados da base: "))
    Al = float(input("área lateral total: "))
    g = float(input("medida do apótema da pirâmide: "))
    # Al = n_lados * (aresta_base * g / 2) -> aresta_base = (2 * Al) / (n_lados * g)
    aresta_base = (2 * Al) / (n_lados * g)
    print(f"Aresta da Base: {aresta_base}")


def calcular_altura():
    g = float(input("medida do apótema da pirâmide: "))
    a_b = float(input("medida do apótema da base: "))
    # Teorema de Pitágoras: g² = h² + a_b²
    if g >= a_b:
        h = math.sqrt(g**2 - a_b**2)
        print(f"Altura da pirâmide: {h}")
    else:
        print("Erro: O apótema da pirâmide deve ser maior que o apótema da base.")


def calcular_apotema_piramide():
    h = float(input("altura da pirâmide: "))
    a_b = float(input("medida do apótema da base: "))
    # Teorema de Pitágoras: g² = h² + a_b²
    g = math.sqrt(h**2 + a_b**2)
    print(f"Apótema da pirâmide: {g}")


def calcular_apotema_base():
    aresta_base = float(input("medida da aresta da base: "))
    n_lados = int(input("número de lados da base: "))
    # Fórmula do apótema de um polígono regular
    a_b = aresta_base / (2 * math.tan(math.pi / n_lados))
    print(f"Apótema da base: {a_b}")


def calcular_aresta_lateral():
    h = float(input("altura da pirâmide: "))
    R = float(input("raio da circunferência circunscrita à base: "))
    # Teorema de Pitágoras: a_l² = h² + R²
    aresta_lateral = math.sqrt(h**2 + R**2)
    print(f"Aresta Lateral: {aresta_lateral}")


def calcular_area_base():
    n_lados = int(input("número de lados da base: "))
    aresta_base = float(input("medida da aresta da base: "))
    a_b = float(input("medida do apótema da base: "))
    Ab = (n_lados * aresta_base * a_b) / 2
    print(f"Área da Base: {Ab}")


menu = """
[1] calcular volume
[2] calcular área total
[3] calcular área lateral
[4] calcular área da face
[5] calcular tronco
[6] calcular aresta da base
[7] calcular altura
[8] calcular apótema da pirâmide
[9] calcular apótema da base
[10] calcular aresta lateral
[11] calcular área da base
"""

print(menu)
opcao = int(input("escolha uma opção: "))

# Dicionário mapeando as opções do menu para suas respectivas funções
acoes = {
    1: calcular_volume,
    2: calcular_area_total,
    3: calcular_area_lateral,
    4: calcular_area_face,
    5: calcular_tronco,
    6: calcular_aresta_base,
    7: calcular_altura,
    8: calcular_apotema_piramide,
    9: calcular_apotema_base,
    10: calcular_aresta_lateral,
    11: calcular_area_base,
}

if opcao in acoes:
    acoes[opcao]()
else:
    print("Opção inválida.")