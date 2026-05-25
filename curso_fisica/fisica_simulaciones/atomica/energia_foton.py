"""
=========================================================
ENERGÍA DEL FOTÓN
=========================================================

Ecuación principal:

    E = hf

Descripción:
------------
Simulación de la relación entre:

- frecuencia
- energía del fotón

La energía aumenta linealmente con la frecuencia.

Conceptos físicos:
------------------
- cuantización
- fotones
- energía electromagnética
- constante de Planck

Objetivos:
----------
1. Comprender cuantización de energía.
2. Relacionar frecuencia y energía.
3. Introducir física cuántica.
4. Base para efecto fotoeléctrico.

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
# CONSTANTE DE PLANCK
# =====================================================

# Constante de Planck (J·s)
h = 6.626e-34


# =====================================================
# FRECUENCIAS
# =====================================================

# Rango de frecuencias
frecuencia = np.linspace(1e13, 1e15, 1000)


# =====================================================
# ECUACIÓN DE ENERGÍA
# =====================================================

def energia_foton(f):
    """
    Calcula la energía de un fotón.

    Parámetros:
    -----------
    f : ndarray
        Frecuencia

    Retorna:
    --------
    ndarray
        Energía del fotón
    """

    return h * f


# =====================================================
# CÁLCULO DE ENERGÍA
# =====================================================

energia = energia_foton(frecuencia)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(10, 5))

# Configuración visual
eje.set_title("Energía del Fotón")

eje.set_xlabel("Frecuencia (Hz)")
eje.set_ylabel("Energía (Joules)")

# Cuadrícula
eje.grid(True)


# =====================================================
# GRAFICAR RELACIÓN
# =====================================================

eje.plot(
    frecuencia,
    energia,
    linewidth=2
)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()