"""
=========================================================
ONDA ESTACIONARIA
=========================================================

Ecuación:

    y(x,t) = 2A sin(kx) cos(ωt)

Descripción:
------------
Simulación de una onda estacionaria generada
por la superposición de dos ondas viajeras
idénticas propagándose en sentidos opuestos.

Características:
----------------
- Nodos      -> amplitud cero
- Vientres   -> amplitud máxima
- Resonancia

Objetivos:
----------
1. Visualizar ondas estacionarias.
2. Comprender nodos y vientres.
3. Introducir modos normales.
4. Base para mecánica cuántica.

Relaciones importantes:
-----------------------
k = 2π / λ

ω = 2πf

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
# PARÁMETROS FÍSICOS
# =====================================================

# Amplitud
AMPLITUD = 1

# Longitud de onda
LONGITUD_ONDA = 2

# Frecuencia
FRECUENCIA = 1


# =====================================================
# MAGNITUDES DERIVADAS
# =====================================================

# Número de onda
k = (2 * np.pi) / LONGITUD_ONDA

# Frecuencia angular
omega = 2 * np.pi * FRECUENCIA


# =====================================================
# DOMINIO ESPACIAL
# =====================================================

x = np.linspace(0, 10, 1000)


# =====================================================
# ECUACIÓN DE ONDA ESTACIONARIA
# =====================================================

def onda_estacionaria(x, t):
    """
    Calcula la amplitud de la onda estacionaria.

    Parámetros:
    -----------
    x : ndarray
        Posición espacial

    t : float
        Tiempo

    Retorna:
    --------
    y : ndarray
        Amplitud de la onda
    """

    return (
        2
        * AMPLITUD
        * np.sin(k * x)
        * np.cos(omega * t)
    )


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 6))

# Configuración visual
eje.set_title("Onda Estacionaria")
eje.set_xlabel("Posición (m)")
eje.set_ylabel("Amplitud")

# Límites
eje.set_xlim(0, 10)
eje.set_ylim(-2.5, 2.5)

# Cuadrícula
eje.grid(True)


# =====================================================
# LÍNEAS AUXILIARES
# =====================================================

# Línea central
eje.axhline(0, linestyle="--")

# =====================================================
# OBJETO GRÁFICO
# =====================================================

linea, = eje.plot([], [], lw=3)


# =====================================================
# FUNCIÓN DE INICIALIZACIÓN
# =====================================================

def inicializar():
    """
    Inicializa la animación.
    """

    linea.set_data([], [])

    return linea,


# =====================================================
# FUNCIÓN DE ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza la onda frame por frame.
    """

    # Tiempo actual
    t = frame / 50

    # Calcular onda
    y = onda_estacionaria(x, t)

    # Actualizar gráfica
    linea.set_data(x, y)

    return linea,


# =====================================================
# CREACIÓN DE ANIMACIÓN
# =====================================================

animacion = FuncAnimation(
    figura,
    animar,
    frames=500,
    init_func=inicializar,
    interval=20,
    blit=True
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()