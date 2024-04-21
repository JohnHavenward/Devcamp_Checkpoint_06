<!-- <link href="style.css" rel="stylesheet"></link> -->

# PREGUNTAS TEÓRICAS

[¿Para qué usamos Clases en Python?](#texto)</br>
[¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#texto)</br>
[¿Cuáles son los tres verbos de API?](#texto)</br>
[¿Es MongoDB una base de datos SQL o NoSQL?](#texto)</br>
[¿Qué es una API?](#texto)</br>
[¿Qué es Postman?](#texto)</br>
[¿Qué es el polimorfismo?](#texto)</br>
[¿Qué es un método dunder?](#texto)</br>
[¿Qué es un decorador de python?](#texto)</br>
</br>



# CLASES




### PROGRAMACIÓN ORIENTADA A OBJETOS



Una clase puede entenderse como una plantilla 

Puede resultar útil para entender el concepto de una clase fijarse en el mito de la cueva descrito por Platón. En él la idea de un objeto puede entenderse como la clase en la que se basan el resto de 

La clase es la parte teórica que no podemos encontrar directamente presente en la realidad pero que identificamos fácilmente en los objetos reales que la representan.

> el concepto de encapsulación de la programación orientada a objetos. Este concepto nos indica que en determinadas ocasiones es importante ocultar el estado interno de los objetos al exterior, para evitar que sean modificados de manera incorrecta. Para la gente que venga del mundo de Java, esto no será nada nuevo, y está muy relacionado con los métodos set()y get() que veremos a continuación.

### INSTANCIAS

La instanciación de una clase es el proceso de crear un objeto a partir de la plantilla definida por la clase

Las instancias son las diferentes copias de la clase creada


### PARÁMETROS SELF Y CLS

> Para saber más: El uso de "self" es totalmente arbitrario. Se trata de una convención acordada por los usuarios de Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre. Lo mismo ocurre con "cls", que veremos a continuación.


### MÉTODOS Y ATRIBUTOS

Un método es una función que forma parte de una clase. La única diferencia con una función es que un método siempre debe estar asociado a una clase.

Un atributo es una variable 

Una clase puede contener tantos métodos como atributos se quiera. 

Para acceder a ellos se una el operador `.` junto al nombre de la instancia.


### PROPIEDADES



### CONSTRUCTOR

Cuando una instancia de una clase es creada se ejecuta automáticamente el método `__init__()` 




### POLIFORMISMO




### HERENCIA


### MÉTODOS DE INSTANCIA


### MÉTODOS DE CLASE


### MÉTODOS ESTÁTICOS





### MÉTODOS ABSTRACTOS


### INTERFACES














# API
[¿Qué es una API?](#texto)</br>
[¿Cuáles son los tres verbos de API?](#texto)</br>
[¿Qué es Postman?](#texto)</br>


Una API o Application Programming Interface


> Una API (del inglés, application programming interface, en español, interfaz de programación de aplicaciones)1​ es una pieza de código que permite a diferentes aplicaciones comunicarse entre sí y compartir información y funcionalidades. Una API es un intermediario entre dos sistemas, que permite que una aplicación se comunique con otra y pida datos o acciones específicas.

REST API  RESTful

Servidor Cliente



Permisos y autentificación


> HTTP verbs are the building blocks of REST API interactions. They define the actions that clients can perform on resources and play a crucial role in ensuring proper resource management. Understanding the semantics of these verbs, as well as their idempotent and safe characteristics, is fundamental in designing effective and predictable RESTful APIs.

> Safety : A safe operation is one that does not modify the state of the server. GET is considered a safe operation, as it does not change anything on the server. However, POST, PUT, and DELETE are not safe, as they can alter server state.



### ARCHIVOS JSON

JavaScript Object Notation



### VERBOS HTTP

Los verbos HTTP son fundamentales en la comunicación entre cliente y servidor ya que indican la acción a realizar
instrucciones



**GET** solicita información de un recurso al servidor. No provoca ningún cambio en el servidor. 

**POST** crea un nuevo recurso en el servidor. Junto a la solicitud el cliente debe enviar la información para crear el nuevo recurso.

**PUT** actualiza un recurso en el servidor. El cliente debe enviar el recurso al completo al servidor incluso si este ha sido modificado levemente. actualiza completamente el recurso

**PATCH** actualiza algunas partes del recurso

**DELETE** borra un recurso en el servidor. El cliente que envía la solicitud debe indicar la información a eliminar.

idempotencia

> El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.
> El método PATCH es utilizado para aplicar modificaciones parciales a un recurso.

> The most commonly used HTTP methods are GET, POST, PUT, PATCH, HEAD, DELETE, and OPTIONS.

### SISTEMA REST

Los verbos Http involucrados en un sistema REST son GET, POST, PUT, PATCH y DELETE

> REST es una arquitectura para aplicaciones en redes (REpresentational State Transfer). RESTful por otro lado, son programas (a modo de web service o API), basados en REST. Muchas veces se usan ambos terminos como sinonimos.

### SISTEMAS CRUD

El término *CRUD* se refiere a las iniciales de las cuatro operaciones básicas que se pueden llevar a cabo en la mayoría de las bases de datos y sistemas de gestión de información:

- [**C**]REATE - crear
- [**R**]EAD - leer
- [**U**]PDATE - actualizar
- [**D**]ELETE - borrar




### HTTP RESPONSE STATUS CODES

> HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:


1. Respuestas informativas (100 – 199)
2. Respuestas satisfactorias (200 – 299)
3. Redirecciones (300 – 399)
4. Errores de los clientes (400 – 499)
5. Errores de los servidores (500 – 599)


[link](https://developer.mozilla.org/es/docs/Web/HTTP/Status)




### POSTMAN

Postman es un software de uso gratuito popularmente usado para el desarrollo de APIs. Su principal función es permitirnos comunicarnos directamente con una API y emular las solicitudes que posteriormente harán loa aplicaciones web que se comuniquen con ella.

Podemos realizar cualquiera de las acciones HTTP y recibir la respuesta dada por la API para poder analizarla. El uso de herramientas como postman es de vital importancia para comprobar el funcionamiento de una API durante su desarrollo. Su principal ventaja es que nos ahorra tener que desarrollar una aplicación web   

Podemos usar la interfaz gráfica del programa para poder realizar las diferentes solicitudes

[postman.com](https://www.postman.com/)

Permite automatizar las peticiones

> Postman es una popular herramienta utilizada para probar APIs, permitiendo a los desarrolladores enviar peticiones a servicios web y ver respuestas. Exploraremos cómo Postman puede ser una herramienta esencial para probar APIs eficientemente. Test de regresión

> endpoints
> cuerpo de la solicitud










# BASES DE DATOS
[¿Es MongoDB una base de datos SQL o NoSQL?](#texto)</br>










# MÉTODOS DUNDER




> está reservado para un uso especial del lenguaje

Son métodos predefinidos en python 

Los métodos dunder, también llamados métodos mágicos de python, 

Estos métodos proporcionan una forma de definir comportamientos específicos para operaciones o funcionalidades integradas en las clases de Python.

La denominación dunder se corresponde a *double underscore* en referencia a los guiones bajos dobles que se escriben al principio y final del nombre de estas funciones.

Los métodos dunder no son llamados directmente en el código, sino que es el propio intérprete de python el que se encarga de hacerlo durante la ejecución del programa.


> Toman como primer argumento self. Pueden tomar argumentos adicionales dependiendo de cómo los llamará el intérprete.





### EJEMPLO PRÁCTICO

En este ejemplo vamos a crear la clase `Rectángulo` y vamos a incorporar paso a paso varios métodos *dunder* para poder entender cómo se usan y lo realmente útiles que pueden llegar a ser.
</br>


#### PASO 1 - Definir la clase `Rectángulo`

```python
class Rectángulo:
    pass
```
<br>


#### PASO 2 - Método `__init__()`

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
```
<br>


#### PASO 3 - Método `__len__()`

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        
    def __len__(self):
        return round(self.altura * self.anchura)
```
<br>


#### PASO 4 - Método `__str__()`

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        
    def __len__(self):
        return round(self.altura * self.anchura)

    def __str__(self):
        return f'Rectángulo de {self.altura}m de altura, {self.anchura}m de anchura y {len(self)}m2 de superficie'
```
</br>


#### PASO 5 - Métodos `__eq__()` , `__lt__()` y `__gt__()`

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        
    def __len__(self):
        return round(self.altura * self.anchura)

    def __str__(self):
        return f'Rectángulo de {self.altura}m de altura, {self.anchura}m de anchura y {len(self)}m2 de superficie'

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)
```



```python
rectángulo_uno = Rectángulo(10.45, 2)
rectángulo_dos = Rectángulo(10, 10.2)

print(len(rectángulo_uno))

print(rectángulo_uno <= rectángulo_dos)
```




### SOBRECARGA DE OPERADORES

- Operaciones aritméticas
- Operaciones de comparación
- Operaciones de ciclo de vida
- Operaciones de representación



### MÉTODOS DUNDER COMUNES



</br>

Operadores aritméticos binarios:

Nombre | Método |Operador | Argumentos |Descripción
------ | :----:  | :-----: | :---------: | ----
Adición          | `__add__`      | +  | (self, other) | Implementa la adición.
Sustracción      | `__sub__`      | –  | (self, other) | Implementa la resta.
Multiplicación   | `__mul__`      | *  | (self, other) | Implementa la multiplicación
División         | `__div__`      | /  | (self, other) | División de implementos.
División de piso | `__floordiv__` | // | (self, other) | Implementa división de piso.
Módulo           | `__mod__` | % | (self, other) | Implementa división de piso.
Potencia | `__pow__` | ** | (self, other) | Implementa división de piso.
División de piso | `__rshift__` | >> | (self, other) | Implementa división de piso.
División de piso | `__lshift__` | << | (self, other) | Implementa división de piso.
División de piso | `__and__` | & | (self, other) | Implementa división de piso.
División de piso | `__or__` | | | (self, other) | Implementa división de piso.
División de piso | `__xor__` | ^ | (self, other) | Implementa división de piso.
</br>

Operadores de asignación:

Nombre | Método |Operador | Argumentos |Descripción
------ | :----:  | :-----: | :---------: | ----
Adición          | `__iadd__`      | +=  | (self, other) | Implementa la adición.
Sustracción      | `__isub__`      | –=  | (self, other) | Implementa la resta.
Multiplicación   | `__imul__`      | *=  | (self, other) | Implementa la multiplicación
División         | `__idiv__`      | /=  | (self, other) | División de implementos.
División de piso | `__ifloordiv__` | //= | (self, other) | Implementa división de piso.
Módulo           | `__imod__`      | %= | (self, other) | Implementa división de piso.
Potencia         | `__ipow__`      | **= | (self, other) | Implementa división de piso.
División de piso | `__irshift__`   | >>= | (self, other) | Implementa división de piso.
División de piso | `__ilshift__`   | <<= | (self, other) | Implementa división de piso.
División de piso | `__iand__`      | &= | (self, other) | Implementa división de piso.
División de piso | `__ior__`       | |= | (self, other) | Implementa división de piso.
División de piso | `__ixor__`      | ^= | (self, other) | Implementa división de piso.
</br>

Operadores aritméticos unarios:

Nombre | Método |Operador | Argumentos |Descripción
------ | :----:  | :-----: | :---------: | ----
Positivo    | `__pos__`    | + | (self) | Implementa la adición.
Negativo    | `__neg__`    | - | (self) | Implementa la adición.
Invertir    | `__invert__` | ~ | (self) | Implementa la adición.
</br>

Operadores de comparación:

Nombre | Método |Operador | Argumentos |Descripción
------ | :----:  | :-----: | :---------: | ----
Menos que	            | `__lt__` | <  | (self, other) | Implementa la comparación menor que
greater que	            | `__gt__` | >  | (self, other) | Implementa el greater que la comparación
Igual a	            | `__eq__` | == | (self, other) | Implementa la comparación igual a
Menos que o igual a	| `__le__` | >= | (self, other) | Implementa la comparación menor o igual que
greater mayor o igual a	| `__ge__` | <= | (self, other) | Implementa el greater que o igual a la comparación
no igual a	            | `__ne__` | != | (self, other) | Implementa la no igualdad
</br>

Operaciones de ciclo de vida:

Método | Parámetros | Descripción
:----: | :--------: | -----------
`__init__` | (self) | Define el constructor
`__del__`  | (self) | Define el constructor
`__new__`  | (cls)  | Define el constructor
</br>

Operaciones de representación:

Método | Parámetros | Descripción
:----: | :--------: | -----------
`__str__`  | (self) | Define el constructor
`__repr__` | (self) | Define el constructor
</br>













# DECORADORES

Los *Function Decorators* o decoradores de python son una potente herramienta que nos permite modificar el comportamiento de una clase o función 

Un decorador contiene en su interior a una función y nos permiten ampliar el funcionamiento de esta sin tener que modificar su código.

Con el uso de decoradores podemos agregar funcionalidades complicadas a funciones o clases existentes con solo una línea de código.


```python
def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
```
</br>


Los decoradores de Python son herramientas valiosas para escribir código limpio, versátil, reutilizable y fácil de mantener.
La ventaja que ofrecen los decoradores es que permiten ampliar el funcionamiento de una función o clase sin cambiar su código original.


En esencia, cualquier función que toma como argumento una función y devuelva otra puede ser usada como un decorador.

Algunos de los usos comunes que se dan a los decoradores en python son:

- Almacenamiento en caché
- Registro
- Temporización
- Autenticación
- Autorización
- Validación.








### SINTAXIS

Debemos distinguir tres partes implicadas en la definición y uso de un decorador:

- Definición del decorador
- Definición de la función decorada
- Llamada a la función decorada
</br></br>

En lo que respecta al decorador, la definición de este se hace como una función normal teniendo en cuenta que debe recibir una función como parámetro y devolver otra.

Por otra parte se debe hacer la definición de la función decorada. Para ello debemos colocar el símbolo `@` junto al nombre del decorador justo antes de la definición de la función antigua, la cual no necesita ninguna alteración en su código.

Finalmente la llamada a la función decorada se hace de igual forma que se llama a la antigua, no es necesaria ninguna referencia al decorador.

Vemos un ejemplo de todo ello a continuación:

```python

```
</br>



### DECORADORES CON PARÁMETROS

Es posible usar decoradores que admitan parámetros para modificar su comportamiento. Para ello debemos envolver nuevamente nuestro decorador con otra función que los defina. Estos parámetros pueden ser usados dentro del decorador para obtener el comportamiento deseado. Se muestra un ejemplo a continuación:

```python
def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)
# Imprimer esto antes y después
# Entra en funcion suma
# Imprimer esto antes y después
```
</br>



### DECORADORES PREDEFINIDOS DE PYTHON

Algunos decoradores pueden usarse directamente ya que corresponden a funciones ya predefinidas en el código de python. A continuación se muestran algunos ejemplos:

Decorador | Descripción
--------- | -----------
@classmethod | Define un método de clase
@abstractmethod | Define un método abstracto
@staticmethod | Define un método estático
@atexit.register | 
@typing.final | 
@enum.unique | 
@property | Define el *getter* y el *setter* de una propiedad de clase
@enum.verify | 
@singledispatch | 
@lru_cache | 



### EJEMPLO PRÁCTICO

```python
autenticado = True

def requiere_autenticación(f):
    def funcion_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return f(*args, **kwargs)
    return funcion_decorada

@requiere_autenticación
def di_hola():
    print("Hola")
    
di_hola()
```
