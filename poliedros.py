import math

# --- 1. POLIEDROS REGULARES DE PLATÃO (Volume, Área, Lado) ---


def calcular_tetraedro_regular():
    print("\n--- Tetraedro Regular (4 faces triangulares equiláteras) ---")
    a = float(input("Medida da aresta (a): "))
    area_total = (a**2) * math.sqrt(3)
    volume = ((a**3) * math.sqrt(2)) / 12
    altura = (a * math.sqrt(6)) / 3
    print(f"Área Total: {area_total:.2f}")
    print(f"Volume: {volume:.2f}")
    print(f"Altura do Tetraedro: {altura:.2f}")


def calcular_hexaedro_regular():
    print("\n--- Hexaedro Regular / Cubo (6 faces quadradas) ---")
    a = float(input("Medida da aresta (a): "))
    area_total = 6 * (a**2)
    volume = a**3
    diagonal = a * math.sqrt(3)
    print(f"Área Total: {area_total:.2f}")
    print(f"Volume: {volume:.2f}")
    print(f"Diagonal do Cubo: {diagonal:.2f}")


def calcular_octaedro_regular():
    print("\n--- Octaedro Regular (8 faces triangulares equiláteras) ---")
    a = float(input("Medida da aresta (a): "))
    area_total = 2 * (a**2) * math.sqrt(3)
    volume = ((a**3) * math.sqrt(2)) / 3
    print(f"Área Total: {area_total:.2f}")
    print(f"Volume: {volume:.2f}")


def calcular_dodecaedro_regular():
    print("\n--- Dodecaedro Regular (12 faces pentagonais regulares) ---")
    a = float(input("Medida da aresta (a): "))
    area_total = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * (a**2)
    volume = ((15 + 7 * math.sqrt(5)) / 4) * (a**3)
    print(f"Área Total: {area_total:.2f}")
    print(f"Volume: {volume:.2f}")


def calcular_icosaedro_regular():
    print("\n--- Icosaedro Regular (20 faces triangulares equiláteras) ---")
    a = float(input("Medida da aresta (a): "))
    area_total = 5 * (a**2) * math.sqrt(3)
    volume = (5 / 12) * (3 + math.sqrt(5)) * (a**3)
    print(f"Área Total: {area_total:.2f}")
    print(f"Volume: {volume:.2f}")


# --- 2. CÁLCULOS DE ÁREAS E ARESTAS ---


def calcular_area_total_qualquer_poliedro():
    print("\n--- Área Total por Soma das Faces ---")
    qtd_tipos = int(
        input("Quantos tipos diferentes de faces o poliedro possui? ")
    )
    area_total = 0

    for i in range(1, qtd_tipos + 1):
        qtd_faces = int(input(f"\nQuantidade de faces do tipo {i}: "))
        area_uma_face = float(input(f"Área de UMA face do tipo {i}: "))
        area_total += qtd_faces * area_uma_face

    print(f"\nÁrea Total da Superfície do Poliedro: {area_total:.2f}")


def calcular_aresta_pela_area_face():
    print("\n--- Descobrir Aresta/Lado a partir da Área de 1 Face ---")
    print("[1] Face Triangular Equilátera")
    print("[2] Face Quadrada")
    print("[3] Face Hexagonal Regular")
    tipo = int(input("Tipo da face: "))
    area = float(input("Área da face: "))

    if tipo == 1:
        a = math.sqrt((4 * area) / math.sqrt(3))
        print(f"Medida da aresta (a) = {a:.2f}")
    elif tipo == 2:
        a = math.sqrt(area)
        print(f"Medida da aresta (a) = {a:.2f}")
    elif tipo == 3:
        a = math.sqrt((2 * area) / (3 * math.sqrt(3)))
        print(f"Medida da aresta (a) = {a:.2f}")
    else:
        print("Opção inválida.")


# --- 3. RELAÇÕES TOPOLÓGICAS E EULER ---


def calcular_relacao_euler():
    print("\n--- Relação de Euler (V - A + F = 2) ---")
    print("O que você deseja calcular?")
    print("[1] Vértices (V)")
    print("[2] Arestas (A)")
    print("[3] Faces (F)")
    sub = int(input("Escolha: "))

    if sub == 1:
        A = int(input("Arestas (A): "))
        F = int(input("Faces (F): "))
        V = 2 + A - F
        print(f"Vértices (V) = {V}")
    elif sub == 2:
        V = int(input("Vértices (V): "))
        F = int(input("Faces (F): "))
        A = V + F - 2
        print(f"Arestas (A) = {A}")
    elif sub == 3:
        V = int(input("Vértices (V): "))
        A = int(input("Arestas (A): "))
        F = 2 + A - V
        print(f"Faces (F) = {F}")
    else:
        print("Opção inválida.")


def calcular_arestas_por_faces_iguais():
    print("\n--- Poliedro com faces do mesmo tipo ---")
    F = int(input("Quantidade total de faces (F): "))
    n = int(
        input(
            "Número de arestas/lados de cada face (ex: 3 p/ triângulo, 4 p/ quadrado): "
        )
    )
    A = (n * F) // 2
    print(f"Quantidade total de arestas (A) = {A}")


def calcular_arestas_por_faces_mistas():
    print("\n--- Poliedro com diferentes tipos de faces ---")
    qtd_tipos = int(
        input("Quantos tipos diferentes de faces o poliedro possui? ")
    )
    soma_lados_faces = 0
    total_faces = 0

    for i in range(1, qtd_tipos + 1):
        f = int(input(f"Quantidade de faces do tipo {i}: "))
        n = int(input("Número de lados/arestas dessas faces: "))
        soma_lados_faces += f * n
        total_faces += f

    A = soma_lados_faces // 2
    print(f"\nTotal de Faces (F) = {total_faces}")
    print(f"Quantidade total de Arestas (A) = {A}")


def calcular_arestas_por_vertices():
    print(
        "\n--- Poliedro onde cada vértice concorre o mesmo nº de arestas ---"
    )
    V = int(input("Quantidade total de vértices (V): "))
    m = int(input("Número de arestas que partem de cada vértice: "))
    A = (m * V) // 2
    print(f"Quantidade total de arestas (A) = {A}")


# --- 4. ÂNGULOS E TABELA DE PLATÃO ---


def calcular_soma_angulos_faces():
    print(
        "\n--- Soma dos Ângulos Internos de Todas as Faces S = (V - 2) * 360° ---"
    )
    V = int(input("Quantidade de vértices (V): "))
    S = (V - 2) * 360
    print(f"Soma dos ângulos internos de todas as faces = {S}°")


def calcular_vertices_pela_soma_angulos():
    print("\n--- Vértices a partir da Soma dos Ângulos das Faces ---")
    S = float(input("Soma dos ângulos das faces (em graus): "))
    V = int((S / 360) + 2)
    print(f"Quantidade de vértices (V) = {V}")


def consultar_poliedros_platao():
    print("\n--- Tabela dos 5 Poliedros de Platão ---")
    platao = {
        "Tetraedro": {
            "V": 4,
            "A": 6,
            "F": 4,
            "Forma das faces": "3 Triângulos por vértice",
        },
        "Hexaedro (Cubo)": {
            "V": 8,
            "A": 12,
            "F": 6,
            "Forma das faces": "3 Quadrados por vértice",
        },
        "Octaedro": {
            "V": 6,
            "A": 12,
            "F": 8,
            "Forma das faces": "4 Triângulos por vértice",
        },
        "Dodecaedro": {
            "V": 20,
            "A": 30,
            "F": 12,
            "Forma das faces": "3 Pentágonos por vértice",
        },
        "Icosaedro": {
            "V": 12,
            "A": 30,
            "F": 20,
            "Forma das faces": "5 Triângulos por vértice",
        },
    }
    for nome, dados in platao.items():
        print(f"\n• {nome}:")
        print(
            f"  Vértices (V): {dados['V']} | Arestas (A): {dados['A']} | Faces (F): {dados['F']}"
        )
        print(f"  Características: {dados['Forma das faces']}")


menu = """
==================================================
        CÁLCULOS COMPLETOS EM POLIEDROS
==================================================
--- POLIEDROS REGULARES DE PLATÃO (Volume, Área, Lado) ---
[1] Tetraedro Regular (4 faces)
[2] Hexaedro Regular / Cubo (6 faces)
[3] Octaedro Regular (8 faces)
[4] Dodecaedro Regular (12 faces)
[5] Icosaedro Regular (20 faces)

--- CÁLCULOS DE ÁREA E MEDIDA DE LADO ---
[6] Área Total de qualquer poliedro (Soma das faces)
[7] Calcular medida do Lado/Aresta (pela Área da face)

--- RELAÇÕES TOPOLÓGICAS E EULER ---
[8] Relação de Euler (Calcular V, A ou F)
[9] Arestas por Faces de mesmo tipo (2A = n * F)
[10] Arestas por Faces Mistas (diferentes tipos de faces)
[11] Arestas por Grau de Vértices (2A = m * V)

--- ÂNGULOS E CONSULTA ---
[12] Soma dos Ângulos das Faces (S = (V - 2) * 360°)
[13] Vértices a partir da Soma dos Ângulos das faces
[14] Consultar Tabela dos Poliedros de Platão (V, A, F)
==================================================
"""

print(menu)
opcao = int(input("Escolha uma opção: "))

# Dicionário mapeando as 14 opções para suas respectivas funções
acoes = {
    1: calcular_tetraedro_regular,
    2: calcular_hexaedro_regular,
    3: calcular_octaedro_regular,
    4: calcular_dodecaedro_regular,
    5: calcular_icosaedro_regular,
    6: calcular_area_total_qualquer_poliedro,
    7: calcular_aresta_pela_area_face,
    8: calcular_relacao_euler,
    9: calcular_arestas_por_faces_iguais,
    10: calcular_arestas_por_faces_mistas,
    11: calcular_arestas_por_vertices,
    12: calcular_soma_angulos_faces,
    13: calcular_vertices_pela_soma_angulos,
    14: consultar_poliedros_platao,
}

if opcao in acoes:
    acoes[opcao]()
else:
    print("Opção inválida.")