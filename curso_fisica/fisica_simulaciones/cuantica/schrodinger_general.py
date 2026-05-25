"""
=========================================================
ECUACIÓN DE SCHRÖDINGER GENERAL
=========================================================

Ecuación principal:

    iħ ∂ψ/∂t =
    -(ħ²/2m) ∂²ψ/∂x² + Vψ

Descripción:
------------
Simulación de una partícula cuántica
interactuando con un potencial.

Se utiliza un pozo de potencial
para observar confinamiento cuántico.

Conceptos físicos:
------------------
- potencial cuántico
- confinamiento
- barreras energéticas
- evolución temporal

Objetivos:
----------
1. Introducir potenciales cuánticos.
2. Visualizar confinamiento.
3. Comprender dinámica cuántica.
4. Base para túnel cuántico.

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
# CONSTANTES
# =====================================================

hbar = 1

m = 1


# =====================================================
# ESPACIO
# =====================================================

N = 1200

x = np.linspace(
    -20,
    20,
    N
)

dx = x[1] - x[0]


# =====================================================
# TIEMPO
# =====================================================

dt = 0.005


# =====================================================
# POTENCIAL CUÁNTICO
# =====================================================

V = np.zeros(N)

# Barreras laterales
V[x < -5] = 5

V[x > 5] = 5


# =====================================================
# PAQUETE DE ONDA INICIAL
# =====================================================

x0 = 0

k0 = 3

sigma = 1


# =====================================================
# FUNCIÓN DE ONDA INICIAL
# =====================================================

psi = np.exp(
    -(x - x0) ** 2 / (2 * sigma ** 2)
) * np.exp(
    1j * k0 * x
)

# Normalización
psi /= np.sqrt(
    np.sum(np.abs(psi) ** 2)
)


# =====================================================
# OPERADOR LAPLACIANO
# =====================================================

def laplaciano(psi):
    """
    Calcula la segunda derivada espacial.
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
    Aplica evolución temporal usando
    Schrödinger general.
    """

    termino_cinetico = (
        -1j * hbar / (2 * m)
    ) * laplaciano(psi)

    termino_potencial = (
        -1j / hbar
    ) * V * psi

    return psi + (
        termino_cinetico
        + termino_potencial
    ) * dt


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title(
    "Schrödinger General con Potencial"
)

eje.set_xlabel("Posición x")

eje.set_ylabel("Probabilidad")

eje.set_xlim(-20, 20)

eje.set_ylim(0, 1)

eje.grid(True)


# =====================================================
# POTENCIAL ESCALADO
# =====================================================

potencial_visual = V / np.max(V)


# =====================================================
# LÍNEAS DE GRÁFICA
# =====================================================

linea_probabilidad, = eje.plot(
    [],
    [],
    linewidth=2,
    label="|ψ|²"
)

linea_potencial, = eje.plot(
    x,
    potencial_visual,
    linestyle="--",
    label="Potencial"
)


# =====================================================
# LEYENDA
# =====================================================

eje.legend()


# =====================================================
# INICIALIZACIÓN
# =====================================================

def inicializar():

    linea_probabilidad.set_data([], [])

    return (
        linea_probabilidad,
        linea_potencial
    )


# =====================================================
# ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza la simulación temporal.
    """

    global psi

    psi = evolucion(psi)

    probabilidad = np.abs(psi) ** 2

    linea_probabilidad.set_data(
        x,
        probabilidad
    )

    return (
        linea_probabilidad,
        linea_potencial
    )


# =====================================================
# CREAR ANIMACIÓN
# =====================================================

animacion = FuncAnimation(
    figura,
    animar,
    init_func=inicializar,
    frames=700,
    interval=20,
    blit=True
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()