

# PREGUNTAS TEÓRICAS

[¿Para qué usamos Clases en Python?](#clases)</br>
[¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#constructor)</br>
[¿Cuáles son los tres verbos de API?](#métodos-http)</br>
[¿Es MongoDB una base de datos SQL o NoSQL?](#mongodb)</br>
[¿Qué es una API?](#api)</br>
[¿Qué es Postman?](#postman)</br>
[¿Qué es el polimorfismo?](#polimorfismo)</br>
[¿Qué es un método dunder?](#métodos-dunder)</br>
[¿Qué es un decorador de python?](#decoradores)</br>
</br>



# CLASES

Python es un lenguaje de programación orientado a objetos y por tanto emplea los conceptos de clase y objeto. La programación orientada a objetos está basada en cuatro principios o pilares básicos que son los siguientes:

- **Herencia** - reutilizar el código compartiéndolo entre varios objetos.
- **Encapsulamiento** - proteger la información de manipulaciones no autorizadas.
- **Abstracción** - representar y manejar conceptos complejos de manera simplificada.
- **Polimorfismo** - ejecutar la misma orden con varios objetos y que respondan de formas diferentes.

</br>


Las clases son la pieza clave para poder cumplir esos principios y en esencia lo que hacen es agrupar una serie de variables y funciones en un único elemento. Una vez definido, ese elemento puede ser construido múltiples veces y cada copia es única e independiente del resto. Las clases pueden entenderse así como las "plantillas" o "modelos" que son usados para producir objetos nuevos.

</br>

Puede resultar útil para entender el concepto de una clase fijarse en el mito de la cueva descrito por Platón. En él la idea de un objeto es el único verdadero o perfecto y puede verse como la clase. El resto son solo sombras proyectadas y se corresponden con los objetos creados a partir de esa clase.

La clase es la parte teórica que no podemos encontrar directamente presente en la realidad pero que identificamos fácilmente en los objetos reales que la representan.

</br>

![Mito de la cueva](/images/mito_cueva.png)

</br></br>


En python cada objeto pertenece a una clase y es la que la hace tener ciertas funciones y variables asociadas a ella.

Para definir una clase debemos usar la palabra reservada `class` junto a su nombre. Por convenio la primera letra del nombre de una clase siempre de escribe en mayúsculas. Vemos un ejemplo a continuación:

</br>

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


Para eliminar una instancia creada podemos usar la palabra clave `del` tal y como se ve en el siguiente ejemplo:

</br>

```python
del p1
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

Un método es una función que forma parte de una clase. La única diferencia con una función normal de python es que un método siempre debe estar asociado a una clase. Se pueden definir tantos métodos como se quiera dentro de una clase.

Cuando definimos un método el primer parámetro siempre debe ser `self`. Este hace referencia a la instancia que la llama y sirve para acceder a sus atributos y métodos. El uso de del nombre *self* es totalmente arbitrario y simplemente se trata de una convención.

Existen principalmente cuatro tipos diferentes de métodos y son los siguientes:

- Métodos de instancia
- Métodos de clase
- Métodos estáticos
- Métodos abstractos

</br>


#### MÉTODOS DE INSTANCIA


Los métodos de instancia son los métodos definidos normalmente dentro de la clase. Aparte de `self` pueden definir otros parámetros.

</br>

```python
class Clase:
    def metodo(self, arg1, arg2):
        return 'Método normal', self


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

> A diferencia de los métodos de instancia, los métodos de clase reciben como argumento `cls` , que hace referencia a la clase. Por lo tanto, 

Los métodos de clase se definen con el decorador `@classmethod` y usan el parámetro `cls` en lugar de `self`. Este parámetro hace referencia a la clase del objeto y no a la instancia. Es por ello que solo pueden acceder y modificar a la clase y en ningún caso pueden hacerlo a la propia instancia.



Pueden llamarse desde la clase o la instancia indistintamente.

```python
class Clase:
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls



Clase.metododeclase()
# ('Método de clase', __main__.Clase)
Pero también se pueden llamar sobre el objeto.

mi_clase.metododeclase()
# ('Método de clase', __main__.Clase)
```

</br>


#### MÉTODOS ESTÁTICOS

Los métodos estáticos se definen con el decorador `@staticmethod` y no tienen como parámetro ni la instancia ni la clase. Es por ello por lo que el uso de estos métodos previenen el poder modificarlas y son usados como métodos que aportan utilidades concretas.

Los métodos estáticos se pueden ver como funciones normales con la particularidad de que van ligadas a una clase concreta.

</br>

```python
class Clase:
    @staticmethod
    def metodoestatico():
        return "Método estático"
        
Clase.metodoestatico()

mi_clase = Clase()
mi_clase.metodoestatico()

# 'Método estático'
# 'Método estático'
```

</br>


#### MÉTODOS ABSTRACTOS

Los métodos abstractos son aquellos que son declarados pero no tienen una implementación directa en la clase. Su finalidad es que las clases que hereden de esta estén obligadas a hacer su propia implementación de este método.

Se definen con el decorador `@abstractmethod` y son frecuentemente usados crear interfaces que faciliten la comunicación entre diferentes clases. Vemos un ejemplo a continuación:

</br>

```python
from abc import ABC, abstractmethod
class Clase(metaclass=ABCMeta):
    @abstractmethod
    def metodo_abstracto(self):
        pass
```
</br>



### HERENCIA

La herencia es un proceso mediante el cual se puede crear una clase hija o *child* que hereda de una clase padre o *parent*.
Esto permite que la clase hija acceda a los métodos y atributos definidos por la clase padre. Igualmente una clase hija puede definir sus propios métodos y atributos o incluso sobrescribir los de la clase padre.

Se puede crear una clase hija simplemente pasando como parámetro la clase padre de la que queremos heredar. Vemos un ejemplo de ello a continuación:

</br>

```python
# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass
```

</br>


El proceso de la herencia de clases resulta muy ventajoso porque nos permite ahorrar la repetición de código y nos ayuda a tener bien organizadas todas nuestras clases. Facilita el mantenimiento del programa y la implementación de nuevas funcionalidades.

Sin embargo, esto requiere un esfuerzo previo para saber cómo vamos a planificar la herencia entre las diferentes clases. Se debe hacer en función de qué clases se parecen más y por tanto comparten un mayor número de métodos y atributos.

</br>


Podemos ver una comparación práctica de la herencia de clases viendo la clasificación de los distintos organismos que se hace en biología. Cada especie comparte muchas similitudes con otras especies a diferentes niveles. Por ejemplo, dos especies son más parecidas si comparten la familia que si solo comparten el reino.

</br>

![Arquitectura de un aplicación web](/images/biological_classification.png)

</br>


Podemos ver en el siguiente ejemplo el uso de la herencia para definir múltiples clases que comparten parcialmente las misma funcionalidad:
 
</br>

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)



# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro




class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")




mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()
# Guau!
# Muuu!

mi_vaca.describeme()
mi_abeja.describeme()
# Soy un Animal del tipo Vaca
# Soy un Animal del tipo Abeja

mi_abeja.picar()
# Picar!
```

</br>


Los métodos de la clases heredadas pueden clasificarse en tres tipos diferentes:

- Heredados directamente de la clase padre: describeme()
- Heredados de la clase padre pero modificados: hablar() y moverse()
- Creados en la clase hija por lo tanto no existentes en la clase padre: picar()

</br></br>


Por último cabe mencionar que podemos hacer uso de de la función `super()` desde la clase hija para acceder a los métodos de la clase padre.

Podemos ver su uso en el siguiente ejemplo: 

</br>

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad        
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
```

</br>


También podemos usar `super()` para ampliar el constructor de la clase padre. Vemos un ejemplo de ello a continuación:

</br>

```python
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
        
mi_perro = Perro('mamífero', 7, 'Luis')
mi_perro.especie
mi_perro.edad
mi_perro.dueño
```

</br>


### POLIMORFISMO

El término polimorfismo tiene origen en las palabras griegas *polys* (muchos) y *morpho* (formas). Este concepto aplicado a la programación hace referencia a que los objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz pero que pueden tomar diferentes formas en su respuesta.

Según el principio de polimorfismo podemos llamar a la misma función en diferentes objetos que no pertenecen a la misma clase.
La respuesta a esa llamada debe estar garantizada y ser diferente y específica para cada objeto. Los comportamientos obtenidos deben así ser distintos y "tomar diferentes formas".

Esta característica permite que sin alterar el código existente de un programa se puedan incorporar nuevos comportamientos y funciones aportando así flexibilidad en el diseño del software. Para hacerlo simplemente deben agregarse nuevas clases cuyo único requisito es que deben tener implementados todos los métodos necesarios usados por el programa.

Una manera fácil de asegurarse de ello es que las diferentes clases hereden de la misma clase padre y que esta tenga métodos abstractos definidos en ella. Esto garantiza que todas las clases hija definan esos métodos y por tanto puedan comunicarse con el mismo interfaz.

</br>


Vemos un ejemplo de todo ello a continuación:

</br>

```python
class Animal:
    def hablar(self):
        pass



class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")



for animal in Perro(), Gato():
    animal.hablar()

# Guau!
# Miau!
```


</br></br></br></br></br>




# API

Las siglas API provienen de *Application Programming Interface* y su principal función es servir de intermediario entre dos sistemas. Una API permite que una aplicación se comunique con otra y pida datos o acciones específicas.

Una llamada a la API, o solicitud API, permite a una aplicación solicitar datos o servicios de otra aplicación. La mayoría de las aplicaciones web realizan regularmente llamadas a la API.



Para ser útil, una API tiene que tener documentación. La documentación indica, entre otras cosas, qué tipos de solicitudes acepta la API, qué puede hacer la API, cómo formatea sus respuestas y cuáles son sus puntos finales. Los desarrolladores pueden revisar la documentación de una API e incorporar esta información cuando desarrollan sus aplicaciones.



- **Request** - es la solicitud envidada por el cliente
- **Response** - es la respuesta dada por el servidor

Request y body y resource

carga útil de la petición

Permisos y autentificación














</br>

### ARQUITECTURA DE UNA APLICACIÓN WEB

La estructura básica de una aplicación web consta de los siguientes elementos:

- **CLIENT** - es el cliente o App que solicita la información
- **API** - es el intermediario entre el cliente y el servidor
- **SERVER** - es el servidor web que suministra la información solicitada
- **DATABASE** - es la base de datos donde el servidor guarda toda la información

</br>

En el siguente diagrama podemos ver estos elementos y cómo se comunican entre sí: 

</br>

![Arquitectura de un aplicación web](/images/webapp_architecture.png)

</br>


Para entender bien el funcionamiento de una aplicación web y sus diferentes partes, en especial la función que cumple la API, resulta muy útil hacer una analogía con un restaurante.

Cuando un cliente entra a un restaurante y ve el menú disponible no va directamente a la cocina a servirse su plato. Es el camarero el encargado de atender a los diferentes clientes del restaurante y tomar nota de sus solicitudes para posteriormente comunicárselas a cocina. Cumple así la función de la API.

La cocina puede entenderse como el servidor web donde se preparan todos los platos solicitados. De igual forma la despensa donde se guardan todos los ingredientes puede ser vista como una base de datos. Esos ingrediente no pueden servirse directamente al cliente, deben ser procesados antes de ser servidos.

Una vez preparados los platos solicitados es el camarero quien se los lleva al cliente. En el caso de que falte algún ingrediente o el plato pedido no pueda ser preparado es el camarero el encargado de pasar la información entre la cocina y el cliente y tratar de buscar una solución.

Las funciones del camarero son variadas y muy importantes para el correcto funcionamiento del restaurante. Ayuda a mantener un orden y dar tiempo a los cocineros de preparar todos los platos pedidos a la vez que se asegura de que a cada cliente se le sirva el plato que ha pedido y no el de otro por error. También comprueba de que todas las solicitudes que hacen los clientes puedan prepararse y no estén pidiendo algo que no esté en la carta. 

Entendida la analogía entre el camarero y la API se puede ver que es una pieza clave en la comunicación entre el cliente y y el servidor.

</br>

Se muestra una representación de esta analogía entre una aplicación web y un restaurante a continuación:

</br> 

![Analogía API restaurante](/images/api_restaurant_analogy.png)

</br>


### ARCHIVOS JSON

El nombre de formato JSON proviene de *JavaScript Object Notation* ya que su estructura es muy similar a la de un objeto de de JavaScript. 

Los archivos en formato `.json` son los más usados para el intercambio de información debido a que solo contienen texto plano.  Es por eso que pueden enviarse fácilmente entre computadoras y tienen una compatibilidad muy alta con la mayoría de lenguajes de programación.

En el siguiente ejemplo de archivo `.json` se define un objeto con tres propiedades y sus respectivos valores:

</br>

```json
{
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}
```

</br>

Podemos ver otro ejemplo de archivo `.json` en el que se ve claramente su estructura jerarquizada a continuación:


</br>


```json
{
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}
```

</br>


### MÉTODOS HTTP

Los métodos HTTP son fundamentales en la comunicación entre cliente y servidor ya que indican la acción a realizar con el recurso especificado. Aunque estos también pueden ser sustantivos, estos métodos de solicitud a veces son llamados HTTP verbs. Es importante resaltar que siempre deben escribirse todas sus letras en mayúsculas.

A continuación vemos un lista


Método | Descripción
:---: | -----------
**GET**     | solicita la información completa de un recurso del servidor. No provoca ningún cambio en el servidor. 
**POST**    | crea un nuevo recurso en el servidor. Junto a la solicitud el cliente debe enviar la información para crear el nuevo recurso.
**PUT**     | reemplaza completamente la información de un recurso en el servidor. El cliente debe enviar el recurso al completo al servidor incluso si este ha sido modificado levemente. actualiza completamente el recurso.
**PATCH**   | aplica modificaciones parciales a un recurso
**DELETE**  | borra un recurso en el servidor. El cliente que envía la solicitud debe indicar el recurso a eliminar.

</br>

Podemos ver una lista completa de métodos HTTP en el siguiente [enlace](https://webconcepts.info/concepts/http-method/)

</br>


### SISTEMA REST

Los verbos Http involucrados en un sistema REST son GET, POST, PUT, PATCH y DELETE


En la arquitectura REST, los clientes envían solicitudes para recuperar o modificar recursos y los servidores envían respuestas a estas solicitudes. Echemos un vistazo a las formas estándar de realizar solicitudes y enviar respuestas.

> REST es una arquitectura para aplicaciones en redes (REpresentational State Transfer). RESTful por otro lado, son programas (a modo de web service o API), basados en REST. Muchas veces se usan ambos terminos como sinonimos.

> La API RESTful es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet. La mayoría de las aplicaciones para empresas deben comunicarse con otras aplicaciones internas o de terceros para llevar a cabo varias tareas

> Las API RESTful admiten este intercambio de información porque siguen estándares de comunicación de software seguros, confiables y eficientes.


El término *CRUD* se refiere a las iniciales de las cuatro operaciones básicas que se pueden llevar a cabo en la mayoría de las bases de datos y sistemas de gestión de información:

- [**C**]REATE - crear
- [**R**]EAD - leer
- [**U**]PDATE - actualizar
- [**D**]ELETE - borrar


Haciendo peticiones
REST requiere que un cliente realice una solicitud al servidor para recuperar o modificar datos en el servidor. Una solicitud generalmente consta de:

- **HTTP verb**un verbo HTTP, que define qué tipo de operación realizar
- **header** un encabezado, que permite al cliente transmitir información sobre la solicitud
- **path** un camino hacia un recurso
- **body** un cuerpo de mensaje opcional que contiene datos



</br>


### CÓDIGOS DE ESTADO DE RESPUESTA HTTP

Cuando un cliente hace una solicitud siempre recibe una respuesta. La respuesta recibida no tiene por qué ser la esperada y es por ello que existen una gran variedad de códigos de estado que nos ayudan a identificar cual ha podido ser el error de haberlo habido. Todos los códigos de estado posibles empiezan por uno de los cinco números que se identifican con las cinco categorías en las que se agrupan. Estas categorías son las siguientes:

</br>

1. Respuestas informativas (100 – 199)
2. Respuestas satisfactorias (200 – 299)
3. Respuestas de redireccionamiento (300 – 399)
4. Respuestas de errores de los clientes (400 – 499)
5. Respuestas de errores de los servidores (500 – 599)

</br>

En total hay 63 códigos posibles y podemos ver una descripción de todos ellos a continuación: 

</br>

Códido | Descripción
:----: | ----------- 
1XX | Respuestas informativas
100 | Continúa en
101 | Protocolos de conmutación
102 | Procesando
103 | Primeras pistas
2XX | Respuestas satisfactorias
200 | OK
201 | Creado
202 | Aceptado
203 | Información no autorizada
204 | Sin contenido
205 | Restablecer contenido
206 | Contenido parcial
207 | Multiestado
208 | Ya comunicado
226 | MI Utilizado
3XX | Respuestas de redireccionamiento
300 | Varias opciones
301 | Movido permanentemente
302 | Encontrado
303 | Ver otros
304 | No modificado
307 | Redireccionamiento temporal
308 | Redireccionamiento permanente
4XX | Respuestas de errores de los clientes
400 | Bad request
401 | No autorizado
402 | Pago requerido
403 | Prohibido
404 | No se ha encontrado
405 | Método no permitido
406 | No aceptable
407 | Se requiere autenticación proxy
408 | Tiempo de espera de la solicitud
409 | Conflicto
410 | Gone
411 | Longitud requerida
412 | Condición previa fallida
413 | Contenido demasiado grande
414 | URI demasiado largo
415 | Tipo de soporte no compatible
416 | Alcance no satisfactorio
417 | Expectativa fallida
421 | Petición mal dirigida
422 | Contenido no procesable
423 | Bloqueado
424 | Dependencia fallida
425 | Demasiado pronto
426 | Actualización necesaria
428 | Condición previa requerida
429 | Demasiadas peticiones
431 | Los campos de la cabecera de la solicitud son demasiado grandes
451 | No disponible por motivos legales
5XX | Respuestas de errores de los servidores 
500 | Error interno del servidor
501 | No aplicado
502 | Bad gateway
503 | Servicio no disponible
504 | Tiempo de espera de la puerta de enlace
505 | Versión HTTP no admitida
506 | Variante también negociada
507 | Almacenamiento insuficiente
508 | Bucle detectado
511 | Autenticación de red necesaria

</br> 


Podemos ver una descripción más detallada de todos ellos en el siguiente [enlace](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

</br>

![502 Bad Gateway](/images/502_status_code.png)

</br>


### POSTMAN

Postman es uno de los programas más populares para trabajar en el desarrollo de APIs. Es gratuito y lo puedes usar sin límites, aunque también tiene su versión premium con características extra. Básicamente permite configurar rutas de endpoints del API y ejecutarlas, para ejercitar el backend de las aplicaciones.

Gracias a Postman podemos guardar todas las request que queramos, para tenerlas preparadas y poder ejecutarlas las veces que haga falta. Esto nos facilita mucho el día a día en el desarrollo, pues generalmente tendremos que probar una ruta diversas veces hasta que comprobemos que todo funciona como se esperaba.

Además, Postman permite trabajar cómodamente con todos los métodos del HTTP, como GET, POST, PUT, PATCH, DELETE. Si no tuviéramos algo como Postman necesitaríamos generar código del cliente, con Javascript y generalmente Ajax para poder realizar los request al servidor y probar todos esos métodos, ya que un navegador cuando accedemos a un recurso mediante su URL solo nos permite hacer un simple GET.





Postman es un software de uso gratuito popularmente usado para el desarrollo de APIs. Su principal función es permitirnos comunicarnos directamente con una API y emular las solicitudes que posteriormente harán loa aplicaciones web que se comuniquen con ella.

Podemos realizar cualquiera de las acciones HTTP y recibir la respuesta dada por la API para poder analizarla. El uso de herramientas como postman es de vital importancia para comprobar el funcionamiento de una API durante su desarrollo. Su principal ventaja es que nos ahorra tener que desarrollar una aplicación web

Podemos usar la interfaz gráfica del programa para poder realizar las diferentes solicitudes


[postman.com](https://www.postman.com/)

![Postman](/images/postman_screenshot.png)

Permite automatizar las peticiones

> Postman es una popular herramienta utilizada para probar APIs, permitiendo a los desarrolladores enviar peticiones a servicios web y ver respuestas. Exploraremos cómo Postman puede ser una herramienta esencial para probar APIs eficientemente.

> endpoints

> cuerpo de la solicitud





</br></br></br></br></br>





# MONGODB

MongoDB es una popular base de datos NoSQL de código abierto utilizada por empresas y particulares que necesitan almacenar grandes cantidades de datos. Está diseñada para ofrecer escalabilidad, flexibilidad y rendimiento, lo que la convierte en una de las bases de datos más populares del mundo. Además, es compatible con muchos sistemas operativos y lenguajes de programación.

</br>

![MongoDB](/images/MongoDB.png)

</br>

A diferencia de las bases de datos relacionales, que se basan en una estructura tabular estricta, las bases de datos NoSQL utilizan documentos similares a JSON con esquemas dinámicos para almacenar y consultar los datos.

Los datos no tienen que tener un esquema preconcebido y esto resulta muy útil porque la mayoría de los datos que generan las aplicaciones web y los dispositivos IoT no están estructurados y no se pueden guardar en una base de datos SQL tradicional. Además, muchas empresas almacenan los datos antes de saber cómo se utilizarán en el futuro.

La flexibilidad que aporta esta naturaleza dinámica es la que hace que MongoDB sea tan potente y eficiente. Por ello es utilizado en una gran variedad de aplicaciones entre las que se incluyen:

- **Sitios y aplicaciones web** - almacenar datos de usuario y contenidos
- **Análisis en tiempo real** - almacenar y analizar grandes cantidades de datos en tiempo real de forma rápida y sencilla
- **Sistemas de gestión de contenidos** - almacenar contenidos y medios
- **Aplicaciones móviles** - almacenar datos de usuarios y dispositivos móviles
- **Redes sociales** - almacenar y gestionar perfiles de usuario, publicaciones y otros datos
- **Aplicaciones sanitarias** - almacenar y gestionar grandes cantidades de datos de pacientes de forma segura
- **Plataformas de comercio electrónico** - almacenar datos de clientes, pedidos y otra información

</br>


### ESTRUCTURA DE MONGODB

Una base de datos de MongoDB no se basa en tablas, columnas y filas como lo hacen las bases de datos relacionales tradicionales. En MongoDB los datos se almacenan como colecciones, documentos y campos. En la siguiente tabla podemos ver una equivalencia entre los términos usados en ambas bases de datos:

Término SQL |     | Término MongoDB
:---------: | :-: | :-------------:
Database | - | Database
Table    | - | Collection
Row      | - | Document
Column   | - | Field
Index    | - | Index

</br>


Una base de datos MongoDB es un contenedor de colecciones de igual forma que un RDMS es un contenedor de tablas para las bases de datos relacionales. Un servidor MongoDB puede almacenar múltiples bases de datos.

Una colección es un grupo de documentos de MongoDB y se corresponde con una tabla creada en una base de datos relacional. No tiene una estructura predefinida.

Un documento es el equivalente a un registro en una base de datos tradicional y se compone de pares de nombre y valor que sirven como unidad básica de datos. Cada campo es una asociación entre un nombre y un valor y es similar a una columna en una base de datos relacional.

Cada documento es diferente y puede tener un número variable de campos ya que su estructura corresponde a la forma en que los desarrolladores construyen sus clases y objetos en el lenguaje de programación utilizado. Al carecer de un esquema predefinido los campos pueden añadirse a voluntad y eso facilita la representación de relaciones jerárquicas u otras estructuras complejas.

</br>


A continuación se muestra un diagrama de la estructura de una base de datos MongoDB:

</br>

![Estructura MongoDB](/images/MongoDB_estructura.png)

</br>


### CARACTERÍSTICAS DE MONGODB

Pese a que existen otras bases de datos NoSQL, MongoDB ofrece una serie de grandes características que la hacen destacar del resto. Algunas de esas características son las siguientes:

- Alto rendimiento: MongoDB está diseñada para ofrecer un alto rendimiento y escalabilidad permitiendo así a las empresas manejar cantidades masivas de datos con facilidad.
- Modelado de datos flexible: MongoDB facilita el almacenamiento de diferentes tipos de datos en la misma base de datos. Esto permit un desarrollo más fácil y rápido.
- Alta disponibilidad: MongoDB está diseñada para permanecer disponible incluso cuando hay problemas de hardware o de red, lo que ayuda a garantizar que los datos estén siempre accesibles.
- Transacciones ACID multidocumento: MongoDB soporta transacciones atómicas multidocumento. Esto permite realizar múltiples operaciones en una única transacción.
- Búsqueda integrada: MongoDB tiene capacidades integradas de búsqueda de texto para permitir a los usuarios encontrar rápida y fácilmente los datos que necesitan.
- Alta seguridad: MongoDB está diseñado pensando en la seguridad. Ofrece funciones avanzadas de autenticación y cifrado para garantizar que los datos se mantienen seguros.
- Facilidad de uso: MongoDB es fácil de configurar y usar. Tiene una interfaz de usuario sencilla que facilita a los usuarios una rápida puesta en marcha.

</br>


También cabe destacar que MongoDB incluye una interfaz de aplicación-cliente y un sistema de archivos que permiten a los usuarios interactuar con la base de datos utilizando lenguajes de programación compatibles como Java, JavaScript y Python. MongoDB  incluye igualmente un lenguaje de consulta del lado del servidor, conocido como *MongoDB Query Language* (MQL), que proporciona a los usuarios una sintaxis expresiva para consultar datos.

</br>


### BASES DE DATOS RELACIONALES

Las bases de datos relacionales son sistemas de bases de datos que utilizan tablas para almacenar y organizar la información. Estas tablas contienen una o más categorías de datos en forma de columnas y cada fila o registro contiene un conjunto de datos definidos por cada una de las categorías. Es habitual que muchas de estas tablas estén interrelacionadas entre sí.

Algunas ventajas de las base de datos relacionales son:

- Fáciles de categorizar y almacenar datos estructurados para consultas y filtrado más rápidos
- Fáciles de escalar y no dependen de una organización física
- Modelo de base de datos tradicional muy desarrollado y bien comprendido
- Alto nivel de seguridad

</br>

Un RDBMS (*Relational DataBase Management System*) es un sistema de gestión de bases de datos relacionales. Se usa para crear y gestionar estas bases de datos y también proporciona una forma sistemática de crear, recuperar, actualizar y gestionar los datos.

El lenguaje SQL (*Structured Query Language*) es el usado de forma estándar para trabajar con bases de datos relacionales. Sirve para comunicarse con el RDBMS y permite llevar a cabo tareas como:

- Crear una tabla e insertar datos en ella
- Consulta y filtrado de datos
- Modificación y actualización de datos
- Eliminar datos o tablas

</br>

Las bases de datos NoSQL deben su nombre a que no usan el estándar del lenguaje SQL para poder gestionar sus datos. Hay varias diferencias importantes entre las bases de datos NoSQL y SQL. Vemos un resumen de ellas en la siguiente tabla:

</br>

![Tabla comparativa entre NoSQL y SQL](/images/tabla_NoSQL_vs_SQL.png)

</br></br></br></br></br>





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

Los decoradores de python son una potente herramienta que nos permite modificar el comportamiento de una clase o función. La ventaja que ofrecen estos es que permiten ampliar el funcionamiento sin cambiar su código original.

Vemos el uso de un decorador a continuación:

</br>

```python
def crear_etiqueta_precio(función_original):
    def función_decorada(*args, **kwds):
        print(f'PRECIO: {función_original(*args, **kwds)}¥')
    return función_decorada


@crear_etiqueta_precio
def calcular_precio(beneficio, *costes):
    precio_total = beneficio
    for coste in costes:
        precio_total += coste
        
    return precio_total
            

calcular_precio(100, 300, 200)
#PRECIO: 600¥
```

</br></br>


Los decoradores de python son muy valiosos para escribir código limpio, versátil, reutilizable y fácil de mantener. Esto se debe en gran medida a que con el uso de decoradores podemos agregar funcionalidades complicadas a funciones o clases existentes con solo una línea de código.

En esencia, cualquier función que toma como argumento una función y devuelva otra puede ser usada como un decorador.

</br>


### SINTAXIS

Debemos distinguir tres partes implicadas en la definición y uso de un decorador:

- Definición del decorador
- Definición de la función decorada
- Llamada a la función decorada

</br>

En lo que respecta al decorador, la definición de este se hace como una función normal teniendo en cuenta que debe recibir la función original como parámetro y devolver la función decorada.

Por otra parte se debe hacer la definición de la función decorada. Para ello debemos colocar el símbolo `@` junto al nombre del decorador justo antes de la definición de la función antigua, la cual no necesita ninguna alteración en su código.

Finalmente la llamada a la función decorada se hace de igual forma que se llama a la antigua, no es necesaria ninguna referencia al decorador.

Vemos un ejemplo de todo ello a continuación:

</br>

```python
def informar_ejecución(función_original):
    def función_decorada(*args, **kwds):
        print("Comienza la ejecución de la función")
        función_original(*args, **kwds)
        print("La ejecución ha finalizado")
    return función_decorada


@informar_ejecución
def mandar_emails(*clientes):
    for cliente in clientes:
        print(f'Enviando email a {cliente}')
            

mandar_emails("Oscar", "Tamara", "Asier", "Pablo", "Rosa",)
#Comienza la ejecución de la función
#Enviando email a Oscar
#Enviando email a Tamara
#Enviando email a Asier
#Enviando email a Pablo
#Enviando email a Rosa
#La ejecución ha finalizado
```

</br>


### DECORADORES CON PARÁMETROS

Es posible usar decoradores que admitan parámetros para modificar su comportamiento. Para ello debemos envolver nuevamente nuestro decorador con otra función que los defina. Estos parámetros pueden ser usados dentro del decorador para obtener el comportamiento deseado. Se muestra un ejemplo a continuación:

</br>

```python
def repetir(veces):
    def decorador(función_original):
        def función_decorada(*args, **kwds):
            for vez in range(veces):
                función_original(*args, **kwds)
                     
        return función_decorada
    return decorador


@repetir(3)
def saludo():
    print("¡Hola, mundo!")

saludo()
#¡Hola, mundo!
#¡Hola, mundo!
#¡Hola, mundo!


@repetir(5)
def sumar(*args):
    total = 0
    for arg in args:
        total += arg
    
    print(f'Total = {total}')

sumar(3, 6, 7)
#Total = 16
#Total = 16
#Total = 16
#Total = 16
#Total = 16
```

</br>


### DECORADORES PREDEFINIDOS DE PYTHON

Algunos decoradores pueden usarse directamente ya que corresponden a funciones ya predefinidas en el código de python. A continuación se muestran algunos ejemplos:

Decorador | Descripción
--------- | -----------
@classmethod    | Define un método de clase
@staticmethod   | Define un método estático
@abstractmethod | Define un método abstracto
@property       | Define el *getter* y el *setter* de una propiedad

</br>


Vemos el uso del decorador `@property` en el siguiente ejemplo:

</br>

```python
class Casa:
    def __init__(self, precio):
        self.__precio = precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_valor):
        if nuevo_valor != "":
            print(f'Modificando el precio a {nuevo_valor}')
            self.__precio = nuevo_valor
        else:
            print("Error. Se debe pasar un valor")
            

mansión = Casa("1.200.000€")

mansión.precio = "900.000€"
#Modificando el precio a 900.000€

print(mansión.precio)
#900.000€
```

</br>


### USOS COMUNES

Algunos de los usos comunes que se dan a los decoradores en python son:

- Almacenamiento en caché
- Registro
- Temporización
- Autenticación
- Autorización
- Validación

</br>


Vemos un ejemplo de uso para comprobar si un usuario está autorizado a continuación:

</br>

```python
usuario_autorizado = False

def requiere_autenticación(función_original):
    def función_decorada(*args, **kwargs):
        if not usuario_autorizado:
            print("Error. Usuario no autorizado")
        else:
            return función_original(*args, **kwargs)
    return función_decorada


@requiere_autenticación
def ejecutar_comando(comando):
    print(f'Ejecutando el comando: {comando}')

    
ejecutar_comando("BORRAR")
#Error. Usuario no autorizado
```
