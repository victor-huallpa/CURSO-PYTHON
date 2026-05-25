"""
=========================================================
DIFRACCIÓN DE FRAUNHOFER
=========================================================

Ecuación principal:

    I = I0 (sin(β)/β)^2

Parámetro:

    β = (ka sin(θ)) / 2

Descripción:
------------
Simulación del patrón de difracción producido
por una única rendija.

La luz atraviesa una abertura y se difracta,
generando un patrón característico de intensidad.

Conceptos físicos:
------------------
- difracción
- interferencia continua
- máximos secundarios
- envolvente de intensidad

Objetivos:
----------
1. Visualizar difracción.
2. Comprender propagación ondulatoria.
3. Introducir óptica avanzada.
4. Base para patrón combinado.

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
# PARÁMETROS FÍSICOS
# =====================================================

# Intensidad máxima
I0 = 1

# Longitud de onda
LONGITUD_ONDA = 0.5

# Ancho de la rendija
a = 1

# Número de onda
k = (2 * np.pi) / LONGITUD_ONDA


# =====================================================
# ÁNGULOS DE OBSERVACIÓN
# =====================================================

# Evitar extremos muy grandes
theta = np.linspace(-0.5, 0.5, 5000)


# =====================================================
# PARÁMETRO BETA
# =====================================================

beta = (k * a * np.sin(theta)) / 2


# =====================================================
# EVITAR DIVISIÓN ENTRE CERO
# =====================================================

# Reemplazar beta = 0 por un valor pequeño
beta = np.where(beta == 0, 1e-10, beta)


# =====================================================
# ECUACIÓN DE INTENSIDAD
# =====================================================

def intensidad(beta):
    """
    Calcula la intensidad del patrón
    de difracción.

    Parámetros:
    -----------
    beta : ndarray
        Parámetro beta

    Retorna:
    --------
    ndarray
        Intensidad luminosa
    """

    return I0 * ((np.sin(beta) / beta) ** 2)


# =====================================================
# CÁLCULO DE INTENSIDAD
# =====================================================

I = intensidad(beta)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

# Configuración visual
eje.set_title("Difracción de Fraunhofer")

eje.set_xlabel("Ángulo θ (rad)")
eje.set_ylabel("Intensidad")

# Cuadrícula
eje.grid(True)


# =====================================================
# GRAFICAR PATRÓN
# =====================================================

eje.plot(theta, I, linewidth=2)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()