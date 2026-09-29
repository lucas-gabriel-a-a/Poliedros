import math


def calcular_volume():
    n_lados = int(input("número de lados: "))
    lado = float(input("medida do lado da base: "))
    h = float(input("altura do prisma: "))
    if n_lados % 2 == 0:
        apotema = lado / 2
    else:
        apotema = float(input("medida do apótema: "))
    Ab = (n_lados * lado * apotema) / 2
    volume = Ab * h
    print(f"Volume: {volume}")


def calcular_area_total():
    n_lados = int(input("número de lados: "))
    lado = float(input("medida do lado da base: "))
    h = float(input("altura do prisma: "))
    apotema = float(input("medida do apótema da base: "))
    Ab = (n_lados * lado * apotema) / 2
    Al = n_lados * (lado * h)
    At = 2 * Ab + Al
    print(f"Área Total: {At}")


def calcular_area_base():
    n_lados = int(input("número de lados: "))
    lado = float(input("medida do lado da base: "))
    apotema = float(input("medida do apótema da base: "))
    Ab = (n_lados * lado * apotema) / 2
    print(f"Área da Base: {Ab}")


def calcular_area_lateral():
    n_lados = int(input("número de lados: "))
    lado = float(input("medida do lado da base: "))
    h = float(input("altura do prisma: "))
    Al = n_lados * (lado * h)
    print(f"Área Lateral: {Al}")


def calcular_area_face():
    lado = float(input("medida do lado da base: "))
    h = float(input("altura do prisma: "))
    A_face = lado * h
    print(f"Área da Face Lateral: {A_face}")


def calcular_quantos_lados():
    Al = float(input("área lateral total: "))
    A_face = float(input("área de uma face lateral: "))
    n_lados = int(Al / A_face)
    print(f"Número de lados da base: {n_lados}")


def calcular_lado_prisma():
    A_face = float(input("área de uma face lateral: "))
    h = float(input("altura do prisma: "))
    lado = A_face / h
    print(f"Medida do lado da base: {lado}")


def calcular_altura_prisma():
    volume = float(input("volume do prisma: "))
    Ab = float(input("área da base: "))
    h = volume / Ab
    print(f"Altura do prisma: {h}")


def calcular_apotema_base():
    lado = float(input("medida do lado da base: "))
    n_lados = int(input("número de lados: "))
    # Fórmula geral para o apótema de um polígono regular: r = a / (2 * tan(pi / n))
    apotema = lado / (2 * math.tan(math.pi / n_lados))
    print(f"Apótema da base: {apotema}")


menu = """
[1] calcular volume
[2] calcular área total
[3] calcular área da base
[4] calcular área lateral
[5] calcular área da face
[6] quantos lados o prisma possui
[7] qual o lado do prisma
[8] altura do prisma
[9] apótema da base
"""

print(menu)
opcao = int(input("escolha uma opção: "))

# Dicionário mapeando a opção diretamente para a sua respectiva função
acoes = {
    1: calcular_volume,
    2: calcular_area_total,
    3: calcular_area_base,
    4: calcular_area_lateral,
    5: calcular_area_face,
    6: calcular_quantos_lados,
    7: calcular_lado_prisma,
    8: calcular_altura_prisma,
    9: calcular_apotema_base,
}

if opcao in acoes:
    acoes[opcao]()
else:
    print("Opção inválida.")