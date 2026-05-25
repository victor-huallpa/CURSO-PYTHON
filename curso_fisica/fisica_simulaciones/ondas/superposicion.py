"""
=========================================================
SUPERPOSICIÓN DE ONDAS
=========================================================

Ecuación principal:

    y_R(x,t) = y_1(x,t) + y_2(x,t)

Descripción:
------------
Simulación de la superposición de dos ondas
viajeras propagándose simultáneamente.

La superposición permite observar:

- interferencia constructiva
- interferencia destructiva
- formación de patrones ondulatorios

Objetivos:
----------
1. Comprender la suma de ondas.
2. Visualizar interferencia.
3. Base para ondas estacionarias.
4. Base para doble rendija.

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
# PARÁMETROS DE LA PRIMERA ONDA
# =====================================================

AMPLITUD_1 = 1
LONGITUD_ONDA_1 = 2
FRECUENCIA_1 = 1
FASE_1 = 0

# Número de onda
k1 = (2 * np.pi) / LONGITUD_ONDA_1

# Frecuencia angular
omega1 = 2 * np.pi * FRECUENCIA_1


# =====================================================
# PARÁMETROS DE LA SEGUNDA ONDA
# =====================================================

AMPLITUD_2 = 1
LONGITUD_ONDA_2 = 2
FRECUENCIA_2 = 1
FASE_2 = np.pi / 2

# Número de onda
k2 = (2 * np.pi) / LONGITUD_ONDA_2

# Frecuencia angular
omega2 = 2 * np.pi * FRECUENCIA_2


# =====================================================
# DOMINIO ESPACIAL
# =====================================================

x = np.linspace(0, 10, 1000)


# =====================================================
# DEFINICIÓN DE LA PRIMERA ONDA
# =====================================================

def onda_1(x, t):
    """
    Primera onda viajera.
    """

    return AMPLITUD_1 * np.cos(k1 * x - omega1 * t + FASE_1)


# =====================================================
# DEFINICIÓN DE LA SEGUNDA ONDA
# =====================================================

def onda_2(x, t):
    """
    Segunda onda viajera.
    """

    return AMPLITUD_2 * np.cos(k2 * x - omega2 * t + FASE_2)


# =====================================================
# SUPERPOSICIÓN DE ONDAS
# =====================================================

def onda_resultante(x, t):
    """
    Suma de ambas ondas.
    """

    return onda_1(x, t) + onda_2(x, t)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 6))

# Configuración visual
eje.set_title("Superposición de Ondas")
eje.set_xlabel("Posición (m)")
eje.set_ylabel("Amplitud")

# Límites
eje.set_xlim(0, 10)
eje.set_ylim(-3, 3)

# Cuadrícula
eje.grid(True)


# =====================================================
# OBJETOS GRÁFICOS
# =====================================================

# Primera onda
linea_1, = eje.plot([], [], label="Onda 1")

# Segunda onda
linea_2, = eje.plot([], [], label="Onda 2")

# Onda resultante
linea_resultante, = eje.plot([], [], lw=3, label="Superposición")

# Mostrar leyenda
eje.legend()


# =====================================================
# FUNCIÓN DE INICIALIZACIÓN
# =====================================================

def inicializar():
    """
    Inicializa las líneas de la animación.
    """

    linea_1.set_data([], [])
    linea_2.set_data([], [])
    linea_resultante.set_data([], [])

    return linea_1, linea_2, linea_resultante


# =====================================================
# FUNCIÓN DE ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza las ondas frame por frame.
    """

    # Tiempo actual
    t = frame / 50

    # Calcular ondas
    y1 = onda_1(x, t)
    y2 = onda_2(x, t)

    # Superposición
    y_total = onda_resultante(x, t)

    # Actualizar gráficas
    linea_1.set_data(x, y1)
    linea_2.set_data(x, y2)
    linea_resultante.set_data(x, y_total)

    return linea_1, linea_2, linea_resultante


# =====================================================
# CREACIÓN DE LA ANIMACIÓN
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