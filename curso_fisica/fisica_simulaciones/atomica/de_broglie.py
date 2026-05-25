"""
=========================================================
LONGITUD DE ONDA DE DE BROGLIE
=========================================================

Ecuación principal:

    λ = h / p

Momento lineal:

    p = mv

Descripción:
------------
Simulación de la longitud de onda
asociada a partículas materiales.

Demuestra que:

- electrones
- protones
- partículas

también presentan comportamiento ondulatorio.

Conceptos físicos:
------------------
- dualidad onda-partícula
- momento lineal
- longitud de onda cuántica
- materia ondulatoria

Objetivos:
----------
1. Comprender dualidad onda-partícula.
2. Relacionar momento y longitud de onda.
3. Introducir mecánica cuántica moderna.
4. Base para Schrödinger.

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
# CONSTANTES FÍSICAS
# =====================================================

# Constante de Planck (J·s)
h = 6.626e-34

# Masa del electrón (kg)
masa_electron = 9.11e-31


# =====================================================
# VELOCIDADES DEL ELECTRÓN
# =====================================================

# Rango de velocidades
velocidad = np.linspace(1e5, 5e7, 2000)


# =====================================================
# MOMENTO LINEAL
# =====================================================

def momento(masa, velocidad):
    """
    Calcula el momento lineal.

    Parámetros:
    -----------
    masa : float
        Masa de la partícula

    velocidad : ndarray
        Velocidad

    Retorna:
    --------
    ndarray
        Momento lineal
    """

    return masa * velocidad


# =====================================================
# LONGITUD DE ONDA DE BROGLIE
# =====================================================

def longitud_onda(momentum):
    """
    Calcula la longitud de onda
    de De Broglie.

    Parámetros:
    -----------
    momentum : ndarray
        Momento lineal

    Retorna:
    --------
    ndarray
        Longitud de onda
    """

    return h / momentum


# =====================================================
# CÁLCULO DE MOMENTO
# =====================================================

p = momento(
    masa_electron,
    velocidad
)


# =====================================================
# CÁLCULO DE LONGITUD DE ONDA
# =====================================================

lambda_db = longitud_onda(p)

# Convertir a nanómetros
lambda_nm = lambda_db * 1e9


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(10, 5))

eje.set_title("Longitud de Onda de De Broglie")

eje.set_xlabel("Velocidad del electrón (m/s)")

eje.set_ylabel("Longitud de onda (nm)")


# =====================================================
# CUADRÍCULA
# =====================================================

eje.grid(True)


# =====================================================
# GRAFICAR RELACIÓN
# =====================================================

eje.plot(
    velocidad,
    lambda_nm,
    linewidth=2
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()