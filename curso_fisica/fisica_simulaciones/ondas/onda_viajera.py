"""
=========================================================
ONDA VIAJERA
=========================================================

Ecuación:

    y(x,t) = A cos(kx - ωt + φ)

Descripción:
------------
Simulación de una onda viajera propagándose
a través del espacio.

La onda se desplaza sobre el eje X mientras
evoluciona en el tiempo.

Variables físicas:
------------------
A  -> amplitud
k  -> número de onda
ω  -> frecuencia angular
φ  -> fase inicial
x  -> posición espacial
t  -> tiempo

Relaciones importantes:
-----------------------
k = 2π / λ

ω = 2πf

v = λf

Objetivos:
----------
1. Representar propagación de ondas.
2. Comprender el comportamiento espacial.
3. Observar movimiento periódico.
4. Base para interferencia y difracción.

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

# Amplitud de la onda
AMPLITUD = 1

# Longitud de onda
LONGITUD_ONDA = 2

# Frecuencia
FRECUENCIA = 1

# Fase inicial
FASE = 0


# =====================================================
# MAGNITUDES DERIVADAS
# =====================================================

# Número de onda
k = (2 * np.pi) / LONGITUD_ONDA

# Frecuencia angular
omega = 2 * np.pi * FRECUENCIA

# Velocidad de propagación
velocidad = LONGITUD_ONDA * FRECUENCIA


# =====================================================
# DOMINIO ESPACIAL
# =====================================================

# Espacio en el eje X
x = np.linspace(0, 10, 1000)


# =====================================================
# ECUACIÓN DE LA ONDA VIAJERA
# =====================================================

def onda_viajera(x, t):
    """
    Calcula la amplitud de la onda
    para una posición y tiempo dados.

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

    return AMPLITUD * np.cos(k * x - omega * t + FASE)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

# Configuración visual
eje.set_title("Onda Viajera")
eje.set_xlabel("Posición (m)")
eje.set_ylabel("Amplitud")

# Límites
eje.set_xlim(0, 10)
eje.set_ylim(-1.5, 1.5)

# Cuadrícula
eje.grid(True)


# =====================================================
# OBJETO GRÁFICO
# =====================================================

linea, = eje.plot([], [], lw=2)


# =====================================================
# FUNCIÓN DE INICIALIZACIÓN
# =====================================================

def inicializar():
    """
    Inicializa la línea de la animación.
    """

    linea.set_data([], [])

    return linea,


# =====================================================
# FUNCIÓN DE ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza la onda en cada frame.

    Parámetros:
    -----------
    frame : int
        Número de frame actual
    """

    # Tiempo actual
    t = frame / 50

    # Calcular amplitud
    y = onda_viajera(x, t)

    # Actualizar línea
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