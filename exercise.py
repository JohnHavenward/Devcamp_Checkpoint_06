#Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

class Usuario:
  def __init__(self, nombre_usuario, contraseña):
    self.nombre_usuario = nombre_usuario
    self.contraseña = contraseña

mi_usuario = Usuario("John", "manzana")