# Archivo: alquiler_equipo.py
# Descripción: Servicio de alquiler de equipos.
# Importa la clase Servicio.
from modelos.servicio import Servicio


# ______________Clase AlquilerEquipo que hereda de Servicio______________
class AlquilerEquipo(Servicio):

    # Constructor.
    def __init__(self, codigo, nombre, costo_base, tipo_equipo):
        
        super().__init__(codigo, nombre, costo_base) # Llama al constructor de la clase padre.       
        self.tipo_equipo = tipo_equipo # Asigna el tipo de equipo utilizando el setter.
         
    @property  # Propiedad tipo_equipo
    def tipo_equipo(self):
        return self._tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, tipo):

        if not tipo.strip():
            raise ValueError("Debe indicar el tipo de equipo.")

        self._tipo_equipo = tipo
    
    def calcular_costo(self, dias=1, descuento=0): # Calcula el costo del alquiler.

        if dias <= 0:
            raise ValueError("Los días deben ser mayores que cero.")

        costo = self.costo_base * dias

        costo -= costo * (descuento / 100)

        return costo
    
    def descripcion(self): # Devuelve la descripción del servicio.

        return (
            f"Alquiler de equipo tipo "
            f"{self.tipo_equipo}."
        )
    
    def mostrar_informacion(self): # Sobrescribe mostrar_informacion().

        return (
            f"{super().mostrar_informacion()}\n"
            f"Tipo de equipo: {self.tipo_equipo}"
        )