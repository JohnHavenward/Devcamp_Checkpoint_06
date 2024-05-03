

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
class Vehículo:
    color = "rojo"
    ruedas = 4
    
               
print(f'El vehículo es de color {Vehículo.color} y tiene {Vehículo.ruedas} ruedas.')
#El vehículo es de color rojo y tiene 4 ruedas.
```

</br>


### INSTANCIAS

La creación de una instancia, también llamada instanciación de una clase, es el proceso de crear un objeto a partir de la plantilla definida por la clase. 

Una clase puede tener tantas instancias creadas como se quiera.

Para acceder a los métodos y atributos de la instancia se usa el operador `.` tal y como vemos a continuación:

```python
class Alerta:
    def __init__(self, identificador, hora):
        self.identificador = identificador
        self.hora = hora
  
    def informar(self):
        print(f'La alerta "{self.identificador}" está programada para las {self.hora}h')


alerta_1 = Alerta("Reunión", "10:30")
alerta_2 = Alerta("Comida", "14:00")


print(alerta_1.identificador) #Reunión
alerta_2.informar() #La alerta "Comida" está programada para las 14:00h
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
class Pasajero:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


pasajero_1 = Pasajero("Ismael", "García", 57)
pasajero_2 = Pasajero("Helena", "Salgado", 44)
pasajero_3 = Pasajero("Lucía", "Blanco", 31)
```

</br>


### ATRIBUTOS

Un atributo es una variable que forma parte de una clase. La única diferencia con una variable normal de python es que un atributo siempre debe estar asociado a una clase.

Una clase puede contener tantos atributos como se quiera.

Hay dos tipos de atributos dentro de una clase:

- Atributos de clase
- Atributos de instancia
</br>

Los atributos de clase son comunes a todas las instancias y se definen directamente dentro de la clase. El valor de un atributo de clase es único y compartido por todas las instancias y la propia clase. Si alguno de los objetos asociados a ella cambia su valor lo hace también para el resto. Podemos ver un ejemplo de ello a continuación:

```python
class Concursante:
    premio_acumulado = 300
  
    def __init__(self, nombre):
        self.nombre = nombre


concursante_1 = Concursante("Sonia")
concursante_2 = Concursante("Ruth")
concursante_3 = Concursante("Nicolás")


print(Concursante.premio_acumulado) #300

Concursante.premio_acumulado += 50
print (concursante_1.premio_acumulado) #350

Concursante.premio_acumulado += 100
print (concursante_2.premio_acumulado) #450

Concursante.premio_acumulado += 250
print (concursante_3.premio_acumulado) #700
```
</br>

Los atributos de instancia son propios de cada instancia y se definen dentro del método `__init__()`. Cada instancia tiene un valor propio para cada atributo.  Si una instancia cambia el valor de su atributo no afecta al resto de las instancias. Además la clase en sí no tiene definidos estos atributos y por tanto no tiene acceso a ellos. Podemos ver la definición y uso de atributos de instancia en el siguiente ejemplo:

```python
class Cuenta:
  def __init__(self, titular, fondos):
    self.titular = titular
    self.fondos = fondos


cuenta_1 = Cuenta("Carmen", 1900)
cuenta_2 = Cuenta("Antonio", 2700)

print (cuenta_1.titular + " : " + str(cuenta_1.fondos) + "$") #Carmen : 1900$ 
print (cuenta_2.titular + " : " + str(cuenta_2.fondos) + "$") #Antonio : 2700$
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


Los métodos de instancia son los métodos definidos normalmente dentro de la clase. Aparte de `self` pueden definir otros parámetros tal y como vemos en el siguiente ejemplo:

</br>

```python
class Trapo:
    def limpiar(self, objeto):
        print(f'Limpiando {objeto}')


mi_trapo = Trapo()


mi_trapo.limpiar("mesa") #Limpiando mesa
mi_trapo.limpiar("silla") #Limpiando silla
```

</br>


#### MÉTODOS DE CLASE

Los métodos de clase se definen con el decorador `@classmethod` y usan el parámetro `cls` en lugar de `self`. Este parámetro hace referencia a la clase del objeto y no a la instancia. Es por ello que solo pueden acceder y modificar a la clase y en ningún caso pueden hacerlo a la propia instancia.

Pueden llamarse desde la clase o la instancia indistintamente. Vemos un ejemplo a continuación:

```python
class Concursante:
    premio_acumulado = 0
  
    @classmethod
    def acumular_premio(cls, premio):
        cls.premio_acumulado += premio


concursante_1 = Concursante()
concursante_2 = Concursante()


print(Concursante.premio_acumulado) #0

Concursante.acumular_premio(50)
print(Concursante.premio_acumulado) #50

concursante_1.acumular_premio(100)
print(Concursante.premio_acumulado) #150

concursante_2.acumular_premio(100)
print(Concursante.premio_acumulado) #250
```

</br>


#### MÉTODOS ESTÁTICOS

Los métodos estáticos se definen con el decorador `@staticmethod` y no tienen como parámetro ni la instancia ni la clase. Es por ello por lo que el uso de estos métodos previenen el poder modificarlas y son usados como métodos que aportan utilidades concretas.

Los métodos estáticos se pueden ver como funciones normales con la particularidad de que van ligadas a una clase concreta. En el siguiente ejemplo se muestra su uso:

</br>

```python
class Matemáticas:
    @staticmethod
    def sumar(a, b):
        return a + b
        
    @staticmethod
    def multiplicar(a, b):
        return a * b


print(Matemáticas.sumar(5, 3)) #8
print(Matemáticas.multiplicar(5, 3)) #15
```

</br>


#### MÉTODOS ABSTRACTOS

Los métodos abstractos son aquellos que son declarados pero no tienen una implementación directa en la clase. Su finalidad es que las clases que hereden de esta estén obligadas a hacer su propia implementación de este método.

Se definen con el decorador `@abstractmethod` (incluido en el módulo `abc` de python) y son frecuentemente usados para crear interfaces que faciliten la comunicación entre diferentes clases. Vemos un ejemplo a continuación:

</br>

```python
from abc import abstractmethod

class Herramienta:    
    @abstractmethod
    def describir_funcionamiento(self):
        pass
      

class Taladro(Herramienta):
    def describir_funcionamiento():
        print("Esta herramienta sirve para hacer agujeros.")
        
Taladro.describir_funcionamiento() #Esta herramienta sirve para hacer agujeros.
```
</br>



### HERENCIA

La herencia es un proceso mediante el cual se puede crear una clase hija o *child* que hereda de una clase padre o *parent*.
Esto permite que la clase hija acceda a los métodos y atributos definidos por la clase padre. Igualmente una clase hija puede definir sus propios métodos y atributos o incluso sobrescribir los de la clase padre.

Se puede crear una clase hija simplemente pasando como parámetro la clase padre de la que queremos heredar. Vemos un ejemplo de ello a continuación:

</br>

```python
class Animal:
    tamaño = "grande"
    patas = 4
    vuelo = False
    
    @classmethod
    def describir(cls):
        print(f'Este animal es {cls.tamaño}, tiene {cls.patas} patas y {"puede volar" if cls.vuelo else "no puede volar"}.')
    

class Gato(Animal):
    tamaño = "mediano"
    
    
class Pájaro(Animal):
    tamaño = "pequeño"
    patas = 2
    vuelo = True
    
    
Gato.describir() #Este animal es mediano, tiene 4 patas y no puede volar.

Pájaro.describir() #Este animal es pequeño, tiene 2 patas y puede volar.
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
class Invento:
    fecha = "Desconocida"
    inventor = "Desconocido"
    
    def __init__(self, propietario, identificador):
        self.propietario = propietario
        self.identificador = identificador

    def describir(self):
        pass

    def mostrar_datos(self):
        print("Nombre: " + type(self).__name__ + "  Fecha: " + str(self.fecha) + "  Inventor: " + self.inventor)


class Teléfono(Invento):
    fecha = 1876
    inventor = "Alexander Graham Bell"

    def describir(self):
        print("El teléfono es un dispositivo de telecomunicación creado para transmitir señales acústicas a distancia por medio de señales eléctricas.")


class Imprenta(Invento):
    fecha = 1440
    inventor = "Johannes Gutenberg"

    def describir(self):
        print("La imprenta es un método mecánico destinado a reproducir textos e imágenes sobre papel, vitela, tela u otro material.")

    def dato_curioso(self):
        print("La biblia de Gutenberg fue el primer libro impreso de la historia y se imprimió con un total de 42 líneas por cada página.")


class Telescopio(Invento):
    fecha = 1608
    inventor = "Hans Lippershey"

    def describir(self):
        print("El telescopio es un instrumento óptico que permite observar objetos lejanos con mucho más detalle que a simple vista")


teléfono_963 = Teléfono("Museo Metropolitano", "ET-963")
imprenta_120 = Imprenta("Biblioteca Antigua", "GG-120")
telescopio_568 = Telescopio("Planetario Central", "FH-568")


teléfono_963.mostrar_datos() #Nombre: Teléfono  Fecha: 1876  Inventor: Alexander Graham Bell
teléfono_963.describir() #El teléfono es un dispositivo de telecomunicación creado para transmitir señales acústicas a distancia por medio de señales eléctricas.

imprenta_120.mostrar_datos() #Nombre: Imprenta  Fecha: 1440  Inventor: Johannes Gutenberg
imprenta_120.describir() #La imprenta es un método mecánico destinado a reproducir textos e imágenes sobre papel, vitela, tela u otro material.
imprenta_120.dato_curioso() #La biblia de Gutenberg fue el primer libro impreso de la historia y se imprimió con un total de 42 líneas por cada página.

telescopio_568.mostrar_datos() #Nombre: Telescopio  Fecha: 1608  Inventor: Hans Lippershey
telescopio_568.describir() #El telescopio es un instrumento óptico que permite observar objetos lejanos con mucho más detalle que a simple vista
```

</br>


Los métodos de la clases heredadas pueden clasificarse en tres tipos diferentes:

- Heredados directamente de la clase padre: mostrar_datos()
- Heredados de la clase padre pero modificados: describir()
- Creados en la clase hija por lo tanto no existentes en la clase padre: dato_curioso()

</br></br>


Por último cabe mencionar que podemos hacer uso de de la función `super()` desde la clase hija para acceder a los métodos de la clase padre y poder ampliar el constructor. Vemos un ejemplo de ello a continuación:

</br>

```python
class Construcción:
    def __init__(self, altura):
        self.altura = altura
        print(f'Se trata de una construcción {self.altura}.')

        
class Casa(Construcción):
    def __init__(self, altura, material):
        super().__init__(altura)
        self.material = material
        print(f'En concreto una casa de {self.material}.')
 
          
mi_casa = Casa("alta", "piedra")
#Se trata de una construcción alta.
#En concreto una casa de piedra.
```

</br>


### POLIMORFISMO

El término polimorfismo tiene origen en las palabras griegas *polys* (muchos) y *morpho* (formas). Este concepto aplicado a la programación hace referencia a que los objetos de diferentes clases pueden ser accedidos utilizando el mismo interfaz pero que pueden tomar diferentes formas en su respuesta.

Según el principio de polimorfismo podemos llamar a la misma función en diferentes objetos que no pertenecen a la misma clase.
La respuesta a esa llamada debe estar garantizada y ser diferente y específica para cada objeto. Los comportamientos obtenidos deben así ser distintos y "tomar diferentes formas".

Esta característica permite que sin alterar el código existente de un programa se puedan incorporar nuevos comportamientos y funciones aportando así flexibilidad en el diseño del software. Para hacerlo simplemente se agregan nuevas clases cuyo único requisito es que deben tener implementados todos los métodos necesarios usados por el programa.

Una manera fácil de asegurarse de ello es que las diferentes clases hereden de la misma clase padre y que esta tenga métodos abstractos definidos en ella. Esto garantiza que todas las clases hija definan esos métodos y por tanto puedan comunicarse con el mismo interfaz.

</br>


Vemos un ejemplo de todo ello a continuación:

</br>

```python
from abc import abstractmethod

class Forma:   
    @abstractmethod
    def calcular_perímetro():
        pass
      
    @abstractmethod
    def calcular_área():
        pass
      

class Cuadrado(Forma):
    def calcular_perímetro():
        print("Se suman los cuatro lados")

    def calcular_área():
        print("Se multiplica la base por la altura")
        
        
class Triángulo(Forma):
    def calcular_perímetro():
        print("Se suman los tres lados")

    def calcular_área():
        print("Se multiplica la base por la altura y se divide entre dos")


Cuadrado.calcular_perímetro() #Se suman los cuatro lados
Cuadrado.calcular_área() #Se multiplica la base por la altura

Triángulo.calcular_perímetro() #Se suman los tres lados
Triángulo.calcular_área() #Se multiplica la base por la altura y se divide entre dos
```


</br></br></br></br></br>




# API

Las siglas API provienen de *Application Programming Interface* y su principal función es servir de intermediario entre dos sistemas. Una API permite que una aplicación se comunique con otra y pida datos o acciones específicas.

Una llamada a la API, o solicitud API, permite a una aplicación solicitar datos o servicios de otra aplicación. La mayoría de las aplicaciones web realizan regularmente llamadas a la API.



Una API define las reglas que se deben seguir para comunicarse con otros sistemas de software. Los desarrolladores exponen o crean API para que otras aplicaciones puedan comunicarse con sus aplicaciones mediante programación.


Se puede pensar en una API web como una puerta de enlace entre los clientes y los recursos de la Web.


Clientes

Los clientes son usuarios que desean acceder a información desde la Web. El cliente puede ser una persona o un sistema de software que utiliza la API.

Recursos

Los recursos son la información que diferentes aplicaciones proporcionan a sus clientes. Los recursos pueden ser imágenes, videos, texto, números o cualquier tipo de datos. (servidor)


Para ser útil, una API tiene que tener documentación. La documentación indica, entre otras cosas, qué tipos de solicitudes acepta la API, qué puede hacer la API, cómo formatea sus respuestas y cuáles son sus puntos finales.



- **Request** - es la solicitud envidada por el cliente
- **Response** - es la respuesta dada por el servidor



La transferencia de estado representacional (REST) es una arquitectura de software que impone condiciones sobre cómo debe funcionar una API. En un principio, REST se creó como una guía para administrar la comunicación en una red compleja como Internet.

Los desarrolladores de API pueden diseñar API por medio de varias arquitecturas diferentes. Las API que siguen el estilo arquitectónico de REST se llaman API RESTful.




En el estilo arquitectónico REST se lleva a cabo la separación entre cliente y servidor. La implementación de ambas partes se puede realizar de forma independiente sin que cada uno conozca al otro. Esto significa que el código del lado del cliente se puede cambiar en cualquier momento sin afectar el funcionamiento del servidor, y el código del lado del servidor se puede cambiar sin afectar el funcionamiento del cliente. La única condición es que cada parte mantenga el formato de mensaje que debe enviar a la otra.


Un *endpoint* o punto final es el lugar donde se realizan las solicitudes a la API.
(conocidas como llamadas API).

la URL de un punto final de la API es como un número de teléfono para hacer llamadas API.

Un servidor de API puede alojar uno o varios puntos finales de la API, lo que significa que aceptará y procesará las llamadas dirigidas a las URL de esos puntos finales. Los clientes de la API también necesitan tener una URL para que el servidor de la API sepa dónde enviar sus respuestas, del mismo modo que Bob y Alice necesitan un número de teléfono para llamarse. Los desarrolladores establecen esta URL cuando desarrollan sus aplicaciones.

Una URL siempre incluye el protocolo de la capa de aplicación, como HTTP, utilizado para llegar a ella. La mayoría de las API web utilizan HTTP, por lo que se incluye en la URL del punto final de la API.




Permisos y autentificación

Una API no acepta llamadas de cualquier cliente. Por estas razones, el servidor de la API tiene que asegurarse de que el cliente del que procede la llamada es conocido y de confianza. La verificación de la identidad se hace mediante la autenticación.




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

Los verbos Http involucrados en un sistema REST son GET, POST, PUT, PATCH y DELETE.


En la arquitectura REST, los clientes envían solicitudes para recuperar o modificar recursos y los servidores envían respuestas a estas solicitudes. Echemos un vistazo a las formas estándar de realizar solicitudes y enviar respuestas.

> REST es una arquitectura para aplicaciones en redes (REpresentational State Transfer). RESTful por otro lado, son programas (a modo de web service o API), basados en REST. Muchas veces se usan ambos terminos como sinonimos.

> La API RESTful es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet. La mayoría de las aplicaciones para empresas deben comunicarse con otras aplicaciones internas o de terceros para llevar a cabo varias tareas

> Las API RESTful admiten este intercambio de información porque siguen estándares de comunicación de software seguros, confiables y eficientes.


El término *CRUD* se refiere a las iniciales de las cuatro operaciones básicas que se pueden llevar a cabo en la mayoría de las bases de datos y sistemas de gestión de información:

- [**C**]REATE - crear
- [**R**]EAD - leer
- [**U**]PDATE - actualizar
- [**D**]ELETE - borrar

Crear, Leer, Actualizar y Eliminar (CRUD) son las cuatro funciones básicas que los modelos deberían poder realizar, como máximo.
Crear, leer, actualizar, eliminar
Cuando creamos API, queremos que nuestros modelos proporcionen cuatro tipos básicos de funcionalidad. El modelo debe poder crear, leer, actualizar y eliminar recursos. Los informáticos suelen referirse a estas funciones con el acrónimo CRUD. Un modelo debe tener la capacidad de realizar como máximo estas cuatro funciones para ser completo. Si una acción no puede describirse mediante una de estas cuatro operaciones, entonces debería ser potencialmente un modelo en sí misma.




Haciendo peticiones

REST requiere que un cliente realice una solicitud al servidor para recuperar o modificar datos en el servidor. Una solicitud generalmente consta de:

- **HTTP verb**un verbo HTTP, que define qué tipo de operación realizar
- **header** un encabezado, que permite al cliente transmitir información sobre la solicitud
- **path** una ruta hacia un recurso
- **body** un cuerpo de mensaje opcional que contiene datos



¿Qué contiene la solicitud del cliente de la API RESTful?

Las API RESTful requieren que las solicitudes contengan los siguientes componentes principales:

Identificador único de recursos

El servidor identifica cada recurso con identificadores únicos de recursos. En los servicios REST, el servidor por lo general identifica los recursos mediante el uso de un localizador uniforme de recursos (URL). El URL especifica la ruta hacia el recurso. Un URL es similar a la dirección de un sitio web que se ingresa al navegador para visitar cualquier página web. El URL también se denomina punto de conexión de la solicitud y especifica con claridad al servidor qué requiere el cliente.

Método

Los desarrolladores a menudo implementan API RESTful mediante el uso del protocolo de transferencia de hipertexto (HTTP). Un método de HTTP informa al servidor lo que debe hacer con el recurso. A continuación, se indican cuatro métodos de HTTP comunes:

GET

Los clientes utilizan GET para acceder a los recursos que están ubicados en el URL especificado en el servidor. Pueden almacenar en caché las solicitudes GET y enviar parámetros en la solicitud de la API RESTful para indicar al servidor que filtre los datos antes de enviarlos.

POST

Los clientes usan POST para enviar datos al servidor. Incluyen la representación de los datos con la solicitud. Enviar la misma solicitud POST varias veces produce el efecto secundario de crear el mismo recurso varias veces.

PUT

Los clientes utilizan PUT para actualizar los recursos existentes en el servidor. A diferencia de POST, el envío de la misma solicitud PUT varias veces en un servicio web RESTful da el mismo resultado.

DELETE

Los clientes utilizan la solicitud DELETE para eliminar el recurso. Una solicitud DELETE puede cambiar el estado del servidor. Sin embargo, si el usuario no cuenta con la autenticación adecuada, la solicitud fallará.

Encabezados de HTTP

Los encabezados de solicitudes son los metadatos que se intercambian entre el cliente y el servidor. Por ejemplo, el encabezado de la solicitud indica el formato de la solicitud y la respuesta, proporciona información sobre el estado de la solicitud, etc.

Datos

Las solicitudes de la API REST pueden incluir datos para que los métodos POST, PUT y otros métodos HTTP funcionen de manera correcta.

Parámetros

Las solicitudes de la API RESTful pueden incluir parámetros que brindan al servidor más detalles sobre lo que se debe hacer. A continuación, se indican algunos tipos de parámetros diferentes:

Los parámetros de ruta especifican los detalles del URL.
Los parámetros de consulta solicitan más información acerca del recurso.
Los parámetros de cookie autentican a los clientes con rapidez.



¿Qué contiene la respuesta del servidor de la API RESTful?

Los principios de REST requieren que la respuesta del servidor contenga los siguientes componentes principales:

Línea de estado

La línea de estado contiene un código de estado de tres dígitos que comunica si la solicitud se procesó de manera correcta o dio error. Por ejemplo, los códigos 2XX indican el procesamiento correcto, pero los códigos 4XX y 5XX indican errores. Los códigos 3XX indican la redirección de URL.

A continuación, se enumeran algunos códigos de estado comunes:

200: respuesta genérica de procesamiento correcto
201: respuesta de procesamiento correcto del método POST
400: respuesta incorrecta que el servidor no puede procesar
404: recurso no encontrado
Cuerpo del mensaje

El cuerpo de la respuesta contiene la representación del recurso. El servidor selecciona un formato de representación adecuado en función de lo que contienen los encabezados de la solicitud. Los clientes pueden solicitar información en los formatos XML o JSON, lo que define cómo se escriben los datos en texto sin formato. Por ejemplo, si el cliente solicita el nombre y la edad de una persona llamada John, el servidor devuelve una representación JSON como la siguiente:

'{"name":"John", "age":30}'

Encabezados

La respuesta también contiene encabezados o metadatos acerca de la respuesta. Estos brindan más contexto sobre la respuesta e incluyen información como el servidor, la codificación, la fecha y el tipo de contenido.



CRUD and REST
In a REST environment, CRUD often corresponds to the HTTP methods POST, GET, PUT, and DELETE, respectively. These are the fundamental elements of a persistent storage system.

Throughout the rest of the article, we will recommend standards and response codes that are typically followed by developers when creating RESTful applications. Conventions may differ so feel free to experiment with different return values and codes as you become comfortable with the CRUD paradigm.

Imagine we are working with a system that is keeping track of meals and their corresponding prices for a restaurant. Let’s look at how we would implement CRUD operations.

CREATE

Request:

POST http://www.myrestaurant.com/dishes/

Body -

{
  "dish": {
    "name": “Avocado Toast”,
    "price": 8
  }
}

Response:

Status Code - 201 (CREATED)

Body -

{
  "dish": {
    "id": 1223,
    "name": “Avocado Toast”,
    "price": 8
  }
}


READ

Request:

GET http://www.myrestaurant.com/dishes/

Response: Status Code - 200 (OK)

Body -

{
  "dishes": [
    {
      "id": 1,
      "name": “Spring Rolls”,
      "price": 6
    },
    {
      "id": 2,
      "name": “Mozzarella Sticks”,
      "price": 7
    },
    ...
    {
      "id": 1223,
      "name": “Avocado Toast”,
      "price": 8
    },
    {
      "id": 1224,
      "name": “Muesli and Yogurt”,
      "price": 5
    }
  ]
}

read a specific item

Request:

GET http://www.myrestaurant.com/dishes/1223

Response: Status Code - 200 (OK)

Body -

{
  "id": 1223,
  "name": “Avocado Toast”,
  "price": 8
}


UPDATE

Request:

PUT http://www.myrestaurant.com/dishes/1223
Body -

{
  "dish": {
    "name": “Avocado Toast”,
    "price": 10
  }
}


Response: Status Code - 200 (OK)

Body -

{
  "dish": {
    "name": “Avocado Toast”,
    "price": 10
  }
}


DELETE

Request:

DELETE http://www.myrestaurant.com/dishes/1223


Response: Status Code - 204 (NO CONTENT)

Body - None

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

Básicamente permite configurar rutas de endpoints del API y ejecutarlas, para ejercitar el backend de las aplicaciones.

Gracias a Postman podemos guardar todas las request que queramos, para tenerlas preparadas y poder ejecutarlas las veces que haga falta. Esto nos facilita mucho el día a día en el desarrollo, pues generalmente tendremos que probar una ruta diversas veces hasta que comprobemos que todo funciona como se esperaba.

A través del cliente API, puede organizar solicitudes en Colecciones Postman para ayudarlo a organizar sus solicitudes para su reutilización, de modo que no pierda tiempo creando todo desde cero. Sus colecciones también pueden contener código JavaScript para vincular solicitudes o automatizar flujos de trabajo comunes, y puede usar secuencias de comandos para visualizar sus respuestas API como cuadros y gráficos.




Además, Postman permite trabajar cómodamente con todos los métodos del HTTP, como GET, POST, PUT, PATCH, DELETE.

Postman es un software de uso gratuito popularmente usado para el desarrollo de APIs. Su principal función es permitirnos comunicarnos directamente con una API y emular las solicitudes que posteriormente harán las aplicaciones web que se comuniquen con ella.

Podemos realizar cualquier solicitud y recibir la respuesta dada por la API para poder analizarla.

El uso de herramientas como postman es de vital importancia para comprobar el funcionamiento de una API durante su desarrollo. Su principal ventaja es poder emular las solicitudes realizadas a la API y nos ahorra así tener que desarrollar una aplicación web real.

Podemos usar la interfaz gráfica del programa para poder realizar las diferentes solicitudes


Postman también nos ayuda a generar automáticamente documentación para nuestra API. Esto permite que futuros usuarios tengan una guía de referencia para utilizarla.

and format text inside the body to make inspection easy



[postman.com](https://www.postman.com/)

![Postman](/images/postman_screenshot.png)

Permite automatizar las peticiones


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
