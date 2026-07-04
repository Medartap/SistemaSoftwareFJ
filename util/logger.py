# Archivo: logger.py
# Descripción: Registra los errores del sistema en un archivo.
# Importa la librería logging.
import logging

# _______Configura el archivo donde se guardarán los errores_______
logging.basicConfig(
    
    filename="logs/errores.log", # Nombre del archivo de registro.   
    level=logging.ERROR, # Nivel de registro.    
    format="%(asctime)s - %(levelname)s - %(message)s" # Formato del mensaje.
)

def registrar_error(error): # Función para registrar errores.
    
    logging.error(error) # Guarda el error en el archivo errores.log.