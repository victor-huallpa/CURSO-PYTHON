"""
=========================================================
FÓRMULA DE RYDBERG
=========================================================

Ecuación principal:

    1/λ = R (1/nf² - 1/ni²)

Descripción:
------------
Simulación de las líneas espectrales
del átomo de hidrógeno utilizando
la fórmula de Rydberg.

Se calculan las longitudes de onda
emitidas durante transiciones electrónicas.

Conceptos físicos:
------------------
- espectros atómicos
- líneas espectrales
- transiciones electrónicas
- emisión de fotones

Objetivos:
----------
1. Comprender espectros atómicos.
2. Calcular longitudes de onda.
3. Visualizar líneas espectrales.
4. Introducir espectroscopía.

Librerías:
-----------
numpy
matplotlib
"""

# =====================================================
# IMPORTACIÓN DE LIBRERÍAS
# =====================================================

import numpy as np
import matplotlib.pyplot as plt


# =====================================================
# CONSTANTE DE RYDBERG
# =====================================================

# Constante de Rydberg (1/m)
R = 1.097e7


# =====================================================
# FUNCIÓN DE RYDBERG
# =====================================================

def longitud_onda(ni, nf):
    """
    Calcula la longitud de onda emitida
    durante una transición electrónica.

    Parámetros:
    -----------
    ni : int
        Nivel inicial

    nf : int
        Nivel final

    Retorna:
    --------
    float
        Longitud de onda en metros
    """

    inversa_lambda = R * (
        (1 / (nf ** 2))
        - (1 / (ni ** 2))
    )

    return 1 / inversa_lambda


# =====================================================
# SERIE DE BALMER
# =====================================================

# Transiciones hacia nf = 2
nf = 2

niveles_iniciales = [3, 4, 5, 6, 7, 8]


# =====================================================
# CALCULAR LONGITUDES DE ONDA
# =====================================================

longitudes_onda = []

for ni in niveles_iniciales:

    lambda_valor = longitud_onda(ni, nf)

    # Convertir a nanómetros
    lambda_nm = lambda_valor * 1e9

    longitudes_onda.append(lambda_nm)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(10, 5))

eje.set_title("Serie de Balmer - Espectro del Hidrógeno")

eje.set_xlabel("Transición Electrónica")
eje.set_ylabel("Longitud de Onda (nm)")


# =====================================================
# NOMBRES DE TRANSICIONES
# =====================================================

etiquetas = [
    f"{ni} → {nf}"
    for ni in niveles_iniciales
]


# =====================================================
# GRÁFICA DE BARRAS
# =====================================================

eje.bar(
    etiquetas,
    longitudes_onda
)


# =====================================================
# MOSTRAR VALORES
# =====================================================

for i, valor in enumerate(longitudes_onda):

    eje.text(
        i,
        valor + 5,
        f"{valor:.1f} nm",
        ha="center"
    )


# =====================================================
# CUADRÍCULA
# =====================================================

eje.grid(True)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()