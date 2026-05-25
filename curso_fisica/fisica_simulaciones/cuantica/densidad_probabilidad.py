"""
=========================================================
DENSIDAD DE PROBABILIDAD
=========================================================

Ecuación principal:

    P(x) = |ψ(x,t)|²

Descripción:
------------
Simulación de la densidad de probabilidad
de una partícula cuántica.

La probabilidad se obtiene calculando
el módulo cuadrado de la función de onda.

Conceptos físicos:
------------------
- probabilidad cuántica
- interpretación de Born
- función de onda
- módulo cuadrado

Objetivos:
----------
1. Comprender densidad de probabilidad.
2. Relacionar ψ con observables físicos.
3. Visualizar distribución espacial.
4. Introducir interpretación cuántica.

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
# PARÁMETROS DE LA ONDA
# =====================================================

# Amplitud
A = 1

# Número de onda
k = 3

# Frecuencia angular
omega = 2

# Tiempo fijo
t = 0


# =====================================================
# ESPACIO
# =====================================================

x = np.linspace(
    -10,
    10,
    4000
)


# =====================================================
# FUNCIÓN DE ONDA
# =====================================================

def funcion_onda(x, t):
    """
    Calcula la función de onda compleja.

    Parámetros:
    -----------
    x : ndarray
        Posición espacial

    t : float
        Tiempo

    Retorna:
    --------
    ndarray
        Función de onda compleja
    """

    return A * np.exp(
        1j * (k * x - omega * t)
    )


# =====================================================
# CÁLCULO DE ψ
# =====================================================

psi = funcion_onda(x, t)


# =====================================================
# DENSIDAD DE PROBABILIDAD
# =====================================================

def densidad_probabilidad(psi):
    """
    Calcula la densidad de probabilidad.

    Parámetros:
    -----------
    psi : ndarray
        Función de onda compleja

    Retorna:
    --------
    ndarray
        Densidad de probabilidad
    """

    return np.abs(psi) ** 2


# =====================================================
# CÁLCULO DE PROBABILIDAD
# =====================================================

P = densidad_probabilidad(psi)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title(
    "Densidad de Probabilidad Cuántica"
)

eje.set_xlabel("Posición x")

eje.set_ylabel("Probabilidad")


# =====================================================
# CUADRÍCULA
# =====================================================

eje.grid(True)


# =====================================================
# GRAFICAR PROBABILIDAD
# =====================================================

eje.plot(
    x,
    P,
    linewidth=2,
    label="|ψ|²"
)


# =====================================================
# LEYENDA
# =====================================================

eje.legend()


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()