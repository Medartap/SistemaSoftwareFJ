# Archivo: asesoria.py
# Descripción: Clase que representa el servicio de asesoría.
# Importa la clase Servicio.
from modelos.servicio import Servicio

# _____________Clase Asesoria que hereda de Servicio.________________
class Asesoria(Servicio):
    # Constructor.
    def __init__(self, codigo, nombre, costo_base, especialidad):
        
        super().__init__(codigo, nombre, costo_base) # Llama al constructor de la clase padre.        
        self.especialidad = especialidad # Asigna la especialidad.      
   
    @property  # Propiedad especialidad
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, especialidad):

        if not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")

        self._especialidad = especialidad
    
    def calcular_costo(self, horas=1): # Calcula el costo de la asesoría.

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        return self.costo_base * horas
   
    def descripcion(self):  # Devuelve la descripción del servicio.

        return (
            f"Asesoría especializada en {self.especialidad}."
        )
    
    def mostrar_informacion(self): # Muestra la información del servicio.

        return (
            f"{super().mostrar_informacion()}\n"
            f"Especialidad: {self.especialidad}"
        )