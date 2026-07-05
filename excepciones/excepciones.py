# Archivo: excepciones.py
# Contiene las excepciones personalizadas del sistema Software FJ.

# ________Excepción para errores relacionados con clientes______
class ClienteError(Exception):
    pass

class ServicioError(Exception): # Excepción para errores relacionados con servicios.
    pass

class ReservaError(Exception): # Excepción para errores relacionados con reservas.
    pass

# ============================================================
# Inicio aporte Oscar Julian Roman
# Fecha: 04/07/2026
# Descripción:
# Excepción personalizada para controlar operaciones inválidas
# relacionadas con el estado de las reservas.
# ============================================================

class ReservaEstadoError(ReservaError):
    """Se genera cuando una reserva cambia a un estado no permitido."""
    pass

# ============================================================
# Fin aporte Oscar Julian Roman
# ============================================================