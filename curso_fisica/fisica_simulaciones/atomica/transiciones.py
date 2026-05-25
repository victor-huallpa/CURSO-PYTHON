"""
=========================================================
TRANSICIONES ELECTRÓNICAS
=========================================================

Ecuación principal:

    hf = Ei - Ef

Descripción:
------------
Simulación de transiciones electrónicas
entre niveles de energía del átomo
de hidrógeno.

Cuando el electrón cambia de nivel:

- emite un fotón
- o absorbe un fotón

Conceptos físicos:
------------------
- emisión
- absorción
- niveles cuánticos
- espectros atómicos

Objetivos:
----------
1. Comprender transiciones electrónicas.
2. Relacionar energía y fotones.
3. Introducir espectros atómicos.
4. Base para la fórmula de Rydberg.

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
# CONSTANTES
# =====================================================

# Energía base del hidrógeno (eV)
E0 = -13.6


# =====================================================
# NIVELES CUÁNTICOS
# =====================================================

niveles = np.arange(1, 7)


# =====================================================
# ENERGÍA CUANTIZADA
# =====================================================

def energia_nivel(n):
    """
    Calcula la energía de un nivel.

    Parámetros:
    -----------
    n : int
        Nivel cuántico principal

    Retorna:
    --------
    float
        Energía del nivel
    """

    return E0 / (n ** 2)


# =====================================================
# CALCULAR ENERGÍAS
# =====================================================

energias = [energia_nivel(n) for n in niveles]


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(8, 6))

eje.set_title("Transiciones Electrónicas")

eje.set_xlabel("Estado")

eje.set_ylabel("Energía (eV)")


# =====================================================
# DIBUJAR NIVELES DE ENERGÍA
# =====================================================

for i, energia in enumerate(energias):

    eje.hlines(
        energia,
        0,
        1,
        linewidth=3
    )

    eixo_texto = 1.05

    eje.text(
        eixo_texto,
        energia,
        f"n={i+1}"
    )


# =====================================================
# TRANSICIONES ELECTRÓNICAS
# =====================================================

# Lista de transiciones:
# (nivel inicial, nivel final)

transiciones = [
    (5, 2),
    (4, 2),
    (3, 2),
    (2, 1)
]


# =====================================================
# DIBUJAR FLECHAS
# =====================================================

for inicial, final in transiciones:

    Ei = energia_nivel(inicial)

    Ef = energia_nivel(final)

    # Flecha de transición
    eje.annotate(
        "",
        xy=(0.5, Ef),
        xytext=(0.5, Ei),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2
        )
    )

    # Energía emitida
    delta_E = Ei - Ef

    # Texto descriptivo
    eje.text(
        0.55,
        (Ei + Ef) / 2,
        f"ΔE = {abs(delta_E):.2f} eV"
    )


# =====================================================
# CONFIGURACIÓN VISUAL
# =====================================================

eje.set_xlim(0, 1.5)

eje.grid(True)


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()