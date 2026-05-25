# Simulaciones Gráficas del Documento — Fórmulas Base en LaTeX

## Objetivo

Este documento contiene únicamente:

* las simulaciones visuales/gráficas presentes en el documento original
* las fórmulas matemáticas usadas en dichas representaciones
* las ecuaciones en formato LaTeX
* las variables necesarias para programarlas en Python

---

# 1. MOVIMIENTO ARMÓNICO SIMPLE

## Representación gráfica

Oscilación sinusoidal de una partícula.

## Fórmula principal

```latex id="m0jlwm"
x(t)=A\cos(\omega t+\phi)
```

## Variables

```latex id="nyx5wd"
A \rightarrow amplitud
```

```latex id="mcfh85"
\omega \rightarrow frecuencia angular
```

```latex id="mxz5io"
\phi \rightarrow fase inicial
```

---

# 2. ONDA VIAJERA

## Representación gráfica

Propagación de una onda en el espacio.

## Fórmula principal

```latex id="r2n49v"
y(x,t)=A\cos(kx-\omega t+\phi)
```

## Fórmulas auxiliares

### Número de onda

```latex id="vrmnnr"
k=\frac{2\pi}{\lambda}
```

### Frecuencia angular

```latex id="0kv8ry"
\omega=2\pi f
```

### Velocidad de propagación

```latex id="kj80rn"
v=\lambda f
```

---

# 3. SUPERPOSICIÓN DE ONDAS

## Representación gráfica

Interferencia entre dos ondas.

## Fórmula principal

```latex id="7b6m4h"
y_R(x,t)=y_1(x,t)+y_2(x,t)
```

---

# 4. INTERFERENCIA CONSTRUCTIVA

## Representación gráfica

Máximos de intensidad.

## Fórmula

```latex id="kqrf1l"
\Delta r=n\lambda
```

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
