# Manual de usuario

## Indice

  1. [Requerimientos](#requerimientos)
  2. [Uso de la aplicacion](#uso-de-la-aplicacion)
  3. [Modulos](#modulos)
      - [Metodo de Muller](#metodo-de-muller)
      - [Regula Falsi](#regula-falsi)
      - [Metodo de la Secante](#metodo-de-la-secante)
      - [Newton en C](#newton-en-c)

## Requerimientos

- [pdflatex](https://gist.github.com/rain1024/98dd5e2c6c8c28f9ea9d)

## Uso de la aplicacion

Una vez se inicie el programa se muestra una ventana donde el usuario tendra botones a la izquierda de la ventana con cada uno de los metodos con los que podra interactuar. Dependiendo de la opcion seleccionada los campos requeridos cambiaran.

| ![vista inicial](https://i.ibb.co/fH8LpSP/secante.png) | 
|:--:| 
| *Vista al iniciar la aplicacion, al lado izquierdo se encuentran los botones para navegar por la misma.* |

El programa exporta los resultados obtenidos en un archivo pdf una vez se pulsa el boton "Calcular", lo cual abre una ventana que permite al usuario escoger como nombrar al archivo y la ruta donde este se guarda

![vista guardar como](https://i.ibb.co/cCq65s6/save.png)

Una vez guardado el PDF generado se vera parecido al siguiente:
![pdf generado por el metodo de Newton](https://i.ibb.co/xHSJYnc/53-26-22-225347.png)
## Modulos

Para digitar las ecuaciones dentro del programa seguir las equivalencias dadas en la siguiente tabla

| Expresion      | Equivalente   |
|----------------|:-------------:|
| sqrt(x)    |    x**(1/2)   |
| x^2        |    x**2       |

Por lo que para ingresar esta ecuacion sqrt(x) + 10x - 20 a la aplicacion se haria de la siguiente forma:
> x * x**(1./2.) + 10 * x - 20

Los resultados obtenidos de las operaciones se exportan en un PDF, el cual contendra: iteraciones, raiz resultante y una tabla de valores

**PD: Debido a limitaciones de python, los métodos de Muller, Secante y Regula Falsi no trabajan con números negativos en intérvalos ya que esta operación los convierte a complejos:**

Ejemplo:
```python
>>> (-27) ** (1/3)
(1.5000000000000004+2.598076211353316j)
>>> (-1) ** (1/3)
(0.5000000000000001+0.8660254037844386j)
```

### Metodo de Muller

Dentro de este modulo calcula la raiz estimada de una funcion a partir de 3 valores iniciales x0, x1 y  x2 teniendo en cuenta la tolerancia especificada.

![vista metodo muller](https://i.ibb.co/mqq19ch/muller.png)

### Regula Falsi

Se calcula la raiz estimada de una funcion con dos puntos iniciales xa y xb siempre y cuando xa < xb y el resultado se basa en la tolerancia especificada.
Si xa < xb no se cumple el modulo no dara resultados.

![vista metodo falsi](https://i.ibb.co/P4NsBJq/falsi.png)

### Metodo de la Secante

Se calcula la raiz estimada de una funcion con dos puntos iniciales xa y xb siempre y cuando xa < xb y el resultado se basa en la tolerancia especificada.
Si xa < xb no se cumple el modulo no dara resultados.

![vista metodo secante](https://i.ibb.co/fH8LpSP/secante.png)
### Newton en C

Newton en C trabaja con un numero complejo como valor inicial, por lo que para ingresar este al programa debe de hacerse sin espacios, de esta manera:
> 2+2j

Ademas del numero complejo, espera el numero de iteraciones con las que se espera trabajar y la funcion la cual se desea estimar

![vista metodo secante](https://i.ibb.co/G2wH6z3/newton.png)
