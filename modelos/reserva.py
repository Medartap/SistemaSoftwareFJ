# Archivo: reserva.py
# Descripción: Implementación de la clase Reserva para gestionar las reservas del sistema.
from modelos.cliente import Cliente
# Importa la clase Servicio.
from modelos.servicio import Servicio

# __________________Clase Reserva.___________________
class Reserva: # Clase encargada de crear, confirmar y procesar las reservas.
    # Constructor.
    def __init__(self, cliente, servicio, duracion):
       
        if not isinstance(cliente, Cliente):  # Verifica que el cliente sea un objeto Cliente.
            raise ValueError("Cliente inválido.")
        
        if not isinstance(servicio, Servicio): # Verifica que el servicio sea un objeto Servicio.
            raise ValueError("Servicio inválido.")
        
        if duracion <= 0: # Verifica que la duración sea mayor que cero.
            raise ValueError("La duración debe ser mayor que cero.")

        # Guarda los datos de la reserva.
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        
        self.estado = "Pendiente" # Estado inicial de la reserva.
    
    def confirmar(self): # Confirma la reserva.

        self.estado = "Confirmada"
    
    def cancelar(self): # Cancela la reserva.

        self.estado = "Cancelada"
   
    def procesar(self):  # Procesa la reserva.

        return self.servicio.calcular_costo(self.duracion)
    
    def mostrar_informacion(self): # Muestra la información de la reserva.

        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )
    