---
marp: true
---

# Python

---

## Instalación

- **Python** (Instalar desde [python.org](https://python.org))
- **Visual Studio Code** (VS Code)
    - Instalar la **extensión de Python** (Microsoft)

---

## Características

- **Interpretado**: El código fuente es procesado directamente por un **intérprete**, sin necesidad de compilación.
    - Intérprete predeterminado en **C** (CPython)
    - Intérprete alternativo en **Python**: **PyPy**
    - Intérprete en **C#**: **IronPython**
- **Tipado dinámico y estricto**: No es necesario declarar el tipo de las variables, pero los tipos deben ser correctos en tiempo de ejecución.
- **Lenguaje de scripting**: Útil para automatización de tareas.
- Herramientas instaladas:
    - **IDLE**: Editor básico de texto de Python.
    - **Intérprete**: Ejecuta archivos con `python archivo.py`.
    - **REPL**: Consola interactiva (Read-Eval-Print Loop) para pruebas rápidas.

---

## Tipos de datos básicos:

- `bool`: Booleano.
- `int`: Entero (64 bits).
- `float`: Flotante (64 bits).
- `str`: Cadena de caracteres.
- `None`: Similar a `null` en otros lenguajes.

### Conversiones de tipo

- `int(x)`: Convierte `x` a entero.
- `float(x)`: Convierte `x` a flotante.
- `bool(x)`: Convierte `x` a booleano.
- `str(x)`: Convierte `x` a cadena de texto.

---

### Operadores

- **Aritméticos**: `+`, `-`, `*`, `/`, `%`
    - Particulares: 
        - `//` (División entera)
        - `**` (Exponenciación)
    - Para cadenas: 
        - `+` (Concatenar)
        - `*` (Repetir)
- **Comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Lógicos**: `and`, `or`, `not`
- **Otros**:
    - `in`: Verifica si un elemento está en una colección.
    - `is`: Comprueba si dos objetos son idénticos (misma referencia en memoria).

---

## Convenciones de nombres

- `nombre_variable`: Identificador de una variable u objeto.
- `NombreClase`: Identificador de una clase.
- `NOMBRE_CONSTANTE`: Identificador de una constante (se puede modificar, pero no es recomendable).

Tipos comunes de nomenclatura:

- `snake_case`: Usado en Python para nombres de variables y funciones.
- `camelCase`: Usado en otros lenguajes como Java.

Ejemplo:
```python
tasa_de_interes = 1.5
IMPUESTO_SOBRE_VENTA = 15.0
```

---

## Funciones incorporadas
- `type(x)`: Permite establecer el tipo de dato de una expresión.
- `input("Mensaje")`: Obtiene un str de la entrada estándar.
- `print(exp)`: Muestra en consola una expresión. Puede usarse sep y end para indicar la separación y finalización de dicho mensaje.
- `range(start, end, step)`: Generador que define una serie de valores enteros en el rango [start, end). 
Variaciones:
    - range(5): El end es 5. Genera: 0, 1, 2, 3, 4.
    - range(2, 5): start es 2, end es 5. Genera: 2, 3, 4.
    - range(2, 10, 2): El tercer elemento es el step. Genera: 2, 4, 6, 8.