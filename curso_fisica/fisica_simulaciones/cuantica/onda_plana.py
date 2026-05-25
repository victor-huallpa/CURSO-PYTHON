"""
=========================================================
ONDA PLANA CUÁNTICA
=========================================================

Ecuación principal:

    ψ(x,t) = A exp(i(kx - ωt))

Descripción:
------------
Simulación de una onda plana cuántica.

La función de onda es compleja y contiene:

- parte real
- parte imaginaria

Representa una partícula libre propagándose.

Conceptos físicos:
------------------
- función de onda
- números complejos
- propagación cuántica
- mecánica cuántica

Objetivos:
----------
1. Introducir funciones de onda.
2. Visualizar ondas complejas.
3. Comprender propagación cuántica.
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
# PARÁMETROS DE LA ONDA
# =====================================================

# Amplitud
A = 1

# Número de onda
k = 2

# Frecuencia angular
omega = 4

# Tiempo fijo
t = 0


# =====================================================
# ESPACIO
# =====================================================

x = np.linspace(
    -10,
    10,
    2000
)


# =====================================================
# FUNCIÓN DE ONDA
# =====================================================

def funcion_onda(x, t):
    """
    Calcula la onda plana cuántica.

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
# PARTE REAL E IMAGINARIA
# =====================================================

parte_real = np.real(psi)

parte_imaginaria = np.imag(psi)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title("Onda Plana Cuántica")

eje.set_xlabel("Posición x")

eje.set_ylabel("Amplitud")


# =====================================================
# CUADRÍCULA
# =====================================================

eje.grid(True)


# =====================================================
# GRAFICAR PARTE REAL
# =====================================================

eje.plot(
    x,
    parte_real,
    linewidth=2,
    label="Parte Real"
)


# =====================================================
# GRAFICAR PARTE IMAGINARIA
# =====================================================

eje.plot(
    x,
    parte_imaginaria,
    linewidth=2,
    linestyle="--",
    label="Parte Imaginaria"
)


# =====================================================
# LEYENDA
# =====================================================

eje.legend()


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()