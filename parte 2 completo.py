import numpy as np

# Definimos la matriz
matriz = np.array([
    [12, 3, 52, 81, 33, 55, 1, 39, 20, 47],
    [43, 57, 61, 78, 31, 25, 3, 4, 95, 99],
    [14, 41, 73, 20, 96, 73, 27, 67, 53, 68],
    [62, 15, 97, 5, 68, 12, 87, 78, 76, 57],
    [17, 25, 30, 22, 26, 81, 61, 62, 84, 34],
    [33, 71, 86, 32, 14, 72, 57, 25, 80, 42],
    [19, 41, 55, 80, 12, 39, 94, 2, 96, 45],
    [89, 25, 68, 83, 4, 77, 36, 87, 62, 70],
    [88, 44, 33, 12, 85, 11, 55, 38, 29, 3],
    [28, 84, 90, 24, 54, 52, 47, 21, 54, 30]
])

# Posición inicial en K9 (índice cero, sería (8, 9))
fila, columna = 8, 9
trayectoria = [(fila, columna)]  # Guarda la secuencia de posiciones visitadas

# Función para obtener los vecinos válidos
def obtener_vecinos(fila, columna):
    vecinos = []
    if fila > 0: vecinos.append((fila - 1, columna))  # Arriba
    if fila < matriz.shape[0] - 1: vecinos.append((fila + 1, columna))  # Abajo
    if columna > 0: vecinos.append((fila, columna - 1))  # Izquierda
    if columna < matriz.shape[1] - 1: vecinos.append((fila, columna + 1))  # Derecha
    return vecinos

# Hill Climbing Básico
while True:
    valor_actual = matriz[fila, columna]
    vecinos = obtener_vecinos(fila, columna)
    vecino_mejor = max(vecinos, key=lambda pos: matriz[pos])
    if matriz[vecino_mejor] > valor_actual:
        fila, columna = vecino_mejor
        trayectoria.append((fila, columna))
    else:
        break  # Se alcanzó un máximo local

print("Hill Climbing Básico - Trayectoria:", trayectoria)
print("Valor final (Máximo local):", matriz[fila, columna])

import random

# Restablecer la posición inicial
fila, columna = 8, 9
trayectoria_estocastica = [(fila, columna)]

# Hill Climbing Estocástico
while True:
    valor_actual = matriz[fila, columna]
    vecinos = obtener_vecinos(fila, columna)
    vecinos_mayores = [v for v in vecinos if matriz[v] > valor_actual]
    
    if vecinos_mayores:
        vecino_aleatorio = random.choice(vecinos_mayores)
        fila, columna = vecino_aleatorio
        trayectoria_estocastica.append((fila, columna))
    else:
        break  # Se alcanzó un máximo local

print("Hill Climbing Estocástico - Trayectoria:", trayectoria_estocastica)
print("Valor final (Máximo local):", matriz[fila, columna])

# Restablecer la posición inicial
fila, columna = 8, 9
trayectoria_first_choice = [(fila, columna)]

# Hill Climbing First-Choice
while True:
    valor_actual = matriz[fila, columna]
    vecinos = obtener_vecinos(fila, columna)
    random.shuffle(vecinos)  # Orden aleatorio de vecinos
    
    movimiento_realizado = False
    for vecino in vecinos:
        if matriz[vecino] > valor_actual:
            fila, columna = vecino
            trayectoria_first_choice.append((fila, columna))
            movimiento_realizado = True
            break
    
    if not movimiento_realizado:
        break  # Se alcanzó un máximo local

print("Hill Climbing First-Choice - Trayectoria:", trayectoria_first_choice)
print("Valor final (Máximo local):", matriz[fila, columna])

resultados_random_restart = []

# Random Restart Hill Climbing con 10 inicios aleatorios
for _ in range(10):
    fila, columna = random.randint(0, matriz.shape[0] - 1), random.randint(0, matriz.shape[1] - 1)
    trayectoria_restart = [(fila, columna)]
    
    while True:
        valor_actual = matriz[fila, columna]
        vecinos = obtener_vecinos(fila, columna)
        vecino_mejor = max(vecinos, key=lambda pos: matriz[pos])
        
        if matriz[vecino_mejor] > valor_actual:
            fila, columna = vecino_mejor
            trayectoria_restart.append((fila, columna))
        else:
            break  # Se alcanzó un máximo local
    
    resultados_random_restart.append((trayectoria_restart, matriz[fila, columna]))

# Mostrar los resultados de cada inicio aleatorio
for i, (trayectoria, valor_final) in enumerate(resultados_random_restart, 1):
    print(f"Inicio {i} - Trayectoria: {trayectoria}")
    print(f"Valor final (Máximo local): {valor_final}")
