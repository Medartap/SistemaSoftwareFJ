
# Descripción:
# Clase abstracta que representa una entidad general del sistema.
# De esta clase se heredarán Cliente y Servicio.
# Importa la clase ABC (Abstract Base Class) y el decorador abstractmethod.
# Estas herramientas permiten crear clases y métodos abstractos.
from abc import ABC, abstractmethod

# ______________________Clase abstracta Entidad______________________________
# Esta clase representa una entidad general del sistema.
# No se puede crear un objeto directamente de esta clase.
# Las clases hijas estarán obligadas a implementar el método
# mostrar_informacion().

class Entidad(ABC):

    # Recibe un código único para identificar la entidad.  
    def __init__(self, codigo):        
        self._codigo = codigo # Guarda el código como un atributo protegido.        
    
    @property # Permite consultar el código sin acceder directamente al atributo.
    def codigo(self): 
        
        return self._codigo# Retorna el código almacenado.   
       
    @codigo.setter # Permite modificar el código cuando sea necesario.
    def codigo(self, codigo):
        
        self._codigo = codigo # Actualiza el valor del código.

   
    # Método abstracto.
    # Todas las clases hijas deberán implementar este método.  
    @abstractmethod
    def mostrar_informacion(self):        
       
        pass # La implementación estará en las clases hijas.