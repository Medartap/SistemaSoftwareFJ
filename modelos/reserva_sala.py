# Archivo: reserva_sala.py
# Descripción: Servicio de reserva de salas.
# Importa la clase Servicio.
from modelos.servicio import Servicio

# _________________Clase ReservaSala que hereda de Servicio________________
class ReservaSala(Servicio):
    # Constructor.
    def __init__(self, codigo, nombre, costo_base, capacidad):
        
        super().__init__(codigo, nombre, costo_base) # Llama al constructor de la clase padre.       
        self.capacidad = capacidad # Asigna la capacidad utilizando el setter
          
    @property # Propiedad capacidad
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad):

        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

        self._capacidad = capacidad

    
   
    def calcular_costo(self, horas=1, descuento=0): # Calcula el costo de la reserva.
          # descuento es opcional y permite aplicar promociones.
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        costo = self.costo_base * horas
        costo -= costo * (descuento / 100)

        return costo
    
    def descripcion(self): # Devuelve la descripción del servicio.

        return (
            f"Reserva de sala para "
            f"{self.capacidad} personas."        )

    
    def mostrar_informacion(self): # Sobrescribe mostrar_informacion().

        return (
            f"{super().mostrar_informacion()}\n"
            f"Capacidad: {self.capacidad} personas"
        )