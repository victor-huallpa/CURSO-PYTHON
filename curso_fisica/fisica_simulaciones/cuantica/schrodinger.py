"""
=========================================================
ECUACIÓN DE SCHRÖDINGER
=========================================================

Ecuación principal:

    iħ ∂ψ/∂t =
    -(ħ²/2m) ∂²ψ/∂x²

Descripción:
------------
Simulación numérica simplificada de la
evolución temporal de una función de onda.

Se utiliza un paquete gaussiano inicial
que evoluciona libremente en el espacio.

Conceptos físicos:
------------------
- ecuación de Schrödinger
- evolución temporal
- propagación cuántica
- dinámica ondulatoria

Objetivos:
----------
1. Visualizar evolución cuántica.
2. Comprender dinámica de ψ.
3. Introducir simulaciones numéricas.
4. Base para potenciales cuánticos.

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
from matplotlib.animation import FuncAnimation


# =====================================================
# CONSTANTES FÍSICAS
# =====================================================

# Constante reducida de Planck
hbar = 1

# Masa de la partícula
m = 1


# =====================================================
# ESPACIO
# =====================================================

N = 1000

x = np.linspace(-20, 20, N)

dx = x[1] - x[0]


# =====================================================
# TIEMPO
# =====================================================

dt = 0.01


# =====================================================
# PAQUETE GAUSSIANO INICIAL
# =====================================================

x0 = -5

k0 = 5

sigma = 1


# =====================================================
# FUNCIÓN DE ONDA INICIAL
# =====================================================

psi = np.exp(
    -(x - x0) ** 2 / (2 * sigma ** 2)
) * np.exp(1j * k0 * x)

# Normalización inicial
psi /= np.sqrt(np.sum(np.abs(psi) ** 2))


# =====================================================
# OPERADOR LAPLACIANO
# =====================================================

def laplaciano(psi):
    """
    Calcula la segunda derivada espacial.

    Parámetros:
    -----------
    psi : ndarray
        Función de onda

    Retorna:
    --------
    ndarray
        Segunda derivada
    """

    return (
        np.roll(psi, -1)
        - 2 * psi
        + np.roll(psi, 1)
    ) / dx ** 2


# =====================================================
# EVOLUCIÓN TEMPORAL
# =====================================================

def evolucion(psi):
    """
    Aplica un paso temporal usando
    Schrödinger libre.

    Parámetros:
    -----------
    psi : ndarray
        Función de onda actual

    Retorna:
    --------
    ndarray
        Nueva función de onda
    """

    return psi + (
        -1j * hbar / (2 * m)
    ) * laplaciano(psi) * dt


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title(
    "Evolución de la Ecuación de Schrödinger"
)

eje.set_xlabel("Posición x")

eje.set_ylabel("Densidad de Probabilidad")

eje.set_xlim(-20, 20)

eje.set_ylim(0, 1)

eje.grid(True)


# =====================================================
# LÍNEA DE GRÁFICA
# =====================================================

linea, = eje.plot([], [], linewidth=2)


# =====================================================
# FUNCIÓN DE INICIALIZACIÓN
# =====================================================

def inicializar():

    linea.set_data([], [])

    return linea,


# =====================================================
# FUNCIÓN DE ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza la simulación temporal.
    """

    global psi

    # Evolución temporal
    psi = evolucion(psi)

    # Densidad de probabilidad
    probabilidad = np.abs(psi) ** 2

    # Actualizar gráfica
    linea.set_data(x, probabilidad)

    return linea,


# =====================================================
# CREAR ANIMACIÓN
# =====================================================

animacion = FuncAnimation(
    figura,
    animar,
    init_func=inicializar,
    frames=500,
    interval=20,
    blit=True
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()