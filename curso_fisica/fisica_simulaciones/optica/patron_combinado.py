"""
=========================================================
PATRÓN COMBINADO:
INTERFERENCIA + DIFRACCIÓN
=========================================================

Ecuación principal:

    I = I0 (sin(β)/β)^2 cos²(α)

Parámetros:

    β = (ka sin(θ)) / 2

    α = (kd sin(θ)) / 2

Descripción:
------------
Simulación del patrón completo generado
por una doble rendija real.

El patrón observado combina:

1. Interferencia entre rendijas
2. Difracción individual de cada rendija

Conceptos físicos:
------------------
- interferencia
- difracción
- intensidad óptica
- envolvente de difracción

Objetivos:
----------
1. Visualizar patrón óptico real.
2. Combinar interferencia y difracción.
3. Comprender experimentos reales.
4. Base para óptica moderna.

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

# Separación entre rendijas
d = 4

# Ancho de cada rendija
a = 1

# Número de onda
k = (2 * np.pi) / LONGITUD_ONDA


# =====================================================
# ÁNGULOS DE OBSERVACIÓN
# =====================================================

theta = np.linspace(-0.5, 0.5, 5000)


# =====================================================
# PARÁMETRO BETA
# =====================================================

beta = (k * a * np.sin(theta)) / 2


# =====================================================
# PARÁMETRO ALPHA
# =====================================================

alpha = (k * d * np.sin(theta)) / 2


# =====================================================
# EVITAR DIVISIÓN ENTRE CERO
# =====================================================

beta = np.where(beta == 0, 1e-10, beta)


# =====================================================
# ECUACIÓN DE INTENSIDAD
# =====================================================

def intensidad(beta, alpha):
    """
    Calcula el patrón combinado de
    interferencia y difracción.

    Parámetros:
    -----------
    beta : ndarray
        Parámetro de difracción

    alpha : ndarray
        Parámetro de interferencia

    Retorna:
    --------
    ndarray
        Intensidad luminosa
    """

    difraccion = (np.sin(beta) / beta) ** 2

    interferencia = np.cos(alpha) ** 2

    return I0 * difraccion * interferencia


# =====================================================
# CÁLCULO DE INTENSIDAD
# =====================================================

I = intensidad(beta, alpha)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

# Configuración visual
eje.set_title(
    "Patrón Combinado: Interferencia + Difracción"
)

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