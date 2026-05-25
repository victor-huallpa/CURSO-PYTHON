"""
=========================================================
PAQUETE DE ONDAS
=========================================================

Ecuación principal:

    Ψ(x,t) = Σ Aₙ exp(i(kₙx - ωₙt))

Descripción:
------------
Simulación de un paquete de ondas
formado por la superposición de
muchas ondas planas cuánticas.

Representa una partícula localizada.

Conceptos físicos:
------------------
- superposición cuántica
- localización espacial
- dispersión temporal
- interferencia

Objetivos:
----------
1. Comprender paquetes de ondas.
2. Visualizar superposición cuántica.
3. Observar dispersión temporal.
4. Introducir localización cuántica.

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
# ESPACIO
# =====================================================

x = np.linspace(
    -40,
    40,
    4000
)


# =====================================================
# TIEMPO
# =====================================================

t = 0


# =====================================================
# PARÁMETROS DEL PAQUETE
# =====================================================

# Número de ondas
num_ondas = 80

# Número de onda central
k0 = 5

# Dispersión de números de onda
sigma_k = 0.6


# =====================================================
# GENERAR NÚMEROS DE ONDA
# =====================================================

k_valores = np.linspace(
    k0 - 2,
    k0 + 2,
    num_ondas
)


# =====================================================
# FUNCIÓN DE ONDA
# =====================================================

def paquete_ondas(x, t):
    """
    Construye el paquete de ondas
    mediante superposición.
    """

    psi = np.zeros_like(
        x,
        dtype=complex
    )

    for k in k_valores:

        # Peso gaussiano
        A = np.exp(
            -(k - k0) ** 2
            / (2 * sigma_k ** 2)
        )

        # Relación de dispersión simple
        omega = k ** 2 / 2

        # Superposición
        psi += A * np.exp(
            1j * (k * x - omega * t)
        )

    return psi


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title(
    "Paquete de Ondas Cuántico"
)

eje.set_xlabel("Posición x")

eje.set_ylabel("Probabilidad")

eje.set_xlim(-40, 40)

eje.set_ylim(0, 80)

eje.grid(True)


# =====================================================
# LÍNEA DE GRÁFICA
# =====================================================

linea, = eje.plot(
    [],
    [],
    linewidth=2
)


# =====================================================
# INICIALIZACIÓN
# =====================================================

def inicializar():

    linea.set_data([], [])

    return linea,


# =====================================================
# ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Evolución temporal del paquete.
    """

    tiempo = frame * 0.05

    psi = paquete_ondas(
        x,
        tiempo
    )

    # Densidad de probabilidad
    probabilidad = np.abs(psi) ** 2

    linea.set_data(
        x,
        probabilidad
    )

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