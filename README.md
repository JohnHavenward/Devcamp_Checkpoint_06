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

```python

```


</br>


### INSTANCIAS

La creación de una instancia, también llamada instanciación de una clase, es el proceso de crear un objeto a partir de la plantilla definida por la clase. 

Una clase puede tener tantas instancias creadas como se quiera.

Para acceder a los métodos y atributos de la instancia se usa el operador `.` tal y como vemos a continuación:

```python

```
</br>


### CONSTRUCTOR

Cuando una instancia de una clase es creada se ejecuta automáticamente el método `__init__()`. Este método es el constructor de la clase y se encarga de recibir los argumentos y asignarlos a la instancia. De esta forma podemos asignar de forma sencilla y breve información a cada una de las instacias creadas.

El constructor debe estar definido dentro de la clase y hacer uso del parámetro `self` para hacer referencia a la instancia creada.

Cuando creamos una instancia no es necesario hacer ninguna referencia al método `__init__()`, simplemente debemos pasar todos los argumentos definidos en él y omitir el argumento `self` ya que este es pasado de forma implícita.

Podemos ver un ejemplo del uso de un constructor a continuación:

```python

```

</br>


### ATRIBUTOS

Un atributo es una variable que forma parte de una clase. La única diferencia con una variable normal de python es que un atributo siempre debe estar asociado a una clase.

Una clase puede contener tantos atributos como se quiera.

Hay dos tipos de atributos dentro de una clase:

- Atributos de clase
- Atributos de instancia
</br>

Los atributos de clase son comunes a todas las instancias y se definen directamente dentro de la clase. El valor de un atributo es único y compartido por todas las instancias y la propia clase. Si alguno de los objetos asociados a ella cambia su valor lo hace también para el resto. Podemos ver un ejemplo de ello a continuación:

```python

```
</br>

Los atributos de instancia son propios de cada instancia y se definen dentro del método `__init__()`. Cada instancia tiene un valor propio para cada atributo.  Si una instancia cambia el valor de su atributo no afecta al resto de las instancias. Además la clase en sí no tiene definidos estos atributos y por tanto no tiene acceso a ellos. Podemos ver la definición y uso de atributos de instancia en el siguiente ejemplo:

```python

```
</br>


#### PROPIEDADES

Las propiedades son un tipo especial de atributo de instancia que se definen con el decorador `@property`. La principal diferencia de una propiedad es que permiten un acceso controlado a ella en los procesos de lectura y escritura  de esta. Esto permite hacer comprobaciones e incluso realizar algún cálculo de forma automática cuando se acceda a su valor.

Para ello se definen dos métodos:

- el método *getter*: se encarga de la lectura del atributo
- el método *setter*: se encarga de la escritura del atributo
</br>

Podemos ver un ejemplo del uso de propiedades a continuación:

```python

```
</br>

Nótese que aunque por su sintaxis un atributo puede parecer un método no se usa el símbolo `()` cuando se hace referencia a él. 
</br>


### MÉTODOS

Un método es una función que forma parte de una clase. La única diferencia con una función normal de python es que un método siempre debe estar asociado a una clase.

Una clase puede contener tantos métodos como se quiera. 
</br>


#### PARÁMETROS SELF Y CLS

Cuando definimos un método en una clase el primer parámetro siempre debe ser `self`. Este hace referencia al propio objeto que la llama y sirve para acceder a sus atributos y métodos.


Los métodos de una clase pueden 

> El parámetro self es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

El uso de del nombre *self* es totalmente arbitrario. Se trata de una convención acordada por los usuarios de Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre. Lo mismo ocurre con "cls", que veremos a continuación.
</br>


#### MÉTODOS DE INSTANCIA

> Los métodos de instancia son los métodos normales, de toda la vida, que hemos visto anteriormente. Reciben como parámetro de entrada self que hace referencia a la instancia que llama al método. También pueden recibir otros argumentos como entrada.

> Para saber más: El uso de "self" es totalmente arbitrario. Se trata de una convención acordada por los usuarios de Python, usada para referirse a la instancia que llama al método, pero podría ser cualquier otro nombre. Lo mismo ocurre con "cls", que veremos a continuación.

```python
class Clase:
    def metodo(self, arg1, arg2):
        return 'Método normal', self
````

Y como ya sabemos, una vez creado un objeto pueden ser llamados.

```python
mi_clase = Clase()
mi_clase.metodo("a", "b")
# ('Método normal', <__main__.Clase at 0x10b9daa90>)
```

En vista a esto, los métodos de instancia:

- Pueden acceder y modificar los atributos del objeto.
- Pueden acceder a otros métodos.
- Dado que desde el objeto self se puede acceder a la clase con ` self.class`, también pueden modificar el estado de la clase
</br>


#### MÉTODOS DE CLASE

> A diferencia de los métodos de instancia, los métodos de clase reciben como argumento cls, que hace referencia a la clase. Por lo tanto, pueden acceder a la clase pero no a la instancia.

```python
class Clase:
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls
```

Se pueden llamar sobre la clase.

```python
Clase.metododeclase()
# ('Método de clase', __main__.Clase)
Pero también se pueden llamar sobre el objeto.

mi_clase.metododeclase()
# ('Método de clase', __main__.Clase)
```

Por lo tanto, los métodos de clase:

- No pueden acceder a los atributos de la instancia.
- Pero si pueden modificar los atributos de la clase.
</br>


#### MÉTODOS ESTÁTICOS


> Por último, los métodos estáticos se pueden definir con el decorador @staticmethod y no aceptan como parámetro ni la instancia ni la clase. Es por ello por lo que no pueden modificar el estado ni de la clase ni de la instancia. Pero por supuesto pueden aceptar parámetros de entrada.

```python
class Clase:
    @staticmethod
    def metodoestatico():
        return "Método estático"
        
mi_clase = Clase()
Clase.metodoestatico()
mi_clase.metodoestatico()

# 'Método estático'
# 'Método estático'
```


> Por lo tanto el uso de los métodos estáticos pueden resultar útil para indicar que un método no modificará el estado de la instancia ni de la clase. Es cierto que se podría hacer lo mismo con un método de instancia por ejemplo, pero a veces resulta importante indicar de alguna manera estas peculiaridades, evitando así futuros problemas y malentendidos.

En otras palabras, los métodos estáticos se podrían ver como funciones normales, con la salvedad de que van ligadas a una clase concreta.
</br>


#### MÉTODOS ABSTRACTOS

> Como ya hemos visto los métodos abstractos son aquellos que son declarados pero no tienen una implementación. También hemos visto como Python nos obliga a implementarlos en la clases que heredan de nuestro interfaz. Esto es posible gracias al decorador @abstractmethod.

```python
from abc import ABC, abstractmethod
class Clase(metaclass=ABCMeta):
    @abstractmethod
    def metodo_abstracto(self):
        pass
```
</br>



### HERENCIA


</br>



### POLIFORMISMO


</br>








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

Estos métodos proporcionan una forma de definir comportamientos específicos para operaciones o funcionalidades integradas en las clases de Python.

La denominación *dunder* se corresponde a *double underscore* en referencia a los guiones bajos dobles que se escriben al principio y final del nombre de estas funciones. Estos métodos también son llamados métodos mágicos de python.

Un empleo muy frecuente para los métodos *dunder* es para la sobrecarga de operadores. Se trata de reutilizar los propios  operadores de python para que realicen la función que deseemos al usarse con la clase que hemos definido. Vemos un ejemplo de ello a continuación:

</br>

```python
class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __add__(self, other):
        return self.edad + other.edad

alumno_01 = Alumno("Gorka", 13)
alumno_02 = Alumno("Paula", 17)

print(f'Edad total: {alumno_01 + alumno_02}')
#Edad total: 30       
```

</br>


Todos los métodos *dunder* están predefinidos en python y se reservan para un uso especial del lenguaje. Es por ello que los métodos *dunder* no son llamados directamente en el código, sino que es el propio intérprete de python el que se encarga de hacerlo durante la ejecución del programa. No podemos crear nuevos métodos *dunder* pero sí implementar los ya existentes en nuestras clases para poder modificar su funcionamiento.

Normalmente los métodos *dunder* tienen un único parámetro llamado `self` y que hace referencia a la propia clase. En ocasiones pueden tener un parámetro adicional llamado `other` y que hace referencia a la otra clase implicada en el método. Ambos parámetros `self` y `other` son nombrados así por convenio.

</br>


### EJEMPLO PRÁCTICO

En este ejemplo vamos a crear la clase `Rectángulo` y vamos a incorporar paso a paso varios métodos *dunder* para poder entender cómo se usan y lo realmente útiles que pueden llegar a ser.

</br>


#### PASO 1 - Definir la clase `Rectángulo`

Definimos la clase `Rectángulo`. Nótese que la palabra clave `pass` simplemente se usa para evitar un error de ejecución por estar esta vacía.

</br>

```python
class Rectángulo:
    pass
```

</br><br>


#### PASO 2 - Método `__init__`

Definimos el método `__init__` junto con los parámetros `self`, `altura`y `anchura`. Se trata del constructor de la clase y su función es tomar los argumentos y asignarlos a los atributos de la instancia creada.

</br>

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
```

<br></br>


#### PASO 3 - Método `__len__`

La función `len()` se usa normalmente en python para obtener el tamaño de una colección y saber cuantos elementos tiene. Imaginemos que nosotros queremos implementar esa función en nuestra clase y que calcule el valor de la superficie. Podemos hacerlo mediante la definición del método `__len__` en nuestra clase devolviendo el producto de los atributos `altura` y `anchura`. Hay que tener en cuenta que la función `len()` de python solo puede devolver una variable de tipo `int` por lo que para evitar posibles errores debemos usar la función `round()` para redondear el cálculo de la superficie.

</br>

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        
    def __len__(self):
        return round(self.altura * self.anchura)
```

<br></br>


#### PASO 4 - Método `__str__`

Por defecto cuando usamos `print()` para mostrar en la terminal la instancia de una clase lo que se muestra es su dirección en memoria y la clase a la que pertenece. En nuestro caso nos interesa más una cadena que nos informe sobre las dimensiones y superficie del rectángulo. Podemos implementar el método `__str__` en nuestra clase para definir la cadena mostrada.

</br>

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        
    def __len__(self):
        return round(self.altura * self.anchura)

    def __str__(self):
        return f'Rectángulo de {self.altura}cm de altura, {self.anchura}cm de anchura y {len(self)}cm2 de superficie'
```

</br></br>


#### PASO 5 - Métodos `__eq__` , `__lt__`, `__le__`, `__gt__` y `__ge__`

A continuación podemos habilitar las comparaciones entre instancias de nuestra clase que por defecto no están disponibles. Para ello debemos especificar la forma en que python debe evaluar esas comparaciones implementando cada una de las funciones *dunder* respectivas. En nuestro caso evaluamos la superficie de los dos rectángulos comparados empleando los parámetros `self` y `other` que hacen referencia a cada uno.

</br>

```python
class Rectángulo:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        
    def __len__(self):
        return round(self.altura * self.anchura)

    def __str__(self):
        return f'Rectángulo de {self.altura}cm de altura, {self.anchura}cm de anchura y {len(self)}cm2 de superficie'

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
</br></br>


Por último creamos varias instancias de nuestra clase y hacemos uso de las diferentes operaciones para comprobar que los métodos *dunder* que hemos definido funcionan correctamente.

</br>
 
```python
rectángulo_uno = Rectángulo(3, 8)
print(f'print(UNO): {rectángulo_uno}')
#print(UNO): Rectángulo de 3cm de altura, 8cm de anchura y 24cm2 de superficie

rectángulo_dos = Rectángulo(5.6, 7)
print(f'print(DOS): {rectángulo_dos}')
#print(DOS): Rectángulo de 5.6cm de altura, 7cm de anchura y 39cm2 de superficie

rectángulo_tres = Rectángulo(2, 12)
print(f'print(TRES): {rectángulo_tres}')
#print(TRES): Rectángulo de 2cm de altura, 12cm de anchura y 24cm2 de superficie

print(f'UNO = DOS: {rectángulo_uno == rectángulo_dos}')
#UNO = DOS: False

print(f'UNO < DOS: {rectángulo_uno < rectángulo_dos}')
#UNO < DOS: True

print(f'UNO <= TRES: {rectángulo_uno <= rectángulo_tres}')
#UNO <= TRES: True

print(f'UNO > TRES: {rectángulo_uno > rectángulo_tres}')
#UNO > TRES: False

print(f'DOS >= TRES: {rectángulo_dos >= rectángulo_tres}')
#DOS >= TRES: True
```
</br>



### MÉTODOS DUNDER COMUNES

A continuación se muestran varias tablas con los métodos *dunder* más comunes clasificados por tipos de operaciones:

</br>


Operaciones aritméticas binarias:

Método | Parámetros | Operador | Descripción
------ | :--------: | :------: | -----------
`__add__`      | (self, other) | +  | suma
`__sub__`      | (self, other) | –  | substracción
`__mul__`      | (self, other) | *  | multiplicación
`__div__`      | (self, other) | /  | división
`__floordiv__` | (self, other) | // | división con redondeo a la baja
`__mod__`      | (self, other) | %  | módulo
`__pow__`      | (self, other) | ** | potencia
`__rshift__`   | (self, other) | >> | operación *shift right*
`__lshift__`   | (self, other) | << | operación *shift right*
`__and__`      | (self, other) | &  | operación lógica AND
`__or__`       | (self, other) | \| | operación lógica OR
`__xor__`      | (self, other) | ^  | operación lógica XOR

</br></br>


Operaciones aritméticas unarias:

Método | Parámetros | Operador | Descripción
------ | :--------: | :------: | -----------
`__pos__`    | (self) | + |signo positivo
`__neg__`    | (self) | - |signo negativo
`__invert__` | (self) | ~ |invertir signo

</br></br>


Operaciones de asignación:

Método | Parámetros | Operador | Descripción
------ | :--------: | :------: | -----------
`__iadd__`      | (self, other) | +=  | suma
`__isub__`      | (self, other) | –=  | substracción
`__imul__`      | (self, other) | *=  | multiplicación
`__idiv__`      | (self, other) | /=  | división
`__ifloordiv__` | (self, other) | //= | división con redondeo a la baja
`__imod__`      | (self, other) | %=  | módulo
`__ipow__`      | (self, other) | **= | potencia
`__irshift__`   | (self, other) | >>= | operación *shift right*
`__ilshift__`   | (self, other) | <<= | operación *shift right*
`__iand__`      | (self, other) | &=  | operación lógica AND
`__ior__`       | (self, other) | \|= | operación lógica OR
`__ixor__`      | (self, other) | ^=  | operación lógica XOR

</br></br>


Operaciones de comparación:

Método | Parámetros | Operador | Descripción
------ | :--------: | :------: | -----------
`__eq__` | (self, other) | == | igual
`__ne__` | (self, other) | != | no igual
`__lt__` | (self, other) | <  | menor que
`__le__` | (self, other) | <= | menor o igual 
`__gt__` | (self, other) | >  | mayor que
`__ge__` | (self, other) | >= | mayor o igual 

</br></br>


Operaciones de ciclo de vida:

Método | Parámetros | Descripción
------ | :--------: | -----------
`__init__` | (self) | inicializa la instancia
`__del__`  | (self) | destruye la instancia
`__new__`  | (cls)  | crea la instancia 

</br></br>


Operaciones de representación:

Método | Parámetros | Descripción
------ | :--------: | -----------
`__str__`  | (self) | Muestra una cadena informativa cuando se llama a la función `print()`
`__repr__` | (self) | muestra una cadena informativa cuando se llama a la función `repr()`

</br></br></br>

**NOTA:** podemos encontrar una lista más extensa de métodos *dunder* en el siguiente [enlace](https://blog.finxter.com/python-dunder-methods-cheat-sheet/)


</br></br></br></br></br>





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
