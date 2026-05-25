"""
=========================================================
OPERADOR MOMENTO
=========================================================

Ecuación principal:

    p̂ = -iħ ∂/∂x

Descripción:
------------
Simulación del operador momento
actuando sobre una función de onda.

Se utiliza una onda plana cuántica
para visualizar el efecto del operador.

Conceptos físicos:
------------------
- operadores cuánticos
- derivadas espaciales
- momento lineal
- observables

Objetivos:
----------
1. Introducir operadores cuánticos.
2. Comprender derivadas físicas.
3. Relacionar momento y ondas.
4. Visualizar acción operatoria.

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

hbar = 1


# =====================================================
# ESPACIO
# =====================================================

x = np.linspace(
    -10,
    10,
    3000
)

dx = x[1] - x[0]


# =====================================================
# PARÁMETROS DE LA ONDA
# =====================================================

A = 1

k = 4


# =====================================================
# FUNCIÓN DE ONDA
# =====================================================

psi = A * np.exp(
    1j * k * x
)


# =====================================================
# OPERADOR MOMENTO
# =====================================================

def operador_momento(psi, dx):
    """
    Aplica el operador momento
    usando derivada numérica.

    Parámetros:
    -----------
    psi : ndarray
        Función de onda

    dx : float
        Paso espacial

    Retorna:
    --------
    ndarray
        Resultado operatorio
    """

    derivada = np.gradient(
        psi,
        dx
    )

    return -1j * hbar * derivada


# =====================================================
# APLICAR OPERADOR
# =====================================================

resultado = operador_momento(
    psi,
    dx
)


# =====================================================
# PARTE REAL DEL RESULTADO
# =====================================================

resultado_real = np.real(resultado)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title(
    "Operador Momento sobre una Onda"
)

eje.set_xlabel("Posición x")

eje.set_ylabel("Amplitud")


# =====================================================
# CUADRÍCULA
# =====================================================

eje.grid(True)


# =====================================================
# FUNCIÓN ORIGINAL
# =====================================================

eje.plot(
    x,
    np.real(psi),
    label="Re(ψ)",
    linewidth=2
)


# =====================================================
# RESULTADO DEL OPERADOR
# =====================================================

eje.plot(
    x,
    resultado_real,
    linestyle="--",
    linewidth=2,
    label="p̂ψ"
)


# =====================================================
# LEYENDA
# =====================================================

eje.legend()


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()