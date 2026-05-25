"""
=========================================================
OPERADOR ENERGÍA
=========================================================

Ecuación principal:

    Ê = iħ ∂/∂t

Descripción:
------------
Simulación del operador energía
aplicado sobre una función de onda
dependiente del tiempo.

Se utiliza una onda plana cuántica
para visualizar la acción temporal
del operador.

Conceptos físicos:
------------------
- operador energía
- derivadas temporales
- evolución cuántica
- Hamiltoniano

Objetivos:
----------
1. Comprender energía cuántica.
2. Relacionar tiempo y energía.
3. Visualizar operadores temporales.
4. Completar operadores básicos.

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


# =====================================================
# TIEMPO
# =====================================================

t = np.linspace(
    0,
    10,
    2000
)

dt = t[1] - t[0]


# =====================================================
# PARÁMETROS DE LA ONDA
# =====================================================

A = 1

k = 3

omega = 5


# =====================================================
# FUNCIÓN DE ONDA TEMPORAL
# =====================================================

def funcion_onda(t):
    """
    Construye función de onda
    dependiente del tiempo.

    Parámetros:
    -----------
    t : ndarray
        Tiempo

    Retorna:
    --------
    ndarray
        Función de onda compleja
    """

    return A * np.exp(
        -1j * omega * t
    )


# =====================================================
# FUNCIÓN DE ONDA
# =====================================================

psi_t = funcion_onda(t)


# =====================================================
# OPERADOR ENERGÍA
# =====================================================

def operador_energia(psi, dt):
    """
    Aplica el operador energía.

    Parámetros:
    -----------
    psi : ndarray
        Función de onda temporal

    dt : float
        Paso temporal

    Retorna:
    --------
    ndarray
        Resultado operatorio
    """

    derivada_tiempo = np.gradient(
        psi,
        dt
    )

    return 1j * hbar * derivada_tiempo


# =====================================================
# APLICAR OPERADOR
# =====================================================

resultado = operador_energia(
    psi_t,
    dt
)


# =====================================================
# PARTE REAL
# =====================================================

parte_real_onda = np.real(psi_t)

parte_real_resultado = np.real(resultado)


# =====================================================
# CREACIÓN DE FIGURA
# =====================================================

figura, eje = plt.subplots(figsize=(12, 5))

eje.set_title(
    "Operador Energía sobre una Onda"
)

eje.set_xlabel("Tiempo")

eje.set_ylabel("Amplitud")


# =====================================================
# CUADRÍCULA
# =====================================================

eje.grid(True)


# =====================================================
# FUNCIÓN DE ONDA ORIGINAL
# =====================================================

eje.plot(
    t,
    parte_real_onda,
    linewidth=2,
    label="Re(ψ)"
)


# =====================================================
# RESULTADO DEL OPERADOR
# =====================================================

eje.plot(
    t,
    parte_real_resultado,
    linestyle="--",
    linewidth=2,
    label="Êψ"
)


# =====================================================
# LEYENDA
# =====================================================

eje.legend()


# =====================================================
# MOSTRAR RESULTADO
# =====================================================

plt.show()