def evaluar_heuristica_H1(esquinas_controladas, fichas_bordes, fichas_estables):
    return 100 * esquinas_controladas - 50 * fichas_bordes + fichas_estables

def evaluar_heuristica_H2(mov_legales_propios, mov_legales_oponente):
    return mov_legales_propios - mov_legales_oponente

def evaluar_heuristica_H3(fichas_propias, fichas_oponente, estables_propias, estables_oponente):
    return (fichas_propias - fichas_oponente) + 10 * (estables_propias - estables_oponente)

# Valores de ejemplo para cada tablero (reemplaza con los valores reales del laboratorio)
tableros = {
    "Tablero 1": {
        "esquinas_controladas": 2,
        "fichas_bordes": 5,
        "fichas_estables": 3,
        "mov_legales_propios": 12,
        "mov_legales_oponente": 10,
        "fichas_propias": 20,
        "fichas_oponente": 15,
        "estables_propias": 4,
        "estables_oponente": 2
    },
    "Tablero 2": {
        "esquinas_controladas": 3,
        "fichas_bordes": 6,
        "fichas_estables": 5,
        "mov_legales_propios": 10,
        "mov_legales_oponente": 8,
        "fichas_propias": 18,
        "fichas_oponente": 20,
        "estables_propias": 3,
        "estables_oponente": 3
    },
    "Tablero 3": {
        "esquinas_controladas": 1,
        "fichas_bordes": 4,
        "fichas_estables": 2,
        "mov_legales_propios": 15,
        "mov_legales_oponente": 12,
        "fichas_propias": 25,
        "fichas_oponente": 22,
        "estables_propias": 6,
        "estables_oponente": 4
    }
}

for nombre, valores in tableros.items():
    h1 = evaluar_heuristica_H1(valores["esquinas_controladas"], valores["fichas_bordes"], valores["fichas_estables"])
    h2 = evaluar_heuristica_H2(valores["mov_legales_propios"], valores["mov_legales_oponente"])
    h3 = evaluar_heuristica_H3(valores["fichas_propias"], valores["fichas_oponente"], valores["estables_propias"], valores["estables_oponente"])
    
    print(f"{nombre}: H1 = {h1}, H2 = {h2}, H3 = {h3}")
