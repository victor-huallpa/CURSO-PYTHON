"""
=========================================================
EFECTO FOTOELÉCTRICO
=========================================================

Ecuaciones principales:

    hf = W + K

    Kmax = hf - W

Descripción:
------------
Simulación del efecto fotoeléctrico.

Cuando la luz incide sobre un metal,
los electrones pueden ser expulsados
si la frecuencia es suficientemente alta.

Conceptos físicos:
------------------
- fotones
- energía cuantizada
- frecuencia umbral
- función de trabajo
- energía cinética

Objetivos:
----------
1. Comprender el efecto fotoeléctrico.
2. Relacionar frecuencia y energía.
3. Introducir frecuencia umbral.
4. Validar el modelo cuántico.

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

# Constante de Planck (J·s)
h = 6.626e-34

# Función de trabajo del metal (J)
W = 2.2e-19


# =====================================================
# FRECUENCIAS
# =====================================================

# Rango de frecuencias
frecuencia = np.linspace(1e13, 2e15, 2000)


# =====================================================
# ENERGÍA CINÉTICA MÁXIMA
# =====================================================

def energia_cinetica(f):
    """
    Calcula la energía cinética máxima
    de los electrones emitidos.

    Parámetros:
    -----------
    f : ndarray
        Frecuencia de la luz

    Retorna:
    --------
    ndarray
        Energía cinética máxima
    """

    return (h * f) - W


# =====================================================
# CÁLCULO DE ENERGÍA
# =====================================================

K = energia_cinetica(frecuencia)


# =====================================================
# ELIMINAR VALORES NEGATIVOS
# =====================================================

# Si la energía es negativa,
# no se emiten electrones.
K = np.where(K < 0, 0, K)


# =====================================================
# FRECUENCIA UMBRAL
# =====================================================

frecuencia_umbral = W / h


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(10, 5))

# Configuración visual
eje.set_title("Efecto Fotoeléctrico")

eje.set_xlabel("Frecuencia (Hz)")
eje.set_ylabel("Energía Cinética Máxima (J)")

# Cuadrícula
eje.grid(True)


# =====================================================
# GRAFICAR ENERGÍA
# =====================================================

eje.plot(
    frecuencia,
    K,
    linewidth=2,
    label="Energía cinética"
)


# =====================================================
# MARCAR FRECUENCIA UMBRAL
# =====================================================

eje.axvline(
    frecuencia_umbral,
    linestyle="--",
    label="Frecuencia umbral"
)


# =====================================================
# LEYENDA
# =====================================================

eje.legend()


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()