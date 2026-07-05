# Archivo: simulacion.py
# Descripción: Simulación completa para validar el funcionamiento del sistema Software FJ.

from colorama import Fore, Style # Importa la librería Colorama para mostrar mensajes con colores.
from modelos.cliente import Cliente # Importa la clase Cliente.
from modelos.reserva_sala import ReservaSala # Importa la clase ReservaSala.
from modelos.alquiler_equipo import AlquilerEquipo # Importa la clase AlquilerEquipo.
from modelos.asesoria import Asesoria # Importa la clase Asesoria.
from modelos.reserva import Reserva # Importa la clase Reserva.
from util.logger import registrar_error # Importa la función que guarda los errores en el archivo errores.log.
from excepciones.excepciones import ReservaEstadoError

# _____________Función: ejecutar_simulacion()_________________
# Descripción: Ejecuta una serie de operaciones para demostrar el funcionamiento
# del sistema, incluyendo casos exitosos y casos con errores.

def ejecutar_simulacion():
    
    print(Fore.CYAN) # Muestra el título de la simulación en color cian.    
    print("=" * 50) # Imprime una línea decorativa.    
    print("SIMULACIÓN DEL SISTEMA") # Muestra el nombre de la simulación.    
    print("=" * 50) # Imprime otra línea decorativa.   
    print(Style.RESET_ALL) # Restablece el color normal de la consola.       
  
# ___________________OPERACIÓN 1____________________________
# Registra un cliente con datos válidos.
    try:
        # Crea un nuevo cliente.
        cliente1 = Cliente(
            "CLI001",
            "Cliente de Prueba 1",
            "100000001",
            "cliente1@softwarefj.com",
            "3001111111"
        )
        # Muestra un mensaje de éxito.
        print(Fore.GREEN + "✔ Operación 1: Cliente registrado correctamente.")       
        print(cliente1.mostrar_informacion()) # Muestra la información del cliente.

    except Exception as error:
        
        print(Fore.RED + f"✘ Error: {error}") # Muestra el error ocurrido.

    finally:
        
        print(Style.RESET_ALL) # Restablece el color de la consola.

# ___________________OPERACIÓN 2____________________________
# Intenta registrar un cliente con un correo inválido.
    # Debe generar una excepción controlada.   
    try:
        # Crea un cliente con un correo incorrecto.
        Cliente( 
            "CLI002",
            "Cliente de Prueba 2",
            "100000002",
            "correo_invalido",
            "3002222222"
        )

        # Este mensaje solo aparecerá si no ocurre ningún error.
        print(Fore.GREEN + "✔ Operación 2: Cliente registrado correctamente.")

    except Exception as error:
        
        print(Fore.RED + "✘ Operación 2: Error controlado.") # Muestra el mensaje del error en color rojo.        
        print(Fore.RED + f"Detalle: {error}") # Muestra la descripción del error.

    finally:
        
        print(Style.RESET_ALL) # Restablece el color de la consola.

# ___________________OPERACIÓN 3____________________________
# Registra una reserva de sala con datos válidos.
    try:
        # Crea un servicio de tipo Reserva de Sala.
        reserva_sala = ReservaSala(
            "SER001",
            "Sala de Juntas",
            80000,
            20
        )
        
        print(Fore.GREEN + "✔ Operación 3: Reserva de sala registrada correctamente.") # Muestra un mensaje de éxito.       
        print(reserva_sala.mostrar_informacion()) # Muestra la información del servicio.

    except Exception as error:
        
        print(Fore.RED + f"✘ Error: {error}") # Muestra el error ocurrido.

    finally:
       
        print(Style.RESET_ALL) # Restablece el color de la consola.

# ___________________OPERACIÓN 4____________________________
# Registra un servicio de alquiler de equipo con datos válidos.  
    try:
        # Crea un servicio de tipo Alquiler de Equipo.
        alquiler_equipo = AlquilerEquipo(
            "SER002",
            "Video Beam",
            50000,
            "Proyector"
        )
        
        print(Fore.GREEN + "✔ Operación 4: Alquiler de equipo registrado "
        "correctamente.") # Muestra un mensaje de éxito.        
        print(alquiler_equipo.mostrar_informacion()) # Muestra la información del servicio.

    except Exception as error:
        
        print(Fore.RED + f"✘ Error: {error}") # Muestra el error ocurrido.

    finally:
        
        print(Style.RESET_ALL) # Restablece el color de la consola.

# ___________________OPERACIÓN 5____________________________
# Registra un servicio de asesoría con datos válidos.
    try:
        # Crea un servicio de tipo Asesoría.
        asesoria = Asesoria(
            "SER003",
            "Asesoría Tecnológica",
            120000,
            "Ingeniería de Software"
        )
       
        print(Fore.GREEN + "✔ Operación 5: Asesoría registrada correctamente.")  # Muestra un mensaje de éxito.        
        print(asesoria.mostrar_informacion()) # Muestra la información del servicio.

    except Exception as error:
        
        print(Fore.RED + f"✘ Error: {error}") # Muestra el error ocurrido.

    finally:
        
        print(Style.RESET_ALL) # Restablece el color de la consola.

# ___________________OPERACIÓN 6____________________________
# Crea una reserva utilizando un cliente y un servicio válidos.
    try:
        # Crea un cliente de prueba.
        cliente = Cliente(
            "CLI003",
            "Cliente de Reserva",
            "100000003",
            "cliente3@softwarefj.com",
            "3003333333"
        )

        # Crea un servicio de tipo Reserva de Sala.
        servicio = ReservaSala(
            "SER004",
            "Sala de Capacitación",
            100000,
            30
        )

        # Crea la reserva.
        reserva = Reserva(
            cliente,
            servicio,
            4
        )
        
        reserva.confirmar() # Confirma la reserva.

        print(Fore.GREEN + "✔ Operación 6: Reserva creada correctamente.") # Muestra un mensaje de éxito.        
        print(reserva.mostrar_informacion()) # Muestra la información de la reserva.       
        print(f"Costo total: ${reserva.procesar():,.0f}") # Calcula el costo total.

    except Exception as error:
        
        print(Fore.RED + f"✘ Error: {error}") # Muestra el error ocurrido.

    finally:
       
        print(Style.RESET_ALL)  # Restablece el color de la consola.

# ___________________OPERACIÓN 7____________________________
# Intenta crear una reserva con una duración inválida.
    # Debe generar una excepción controlada. 
    try:
        # Crea un cliente válido.
        cliente = Cliente(
            "CLI004",
            "Cliente de Prueba 4",
            "100000004",
            "cliente4@softwarefj.com",
            "3004444444"
        )

        # Crea un servicio válido.
        servicio = ReservaSala(
            "SER005",
            "Sala Ejecutiva",
            90000,
            15
        )

        # Intenta crear una reserva con duración inválida.
        Reserva(
            cliente,
            servicio,
            0
        )

        # Este mensaje solo aparecerá si no ocurre ningún error.
        print(Fore.GREEN + "✔ Operación 7 ejecutada correctamente.")

    except Exception as error:

        # Muestra el mensaje del error.
        print(Fore.RED + "✘ Operación 7: Error controlado.")

        # Muestra el detalle del error.
        print(Fore.RED + f"Detalle: {error}")

    finally:

        # Restablece el color normal de la consola.
        print(Style.RESET_ALL)

# ___________________OPERACIÓN 8____________________________
    # Intenta registrar un servicio con un costo inválido.
    # Debe generar una excepción controlada. 
    try:

        # Intenta crear una reserva de sala con costo inválido.
        ReservaSala(
            "SER006",
            "Sala de Conferencias",
            -50000,
            25
        )

        # Este mensaje solo aparecerá si no ocurre ningún error.
        print(Fore.GREEN + "✔ Operación 8 ejecutada correctamente.")

    except Exception as error:
        
        print(Fore.RED + "✘ Operación 8: Error controlado.") # Muestra el mensaje del error.        
        print(Fore.RED + f"Detalle: {error}") # Muestra el detalle del error.

    finally:
        
        print(Style.RESET_ALL) # Restablece el color normal de la consola.

# ___________________OPERACIÓN 9____________________________
    # Genera un error y lo registra en el archivo errores.log.   
    try:
        
        raise ValueError("Error de prueba para el archivo de log.") # Genera un error de prueba.

    except Exception as error:
        
        registrar_error(error) # Registra el error en el archivo errores.log.        
        print(Fore.RED + "✘ Operación 9: Error registrado en errores.log") # Informa que el error fue registrado.

    finally:
        
        print(Style.RESET_ALL) # Restablece el color normal de la consola.

           
       # ---------------- OPERACIÓN 10 ----------------
    # Verifica que no se pueda confirmar una reserva cancelada.

    try:

        cliente_prueba = Cliente(
        "CLI999",
        "Cliente Prueba",
        "123456789",
        "prueba@softwarefj.com",
        "3000000000"
        )
        servicio_prueba = ReservaSala(
            "SER999",
        "Sala Prueba",
        100000,
        20
        )

        reserva = Reserva(
            cliente_prueba,
        servicio_prueba,
        2
        )

        reserva.cancelar()
        reserva.confirmar()

    except ReservaEstadoError as error:

        print(Fore.RED + "✘ Operación 10: Error controlado.")
        print(f"Detalle: {error}")

    finally:

        print(Style.RESET_ALL)

# ___________________OPERACIÓN 11____________________________
    # Verifica que el sistema continúa funcionando después
    # de ejecutar todas las operaciones de la simulación.
    print(Fore.GREEN)
    print("=" * 60)
    print("SIMULACIÓN FINALIZADA CORRECTAMENTE")
    print("Todas las operaciones fueron ejecutadas.")
    print("El sistema continúa funcionando después de los errores.")
    print("=" * 60)
    print(Style.RESET_ALL)

    input("\nPresione ENTER para volver al menú...")