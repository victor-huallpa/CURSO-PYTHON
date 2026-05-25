"""
=========================================================
MODELO DE BOHR
=========================================================

Ecuaciones principales:

    r_n = a0 * n²

    E_n = E0 / n²

Descripción:
------------
Simulación de los niveles electrónicos
cuantizados del átomo de hidrógeno
según el modelo de Bohr.

Conceptos físicos:
------------------
- cuantización orbital
- niveles de energía
- órbitas permitidas
- átomo de hidrógeno

Objetivos:
----------
1. Visualizar órbitas electrónicas.
2. Comprender cuantización.
3. Representar niveles energéticos.
4. Base para transiciones electrónicas.

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
# CONSTANTES FÍSICAS
# =====================================================

# Radio de Bohr (m)
a0 = 5.29e-11

# Energía base (eV)
E0 = -13.6


# =====================================================
# NIVELES CUÁNTICOS
# =====================================================

# Niveles principales
niveles = np.arange(1, 7)


# =====================================================
# RADIO DE BOHR
# =====================================================

def radio_bohr(n):
    """
    Calcula el radio permitido
    para un nivel cuántico.

    Parámetros:
    -----------
    n : int o ndarray
        Número cuántico principal

    Retorna:
    --------
    ndarray
        Radio orbital
    """

    return a0 * (n ** 2)


# =====================================================
# ENERGÍA CUANTIZADA
# =====================================================

def energia_bohr(n):
    """
    Calcula la energía del nivel.

    Parámetros:
    -----------
    n : int o ndarray
        Número cuántico principal

    Retorna:
    --------
    ndarray
        Energía del nivel
    """

    return E0 / (n ** 2)


# =====================================================
# CÁLCULO DE RADIOS Y ENERGÍAS
# =====================================================

radios = radio_bohr(niveles)

energias = energia_bohr(niveles)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, (eje_1, eje_2) = plt.subplots(
    1,
    2,
    figsize=(14, 6)
)


# =====================================================
# SUBGRÁFICA 1:
# ÓRBITAS DE BOHR
# =====================================================

eje_1.set_title("Órbitas Cuantizadas")

# Dibujar órbitas
for i, radio in enumerate(radios):

    circulo = plt.Circle(
        (0, 0),
        radio / a0,
        fill=False
    )

    eje_1.add_patch(circulo)

    # Etiqueta del nivel
    eje_1.text(
        radio / a0,
        0,
        f"n={i+1}"
    )

# Núcleo
eje_1.plot(0, 0, 'ro', markersize=10)

# Configuración visual
eje_1.set_xlim(-40, 40)
eje_1.set_ylim(-40, 40)

eje_1.set_aspect("equal")

eje_1.grid(True)


# =====================================================
# SUBGRÁFICA 2:
# NIVELES DE ENERGÍA
# =====================================================

eje_2.set_title("Niveles de Energía")

for i, energia in enumerate(energias):

    eje_2.hlines(
        energia,
        0,
        1,
        linewidth=3
    )

    eixo_texto = 1.05

    eje_2.text(
        eixo_texto,
        energia,
        f"n={i+1}"
    )

# Configuración visual
eje_2.set_xlabel("Estado")

eje_2.set_ylabel("Energía (eV)")

eje_2.set_xlim(0, 1.5)

eje_2.grid(True)


# =====================================================
# AJUSTAR ESPACIADO
# =====================================================

plt.tight_layout()


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()