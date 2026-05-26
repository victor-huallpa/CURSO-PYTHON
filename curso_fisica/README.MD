# 🔬 Simulaciones Interactivas de Física

Colección completa de simulaciones gráficas interactivas de fenómenos físicos fundamentales, desde mecánica ondulatoria hasta mecánica cuántica, implementadas en Python con visualización Matplotlib.

---

## 📋 Contenido del Proyecto

El proyecto está organizado en **6 módulos temáticos** con simulaciones relacionadas:

### 1. **Ondas** (`ondas/`)
Simulaciones de fenómenos ondulatorios clásicos.

| Simulación | Fenómeno | Ecuación |
|------------|----------|----------|
| `movimiento_armonico.py` | Oscilación sinusoidal | $x(t) = A\cos(\omega t + \phi)$ |
| `onda_viajera.py` | Propagación ondulatoria | $y(x,t) = A\cos(kx - \omega t + \phi)$ |
| `onda_estacionaria.py` | Ondas estacionarias | $y(x,t) = 2A\sin(kx)\cos(\omega t)$ |
| `superposicion.py` | Interferencia entre ondas | $y_R = y_1 + y_2$ |
| `interferencia.py` | Patrones interferométricos | $\Delta r = n\lambda$ |

---

### 2. **Física Atómica** (`atomica/`)
Modelos clásicos y cuánticos del átomo.

| Simulación | Concepto | Ecuación Principal |
|------------|----------|-------------------|
| `modelo_bohr.py` | Órbitas cuantizadas | $r_n = a_0 n^2$, $E_n = -\frac{13.6 \text{ eV}}{n^2}$ |
| `transiciones.py` | Transiciones electrónicas | $\Delta E = hf = h\nu$ |
| `energia_foton.py` | Energía de fotones | $E = h\nu = \frac{hc}{\lambda}$ |
| `efecto_fotoelectrico.py` | Efecto fotoeléctrico | $K_{max} = h\nu - \phi$ |
| `de_broglie.py` | Longitud de onda de De Broglie | $\lambda = \frac{h}{p} = \frac{h}{mv}$ |
| `rydberg.py` | Fórmula de Rydberg | $\frac{1}{\lambda} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$ |
| `ondas_estacionarias_electron.py` | Ondas estacionarias del electrón | Interpretación ondulatoria de Bohr |

---

### 3. **Mecánica Cuántica General** (`cuantica/`)
Conceptos fundamentales de la teoría cuántica.

| Simulación | Tema | Descripción |
|------------|------|-------------|
| `schrodinger.py` | Ecuación de Schrödinger | Evolución temporal de la función de onda |
| `schrodinger_general.py` | Schrödinger generalizada | Ecuación independiente del tiempo |
| `paquete_ondas.py` | Paquete de ondas | Propagación de superposiciones gaussianas |
| `onda_plana.py` | Ondas planas | Eigenfunciones en espacio libre |
| `densidad_probabilidad.py` | Densidad de probabilidad | Interpretación de $\|\psi\|^2$ |
| `operador_momento.py` | Operador momento | $\hat{p} = -i\hbar\frac{\partial}{\partial x}$ |
| `operador_energia.py` | Operador energía | $\hat{E} = i\hbar\frac{\partial}{\partial t}$ |

---

### 4. **Óptica Clásica** (`optica/`)
Fenómenos luminosos y ondulatorios.

| Simulación | Fenómeno | Aplicación |
|------------|----------|-----------|
| `doble_rendija.py` | Experimento de Young | Interferencia de luz |
| `difraccion.py` | Difracción de Fraunhofer | Patrón de intensidad |
| `patron_combinado.py` | Difracción e interferencia | Combinación de efectos |

---

### 5. **Utilidades** (`utilidades/`)
Herramientas y constantes compartidas.

| Módulo | Contenido |
|--------|----------|
| `constantes.py` | Constantes físicas fundamentales (h, ħ, c, e, m_e, etc.) |
| `graficador.py` | Funciones para visualización y animación de datos |

---

### 6. **Videos** (`videos/`)
Almacenamiento para animaciones y videos generados.

---

## 🛠️ Instalación y Configuración

### Requisitos
- Python 3.8+
- pip (gestor de paquetes)

### Dependencias Principales
- **matplotlib**: Visualización gráfica
- **numpy**: Computación numérica
- **scipy**: Algoritmos científicos
- **jupyter**: Notebooks interactivos
- **celluloid**: Generación de animaciones

### Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd /var/www/html/PYTHON/python-cursos/curso_fisica
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   venv\Scripts\activate  # Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Uso

### Ejecutar una simulación individual
```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar simulación
python fisica_simulaciones/ondas/movimiento_armonico.py
python fisica_simulaciones/atomica/modelo_bohr.py
python fisica_simulaciones/cuantica/schrodinger.py
# etc.
```

### Estructura de archivos de simulación
Cada simulación sigue un patrón estándar:

```python
"""
Documentación del fenómeno físico
- Ecuaciones matemáticas
- Descripción física
- Conceptos clave
"""

# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from utilidades.constantes import *
from utilidades.graficador import *

# Definir parámetros del sistema
# Realizar cálculos
# Generar visualización
# mostrar/guardar resultados
```

---

## 📊 Ejemplo de Uso

### Movimiento Armónico Simple
```python
python fisica_simulaciones/ondas/movimiento_armonico.py
```
Genera una visualización de la oscilación periódica de una masa en un resorte.

### Modelo de Bohr
```python
python fisica_simulaciones/atomica/modelo_bohr.py
```
Visualiza las órbitas electrónicas permitidas y los niveles de energía del átomo de hidrógeno.

### Ecuación de Schrödinger
```python
python fisica_simulaciones/cuantica/schrodinger.py
```
Simula la evolución temporal de una función de onda gaussiana en espacio libre.

---

## 📚 Conceptos Cubre

### Mecánica Ondulatoria
- Oscilación armónica simple
- Propagación de ondas
- Ondas estacionarias
- Interferencia y difracción
- Superposición

### Física Atómica
- Modelo de Bohr del átomo
- Transiciones electrónicas
- Efecto fotoeléctrico
- Dualidad onda-corpúsculo
- Fórmula de Rydberg

### Mecánica Cuántica
- Función de onda ($\psi$)
- Ecuación de Schrödinger
- Densidad de probabilidad ($|\psi|^2$)
- Paquetes de ondas
- Operadores cuánticos (momento, energía)

### Óptica
- Interferencia luminosa
- Difracción de Fraunhofer
- Experimento de doble rendija
- Parámetros ópticos

---

## 🎯 Objetivos Educativos

Estas simulaciones buscan:

✓ Visualizar conceptos físicos abstractos  
✓ Facilitar la comprensión de ecuaciones matemáticas  
✓ Permitir experimentación interactiva  
✓ Demostrar fenómenos que son difíciles de observar en laboratorio  
✓ Proporcionar una base para análisis más complejos  
✓ Fomentar el aprendizaje experimental

---

## 📁 Estructura Completa del Proyecto

```
curso_fisica/
├── README.MD                          # Este archivo
├── requirements.txt                   # Dependencias Python
├── fisica_simulaciones/
│   ├── main.py
│   ├── ondas/
│   │   ├── movimiento_armonico.py
│   │   ├── onda_viajera.py
│   │   ├── onda_estacionaria.py
│   │   ├── superposicion.py
│   │   └── interferencia.py
│   ├── atomica/
│   │   ├── modelo_bohr.py
│   │   ├── transiciones.py
│   │   ├── energia_foton.py
│   │   ├── efecto_fotoelectrico.py
│   │   ├── de_broglie.py
│   │   ├── rydberg.py
│   │   └── ondas_estacionarias_electron.py
│   ├── cuantica/
│   │   ├── schrodinger.py
│   │   ├── schrodinger_general.py
│   │   ├── paquete_ondas.py
│   │   ├── onda_plana.py
│   │   ├── densidad_probabilidad.py
│   │   ├── operador_momento.py
│   │   └── operador_energia.py
│   ├── optica/
│   │   ├── doble_rendija.py
│   │   ├── difraccion.py
│   │   └── patron_combinado.py
│   ├── utilidades/
│   │   ├── constantes.py
│   │   └── graficador.py
│   ├── graficas/                      # Gráficos generados
│   └── videos/                        # Animaciones generadas
```

---

## 🔧 Constantes Físicas Incluidas

El archivo `utilidades/constantes.py` proporciona:

- $h$ = Constante de Planck
- $\hbar$ = Constante de Planck reducida
- $c$ = Velocidad de la luz
- $e$ = Carga elemental
- $m_e$ = Masa del electrón
- $a_0$ = Radio de Bohr
- $R_H$ = Constante de Rydberg
- Y más...

---

## 📝 Notas sobre Visualización

Todas las simulaciones utilizan **matplotlib** para generar gráficos interactivos que permiten:

- Ver la evolución del sistema en tiempo real
- Guardar imágenes de los resultados
- Generar animaciones con **celluloid**
- Personalizar parámetros (amplitud, frecuencia, tiempo, etc.)

---

## 🤝 Contribuciones

Para agregar nuevas simulaciones:

1. Crear archivo en la carpeta temática correspondiente
2. Incluir documentación con ecuaciones y conceptos
3. Usar las constantes de `utilidades/constantes.py`
4. Implementar visualización con `utilidades/graficador.py`
5. Actualizar este README

---

## 📄 Licencia

Este proyecto es material educativo para cursos de física.

---

## 🎓 Autor

Proyecto de simulaciones didácticas de fenómenos físicos.

---

# 5. INTERFERENCIA DESTRUCTIVA

## Representación gráfica

Mínimos de intensidad.

## Fórmula

```latex id="u8im23"
\Delta r=\left(n+\frac12\right)\lambda
```

---

# 6. ONDA ESTACIONARIA

## Representación gráfica

Nodos y vientres en una cuerda.

## Fórmula principal

```latex id="cwqew4"
y(x,t)=2A\sin(kx)\cos(\omega t)
```

## Longitudes permitidas

```latex id="j1l7bx"
\lambda_n=\frac{2L}{n}
```

---

# 7. DOBLE RENDIJA DE YOUNG

## Representación gráfica

Patrón de interferencia luminosa.

## Ondas emitidas por las rendijas

```latex id="l3v9um"
y_1=A\cos(kx-\omega t)
```

```latex id="13x9i1"
y_2=A\cos(kx-\omega t+\delta)
```

---

## Intensidad del patrón de interferencia

```latex id="r7yyls"
I=4I_0\cos^2\left(\frac{\delta}{2}\right)
```

---

## Desfase

```latex id="tksfjt"
\delta=k\Delta r
```

---

## Número de onda

```latex id="uk1p2k"
k=\frac{2\pi}{\lambda}
```

---

# 8. DIFRACCIÓN DE FRAUNHOFER

## Representación gráfica

Difracción de una sola rendija.

## Intensidad

```latex id="kt0ehx"
I=I_0\left(\frac{\sin\beta}{\beta}\right)^2
```

## Parámetro beta

```latex id="ix6lv7"
\beta=\frac{ka\sin\theta}{2}
```

---

# 9. DOBLE RENDIJA + DIFRACCIÓN

## Representación gráfica

Patrón total observado en pantalla.

## Fórmula principal

```latex id="cb1rfa"
I=I_0\left(\frac{\sin\beta}{\beta}\right)^2\cos^2\alpha
```

## Parámetro alpha

```latex id="66d9wg"
\alpha=\frac{kd\sin\theta}{2}
```

---

# 10. ENERGÍA DEL FOTÓN

## Representación gráfica

Relación energía-frecuencia.

## Fórmula

```latex id="jlwm7u"
E=hf
```

---

# 11. EFECTO FOTOELÉCTRICO

## Representación gráfica

Electrones emitidos según frecuencia.

## Fórmula principal

```latex id="tdptim"
hf=W+K
```

## Energía cinética máxima

```latex id="cx6s2w"
K_{max}=hf-W
```

---

# 12. MODELO DE BOHR

## Representación gráfica

Órbitas electrónicas cuantizadas.

---

## Equilibrio de fuerzas

```latex id="n1w5x8"
\frac{ke^2}{r^2}=\frac{mv^2}{r}
```

---

## Momento angular cuantizado

```latex id="l5ot35"
mvr=n\hbar
```

---

## Radio de Bohr

```latex id="79y61s"
r_n=a_0n^2
```

---

## Energía cuantizada

```latex id="vrgm6o"
E_n=\frac{E_0}{n^2}
```

---

# 13. TRANSICIONES ELECTRÓNICAS

## Representación gráfica

Saltos entre niveles energéticos.

## Fórmula

```latex id="0lq6tp"
hf=E_i-E_f
```

---

# 14. FÓRMULA DE RYDBERG

## Representación gráfica

Serie de Balmer y espectros.

## Fórmula principal

```latex id="rv56ig"
\frac1{\lambda}=R\left(\frac1{n_f^2}-\frac1{n_i^2}\right)
```

---

# 15. LONGITUD DE ONDA DE DE BROGLIE

## Representación gráfica

Electrón como onda.

## Fórmula principal

```latex id="zwq33h"
\lambda=\frac{h}{p}
```

---

# 16. ONDAS ESTACIONARIAS DEL ELECTRÓN

## Representación gráfica

Ondas permitidas en órbitas.

## Fórmula

```latex id="fx0v3y"
2\pi r=n\lambda
```

---

# 17. ECUACIÓN DE SCHRÖDINGER

## Representación gráfica

Evolución de función de onda.

## Fórmula dependiente del tiempo

```latex id="2owz1y"
i\hbar\frac{\partial\psi}{\partial t}=
-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}
```

---

# 18. ECUACIÓN DE SCHRÖDINGER GENERAL

## Con potencial

```latex id="2vg1be"
i\hbar\frac{\partial\psi}{\partial t}=
-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}+V\psi
```

---

# 19. ECUACIÓN INDEPENDIENTE DEL TIEMPO

## Estados estacionarios

```latex id="pdsm8q"
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}+V\psi=E\psi
```

---

# 20. ONDA PLANA CUÁNTICA

## Representación gráfica

Parte real e imaginaria de la onda.

## Fórmula principal

```latex id="0t4jq7"
\psi(x,t)=Ae^{i(kx-\omega t)}
```

---

# 21. DENSIDAD DE PROBABILIDAD

## Representación gráfica

Probabilidad de encontrar la partícula.

## Fórmula

```latex id="d7g0c3"
P(x)=|\psi(x,t)|^2
```

---

# 22. NORMALIZACIÓN

## Fórmula

```latex id="a3qpm4"
\int_{-\infty}^{\infty}|\psi|^2dx=1
```

---

# 23. PAQUETE DE ONDAS

## Representación gráfica

Superposición de ondas planas.

## Fórmula principal

```latex id="d3h15n"
\Psi(x,t)=\sum_n A_ne^{i(k_nx-\omega_nt)}
```

---

# 24. OPERADOR MOMENTO

## Fórmula

```latex id="sxyg2n"
\hat{p}=-i\hbar\frac{\partial}{\partial x}
```

---

# 25. OPERADOR ENERGÍA

## Fórmula

```latex id="c9v5b2"
\hat{E}=i\hbar\frac{\partial}{\partial t}
```

---

# ORDEN RECOMENDADO PARA PROGRAMAR

## Nivel 1 — Ondas clásicas

```text id="sv7c0k"
1. Movimiento armónico
2. Onda viajera
3. Superposición
4. Interferencia
5. Ondas estacionarias
```

---

## Nivel 2 — Óptica

```text id="7ggpjm"
6. Doble rendija
7. Difracción
8. Patrón combinado
```

---

## Nivel 3 — Física atómica

```text id="n0mr3v"
9. Modelo de Bohr
10. Transiciones electrónicas
11. Serie de Balmer
```

---

## Nivel 4 — Mecánica cuántica

```text id="0j9sxf"
12. Onda plana cuántica
13. Probabilidad
14. Schrödinger
15. Paquetes de ondas
```

---

# LAS SIMULACIONES MÁS IMPORTANTES DEL DOCUMENTO

## Más fáciles

```text id="wxu0hm"
- MAS
- onda viajera
- interferencia
- ondas estacionarias
```

---

## Nivel intermedio

```text id="12w1d6"
- doble rendija
- difracción
- Bohr
```

---

## Más complejas

```text id="jlwmme"
- Schrödinger
- paquetes de ondas
- densidad de probabilidad
```
