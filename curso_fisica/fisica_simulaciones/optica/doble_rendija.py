"""
=========================================================
DOBLE RENDIJA DE YOUNG
=========================================================

Ecuación principal:

    I = 4I0 cos²(δ / 2)

Desfase:

    δ = kΔr

Descripción:
------------
Simulación del experimento de doble rendija
de Young.

Dos fuentes coherentes generan un patrón
de interferencia sobre una pantalla.

Conceptos físicos:
------------------
- interferencia
- coherencia
- intensidad luminosa
- franjas brillantes y oscuras

Objetivos:
----------
1. Visualizar interferencia luminosa.
2. Representar intensidad óptica.
3. Comprender el experimento de Young.
4. Base de óptica y mecánica cuántica.

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
d = 2

# Número de onda
k = (2 * np.pi) / LONGITUD_ONDA


# =====================================================
# PANTALLA DE OBSERVACIÓN
# =====================================================

# Coordenadas sobre la pantalla
x = np.linspace(-20, 20, 5000)


# =====================================================
# DIFERENCIA DE CAMINO
# =====================================================

# Aproximación geométrica
delta_r = d * np.sin(x / 20)


# =====================================================
# DESFASE
# =====================================================

delta = k * delta_r


# =====================================================
# INTENSIDAD DEL PATRÓN
# =====================================================

def intensidad(delta):
    """
    Calcula la intensidad luminosa.

    Parámetros:
    -----------
    delta : ndarray
        Desfase

    Retorna:
    --------
    ndarray
        Intensidad óptica
    """

    return 4 * I0 * (np.cos(delta / 2) ** 2)


# =====================================================
# CÁLCULO DE INTENSIDAD
# =====================================================

I = intensidad(delta)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

# Configuración visual
eje.set_title("Patrón de Interferencia - Doble Rendija")

eje.set_xlabel("Posición sobre la pantalla")
eje.set_ylabel("Intensidad luminosa")

# Cuadrícula
eje.grid(True)


# =====================================================
# GRAFICAR PATRÓN
# =====================================================

eje.plot(x, I, linewidth=2)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()