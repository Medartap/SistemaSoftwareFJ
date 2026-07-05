# Archivo: servicio.py
# Descripción: Implementación de la clase abstracta Servicio del sistema Software FJ.
# Importa la clase abstracta Entidad.

from modelos.entidad import Entidad

# Importa las herramientas para crear métodos abstractos.
from abc import abstractmethod


# ____________________Clase abstracta Servicio_________________________
class Servicio(Entidad): # Clase base para todos los servicios ofrecidos por el sistema.

    # Constructor.
    def __init__(self, codigo, nombre, costo_base):
        
        super().__init__(codigo) # Llama al constructor de la clase padre.        
        self.nombre = nombre # Asigna los valores utilizando los setters.
        self.costo_base = costo_base     
   
    @property # Propiedad nombre
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):

        if not nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        self._nombre = nombre       
    
    @property  # Propiedad costo_base
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, costo):

        if costo <= 0:
            raise ValueError("El costo debe ser mayor que cero.")

        self._costo_base = costo
    
    @abstractmethod # Método abstracto para calcular el costo.
    def calcular_costo(self):
        pass

    
    @abstractmethod # Método abstracto para describir el servicio.
    def descripcion(self):
        pass
   
    def mostrar_informacion(self): # Implementación del método heredado.

        return (
            f"Código: {self.codigo}\n"
            f"Servicio: {self.nombre}\n"
            f"Costo Base: ${self.costo_base:,.0f}"
        )