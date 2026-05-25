"""
=========================================================
INTERFERENCIA DE ONDAS
=========================================================

Descripción:
------------
Simulación de interferencia entre dos fuentes
emisoras de ondas.

Se representan:

- interferencia constructiva
- interferencia destructiva
- franjas de interferencia

Conceptos físicos:
------------------
Constructiva:
Δr = nλ

Destructiva:
Δr = (n + 1/2)λ

Objetivos:
----------
1. Comprender interferencia.
2. Visualizar patrones espaciales.
3. Base para doble rendija.
4. Introducir óptica ondulatoria.

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

# Amplitud de las ondas
AMPLITUD = 1

# Longitud de onda
LONGITUD_ONDA = 1

# Frecuencia
FRECUENCIA = 1

# Frecuencia angular
omega = 2 * np.pi * FRECUENCIA

# Número de onda
k = (2 * np.pi) / LONGITUD_ONDA


# =====================================================
# POSICIÓN DE LAS FUENTES
# =====================================================

fuente_1 = (-2, 0)
fuente_2 = (2, 0)


# =====================================================
# MALLA ESPACIAL 2D
# =====================================================

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

X, Y = np.meshgrid(x, y)


# =====================================================
# DISTANCIAS A CADA FUENTE
# =====================================================

r1 = np.sqrt((X - fuente_1[0])**2 + (Y - fuente_1[1])**2)

r2 = np.sqrt((X - fuente_2[0])**2 + (Y - fuente_2[1])**2)


# =====================================================
# ECUACIONES DE ONDA
# =====================================================

def onda(r, t):
    """
    Calcula una onda circular.

    Parámetros:
    -----------
    r : ndarray
        Distancia radial

    t : float
        Tiempo

    Retorna:
    --------
    ndarray
        Amplitud de la onda
    """

    return AMPLITUD * np.cos(k * r - omega * t)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(8, 8))

eje.set_title("Interferencia de Ondas")

eje.set_xlabel("Posición X")
eje.set_ylabel("Posición Y")


# =====================================================
# FUNCIÓN DE ANIMACIÓN
# =====================================================

def animar(frame):
    """
    Actualiza el patrón de interferencia.
    """

    eje.clear()

    # Tiempo actual
    t = frame / 20

    # Ondas individuales
    onda_1 = onda(r1, t)
    onda_2 = onda(r2, t)

    # Superposición
    interferencia = onda_1 + onda_2

    # Mapa de colores
    grafica = eje.imshow(
        interferencia,
        extent=[-10, 10, -10, 10],
        origin="lower",
        cmap="viridis",
        animated=True
    )

    # Dibujar fuentes
    eje.plot(fuente_1[0], fuente_1[1], 'ro')
    eje.plot(fuente_2[0], fuente_2[1], 'ro')

    # Etiquetas
    eje.set_title("Interferencia Constructiva y Destructiva")

    eixo_x = "Posición X"
    eixo_y = "Posición Y"

    eje.set_xlabel(eixo_x)
    eje.set_ylabel(eixo_y)

    return [grafica]


# =====================================================
# CREACIÓN DE ANIMACIÓN
# =====================================================

animacion = FuncAnimation(
    figura,
    animar,
    frames=300,
    interval=30,
    blit=True
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()