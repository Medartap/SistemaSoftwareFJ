# Archivo: excepciones.py
# Contiene las excepciones personalizadas del sistema Software FJ.

# ________Excepción para errores relacionados con clientes______
class ClienteError(Exception):
    pass

class ServicioError(Exception): # Excepción para errores relacionados con servicios.
    pass

class ReservaError(Exception): # Excepción para errores relacionados con reservas.
    pass