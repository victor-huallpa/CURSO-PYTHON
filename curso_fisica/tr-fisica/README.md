# Plantilla de Resolución de Ejercicios - Física II

## Descripción General

Este proyecto contiene la estructura de un documento LaTeX para la resolución de ejercicios del Capítulo 26 (Circuitos) del libro "Física Universitaria" de Young, Freedman, Sears y Zemansky, Volumen II. Es un trabajo colaborativo de la asignatura Física II de la Escuela Profesional de Ingeniería de Software y Sistemas, Universidad Nacional de Juliaca.

**Docente:** Dr. Calcina Cuevas Serapio Cecilio

---

## Estructura del Proyecto

```
├── main.tex                 # Archivo principal (documento maestro)
├── README.md               # Este archivo
│
├── config/                 # Archivos de configuración
│   ├── packages.tex       # Paquetes necesarios
│   ├── settings.tex       # Configuración global (márgenes, fuentes, etc.)
│   ├── commands.tex       # Comandos personalizados
│   └── portada.tex        # Portada del documento
│
├── content/               # Contenido general
│   └── resumen.tex        # Introducción/resumen
│
├── ejercicios/            # Ejercicios por integrante
│   ├── 01_parte/          # Integrante 1 (ejemplo de referencia)
│   ├── 02_parte/          # Integrante 2
│   ├── 03_parte/          # Integrante 3
│   ├── 04_parte/          # Integrantes 4-8
│   ├── 05_parte/          
│   ├── 06_parte/          
│   ├── 07_parte/          
│   └── 08_parte/          
│
├── template/              # Plantillas
│   └── ejercicio_template.tex  # Plantilla base para ejercicios
│
└── img/                   # Directorio para imágenes (vacío)
```

---

## Configuración

### Paquetes Utilizados

Los paquetes LaTeX incluidos en `config/packages.tex` proporcionan:

- **Idioma:** Soporte para español (`babel`)
- **Matemáticas:** `amsmath`, `amssymb`, `amsthm`, `mathtools` para notación científica
- **Gráficos:** `graphicx` para insertar imágenes, `float` para control de flotantes
- **Formato:** `booktabs`, `array` para tablas; `xcolor` para colores
- **Referencias:** `hyperref` para hipervínculos, `cleveref` para referencias inteligentes
- **Formato de página:** `fancyhdr` para encabezados/pies, `geometry` para márgenes
- **Tipografía:** `microtype` para justificación mejorada
- **Listas:** `enumitem` para control de enumeraciones

### Comandos Personalizados

En `config/commands.tex` se definen tres comandos principales:

- `\ejercicio{XX}` - Crea una sección para el ejercicio número XX
- `\enunciado` - Subsección para el enunciado del problema
- `\solucion` - Subsección para la solución

---

## Estructura de un Ejercicio

### Plantilla Base

Cada ejercicio debe seguir esta estructura (ver `template/ejercicio_template.tex`):

```latex
\ejercicio{XX}

\enunciado
Escriba aquí el enunciado.

\solucion
Escriba aquí la solución.
```

### Ejemplo de Referencia

La carpeta `ejercicios/01_parte/` contiene dos archivos:
- `ejer_01.tex` - Ejemplo modelo de resolución de ejercicio
- `ejer_01 copy.tex` - Copia del ejemplo (nota: revisar antes de compilar)

**Nota:** La carpeta 01_parte sirve únicamente como referencia y ejemplo de formato. No debe editarse una vez definido como estándar.

---

## Instrucciones de Uso

### 1. Agregar un Nuevo Ejercicio

Para la carpeta correspondiente (ej: `ejercicios/02_parte/`):

a) Crear archivo `ejer_XX.tex` en la carpeta asignada:

```latex
\ejercicio{XX}

\enunciado
[Enunciado del problema]

\solucion
[Desarrollo matemático y solución]
```

b) Incluir el archivo en `ejercicios/XX_parte/ejercicios.tex`:

```latex
\input{ejercicios/XX_parte/ejer_XX}
```

### 2. Compilación del Documento

```bash
latexmk -pdf main.tex
```

O compilación manual:

```bash
pdflatex main.tex
```

### 3. Insertar Imágenes

Las imágenes deben colocarse en la carpeta `img/` y referenciarse como:

```latex
\includegraphics[width=0.8\textwidth]{img/nombre_imagen.png}
```

### 4. Ecuaciones Matemáticas

Utilizar el entorno `equation` o `align*`:

```latex
\begin{equation}
F = ma
\end{equation}
```

---

## Estructura del Documento Principal

El archivo `main.tex` incluye en orden:

1. **Configuración:** Paquetes, settings y comandos
2. **Portada:** Información da institución, asignatura y bibliografía
3. **Índice:** Tabla de contenidos autogenerada
4. **Resumen:** Introducción general en `content/resumen.tex`
5. **Ejercicios:** Ocho secciones, una por integrante (02 a 08 cargan de 04_parte)

---

## Notas Importantes

- **Compilación:** Se recomienda usar `latexmk` para manejo automático de referencias cruzadas y generación de índice.
- **Archivos auxiliares:** Los archivos `.aux`, `.fdb_latexmk`, `.fls` y `.toc` se generan automáticamente durante la compilación. No deben editarse.
- **Portada:** Modificar únicamente si cambia docente, institución o referencia bibliográfica.
- **Formato consistente:** Usar siempre los comandos `\ejercicio`, `\enunciado` y `\solucion` para mantener consistencia.
- **Espacios en nombres:** Evitar espacios en nombres de archivos (ej: no usar `ejer 01.tex`).

---

## Próximos Pasos

1. Validar que cada integrante agregue sus ejercicios en su carpeta correspondiente
2. Verificar referencia cruzada correcta en `main.tex`
3. Realizar compilación final con `latexmk -pdf main.tex`
4. Revisar índice y referencias generadas correctamente

---

**Versión:** 1.0  
**Última actualización:** Junio 2026
