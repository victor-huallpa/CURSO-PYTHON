"""
=========================================================
ONDAS ESTACIONARIAS DEL ELECTRÓN
=========================================================

Ecuación principal:

    2πr = nλ

Descripción:
------------
Simulación del comportamiento ondulatorio
del electrón alrededor del núcleo.

La órbita electrónica solo es estable
cuando la onda se ajusta exactamente
sobre la circunferencia orbital.

Conceptos físicos:
------------------
- ondas estacionarias
- cuantización
- interferencia constructiva
- dualidad onda-partícula

Objetivos:
----------
1. Visualizar ondas electrónicas.
2. Comprender cuantización orbital.
3. Relacionar Bohr y De Broglie.
4. Introducir mecánica cuántica.

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
# PARÁMETROS CUÁNTICOS
# =====================================================

# Número cuántico principal
n = 4

# Radio orbital arbitrario
radio = 5


# =====================================================
# ÁNGULO POLAR
# =====================================================

theta = np.linspace(
    0,
    2 * np.pi,
    2000
)


# =====================================================
# ONDA ESTACIONARIA
# =====================================================

def onda_estacionaria(theta, n):
    """
    Calcula la amplitud de la onda
    electrónica sobre la órbita.

    Parámetros:
    -----------
    theta : ndarray
        Ángulo polar

    n : int
        Número cuántico

    Retorna:
    --------
    ndarray
        Amplitud ondulatoria
    """

    return np.sin(n * theta)


# =====================================================
# CÁLCULO DE AMPLITUD
# =====================================================

amplitud = onda_estacionaria(theta, n)


# =====================================================
# MODIFICAR RADIO SEGÚN LA ONDA
# =====================================================

# La amplitud modifica ligeramente el radio
radio_modulado = radio + 0.5 * amplitud


# =====================================================
# COORDENADAS POLARES
# =====================================================

x = radio_modulado * np.cos(theta)

y = radio_modulado * np.sin(theta)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(8, 8))

eje.set_title(
    "Ondas Estacionarias del Electrón"
)


# =====================================================
# DIBUJAR NÚCLEO
# =====================================================

eje.plot(
    0,
    0,
    'ro',
    markersize=10,
    label="Núcleo"
)


# =====================================================
# DIBUJAR ÓRBITA ONDULATORIA
# =====================================================

eje.plot(
    x,
    y,
    linewidth=2,
    label=f"n = {n}"
)


# =====================================================
# CONFIGURACIÓN VISUAL
# =====================================================

eje.set_aspect("equal")

eje.grid(True)

eje.legend()


# =====================================================
# ETIQUETAS
# =====================================================

eje.set_xlabel("Posición X")

eje.set_ylabel("Posición Y")


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()