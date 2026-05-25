"""
=========================================================
MOVIMIENTO ARMÓNICO SIMPLE (MAS)
=========================================================

Ecuación:

    x(t) = A * cos(ωt + φ)

Descripción:
------------
Simulación gráfica del Movimiento Armónico Simple.

Una partícula oscila periódicamente alrededor
de una posición de equilibrio siguiendo una
función sinusoidal.

Variables físicas:
------------------
A  -> amplitud
ω  -> frecuencia angular
φ  -> fase inicial
t  -> tiempo

Objetivos de esta simulación:
-----------------------------
1. Representar gráficamente la oscilación.
2. Comprender el comportamiento periódico.
3. Servir como base para simulaciones futuras.

Librerías utilizadas:
---------------------
numpy      -> cálculo numérico
matplotlib -> gráficas y animaciones
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

# Amplitud máxima de oscilación
AMPLITUD = 1.0

# Frecuencia en Hz
FRECUENCIA = 1.0

# Frecuencia angular:
# ω = 2πf
omega = 2 * np.pi * FRECUENCIA

# Fase inicial
FASE = 0

# Tiempo máximo de simulación
TIEMPO_MAXIMO = 10

# Cantidad de muestras temporales
MUESTRAS = 1000


# =====================================================
# DOMINIO TEMPORAL
# =====================================================

# Genera valores de tiempo entre 0 y TIEMPO_MAXIMO
tiempo = np.linspace(0, TIEMPO_MAXIMO, MUESTRAS)


# =====================================================
# ECUACIÓN DEL MOVIMIENTO ARMÓNICO SIMPLE
# =====================================================

def movimiento_armonico(t):
    """
    Calcula la posición de la partícula
    para un tiempo dado.

    Parámetros:
    -----------
    t : float o ndarray
        Tiempo

    Retorna:
    --------
    x : float o ndarray
        Posición de la partícula
    """

    return AMPLITUD * np.cos(omega * t + FASE)


# =====================================================
# CÁLCULO DE POSICIONES
# =====================================================

# Calcula todas las posiciones de la partícula
posicion = movimiento_armonico(tiempo)


# =====================================================
# CREACIÓN DE LA FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(10, 5))

# Configuración visual
eje.set_title("Movimiento Armónico Simple")
eje.set_xlabel("Tiempo (s)")
eje.set_ylabel("Posición (m)")

# Límites de la gráfica
eje.set_xlim(0, TIEMPO_MAXIMO)
eje.set_ylim(-1.2 * AMPLITUD, 1.2 * AMPLITUD)

# Cuadrícula
eje.grid(True)


# =====================================================
# OBJETOS GRÁFICOS
# =====================================================

# Línea principal de la onda
linea, = eje.plot([], [], lw=2)

# Punto móvil que representa la partícula
particula, = eje.plot([], [], 'ro')


# =====================================================
# FUNCIÓN DE INICIALIZACIÓN
# =====================================================

def inicializar():
    """
    Inicializa los elementos gráficos.
    """

    linea.set_data([], [])
    particula.set_data([], [])

    return linea, particula


# =====================================================
# FUNCIÓN DE ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza la animación frame por frame.

    Parámetros:
    -----------
    frame : int
        Índice del frame actual
    """

    # Datos hasta el frame actual
    x_datos = tiempo[:frame]
    y_datos = posicion[:frame]

    # Actualizar línea
    linea.set_data(x_datos, y_datos)

    # Actualizar partícula
    particula.set_data([tiempo[frame]], [posicion[frame]])

    return linea, particula


# =====================================================
# CREACIÓN DE LA ANIMACIÓN
# =====================================================

animacion = FuncAnimation(
    figura,
    animar,
    frames=len(tiempo),
    init_func=inicializar,
    interval=10,
    blit=True
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()