import itertools
from collections import Counter
from fractions import Fraction

def mostrar_tabla_probabilidades(num_dados):
    # Generar todas las combinaciones posibles de los dados
    dados = list(itertools.product(range(1, 7), repeat=num_dados))

    # Calcular la suma de cada combinación
    sumas = [sum(comb) for comb in dados]

    # Contar las ocurrencias de cada suma
    contador_sumas = Counter(sumas)

    # Total de combinaciones posibles
    total_combinaciones = len(dados)

    # Mostrar tabla con todas las sumas posibles y sus probabilidades
    print(f"Tabla de probabilidades para {num_dados} dados:")
    print(f"{'Suma':<6} {'Probabilidad'}")
    print("-" * 20)

    # Mostrar las probabilidades para todas las sumas posibles
    for suma in range(num_dados, 6 * num_dados + 1):
        probabilidad = Fraction(contador_sumas[suma], total_combinaciones)
        print(f"{suma:<6} {probabilidad}")

# Ejemplo de uso:
num_dados = int(input("Introduce el número de dados: "))

mostrar_tabla_probabilidades(num_dados)

