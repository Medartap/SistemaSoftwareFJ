# Archivo: main.py
# Descripción: Programa principal del sistema Software FJ.

import os # Importa librerías.

from colorama import Fore, Style, init # Importa Colorama para los colores.

init(autoreset=True) # Inicializa Colorama.

# ____________Importa las clases del sistema______________
from modelos.cliente import Cliente
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria
from modelos.reserva import Reserva
from pruebas.simulacion import ejecutar_simulacion  # Importa la función que ejecuta la simulación del sistema.
from util.logger import registrar_error # Importa el registro de errores.

# ___________Listas del sistema______________
clientes = []
servicios = []
reservas = []

# ________Funciones auxiliares_______________

def limpiar(): # Limpia la consola.

    os.system("cls" if os.name == "nt" else "clear")

def encabezado(): # Muestra el encabezado.

    limpiar()

    print(Fore.CYAN + "=" * 50)      # Color azul.
    print(Fore.CYAN + "        SISTEMA SOFTWARE FJ")
    print(Fore.CYAN + "=" * 50)
    print(Style.RESET_ALL)

def pausar(): # Pausa el programa.

    input("\nPresione ENTER para continuar...")


# _____________Muestra el menú.________________
def menu():

    encabezado()

    print(Fore.YELLOW + "1. Registrar cliente")   # en color Amarillo.
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Mostrar clientes")
    print("5. Mostrar servicios")
    print("6. Mostrar reservas")
    print("7. Ejecutar simulación")
    print("0. Salir")
    print(Style.RESET_ALL)

    return input("Seleccione una opción: ")

# ______________Registra un nuevo cliente_______________
def registrar_cliente():

    encabezado()

    try:

        # Solicita los datos del cliente.
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        
        cliente = Cliente(codigo, nombre, documento, correo, telefono) # Crea el objeto cliente.        
        clientes.append(cliente) # Agrega el cliente a la lista.

    except Exception as error:
        
        registrar_error(error) # Registra el error en el archivo log.        
        print(Fore.RED + f"\nError: {error}") # Muestra el mensaje de error.

    else:
        
        print(Fore.GREEN + "\nCliente registrado correctamente.") # Mensaje cuando el registro es exitoso.

    finally:
        
        pausar() # Espera que el usuario presione ENTER.
     
# _______________Registra un nuevo servicio________________
def registrar_servicio():

    encabezado()

    try:

        # Muestra los tipos de servicio.
        print(Fore.YELLOW + "1. Reserva de sala")
        print("2. Alquiler de equipo")
        print("3. Asesoría")
        print(Style.RESET_ALL)

        opcion = input("\nSeleccione el servicio: ")

        # Solicita los datos del servicio.
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        costo = float(input("Costo base: "))

        # Crea una reserva de sala.
        if opcion == "1":

            capacidad = int(input("Capacidad de la sala: "))

            servicio = ReservaSala(
                codigo,
                nombre,
                costo,
                capacidad
            )

        # Crea un alquiler de equipo.
        elif opcion == "2":

            tipo = input("Tipo de equipo: ")

            servicio = AlquilerEquipo(
                codigo,
                nombre,
                costo,
                tipo
            )

        # Crea una asesoría.
        elif opcion == "3":

            especialidad = input("Especialidad: ")

            servicio = Asesoria(
                codigo,
                nombre,
                costo,
                especialidad
            )

        else:

            raise ValueError("Opción de servicio inválida.")
        
        servicios.append(servicio) # Agrega el servicio a la lista.

    except Exception as error:
        
        registrar_error(error) # Registra el error en el archivo log.        
        print(Fore.RED + f"\nError: {error}") # Muestra el mensaje de error.

    else:
        # Mensaje cuando el registro es exitoso.
        print(Fore.GREEN + "\nServicio registrado correctamente.")

    finally:        
        pausar() # Espera que el usuario presione ENTER.

# ________________Crea una nueva reserva___________________
def crear_reserva():

    encabezado()

    try:
        
        if not clientes: # Verifica que existan clientes.
 
            raise ValueError("No hay clientes registrados.")
        
        if not servicios: # Verifica que existan servicios.

            raise ValueError("No hay servicios registrados.")

        # Muestra los clientes.
        print(Fore.CYAN + "\nCLIENTES")

        for i, cliente in enumerate(clientes):

            print(f"{i + 1}. {cliente.nombre}")

        indice_cliente = int(input("\nSeleccione un cliente: ")) - 1

        # Muestra los servicios.
        print(Fore.CYAN + "\nSERVICIOS")

        for i, servicio in enumerate(servicios):

            print(f"{i + 1}. {servicio.nombre}")

        indice_servicio = int(input("\nSeleccione un servicio: ")) - 1        
        duracion = int(input("Duración (horas): ")) # Solicita la duración.

        # Crea la reserva.
        reserva = Reserva(
            clientes[indice_cliente],
            servicios[indice_servicio],
            duracion
        )
        
        reserva.confirmar() # Confirma la reserva.        
        reservas.append(reserva) # Agrega la reserva.

    except Exception as error:

        registrar_error(error)

        print(Fore.RED + f"\nError: {error}")

    else:

        print(Fore.GREEN + "\nReserva creada correctamente.")

    finally:

        pausar()

# _________________Muestra los clientes registrados_________________
def mostrar_clientes():

    encabezado()

    if not clientes:

        print(Fore.RED + "No hay clientes registrados.")

    else:

        print(Fore.CYAN + "CLIENTES REGISTRADOS\n")

        for cliente in clientes:

            print(cliente.mostrar_informacion())

    pausar()

# _________________Muestra los servicios registrados_______________
def mostrar_servicios():

    encabezado()

    if not servicios:

        print(Fore.RED + "No hay servicios registrados.")

    else:

        print(Fore.CYAN + "SERVICIOS REGISTRADOS\n")

        for servicio in servicios:

            print(servicio.mostrar_informacion())

    pausar()

#_________________Muestra las reservas registradas______________
def mostrar_reservas():

    encabezado()

    if not reservas:

        print(Fore.RED + "No hay reservas registradas.")

    else:

        print(Fore.CYAN + "RESERVAS REGISTRADAS\n")

        for reserva in reservas:

            print(reserva.mostrar_informacion())

    pausar()

# ________________Programa principal__________________
# Controla el menú del sistema y ejecuta la opción seleccionada por el usuario.
if __name__ == "__main__":

    while True: # Muestra el menú y captura la opción elegida.

        opcion = menu()  

        if opcion == "1": # Opción 1: Registrar un cliente.

            registrar_cliente() 

        elif opcion == "2": # Opción 2: Registrar un servicio.

            registrar_servicio() 

        elif opcion == "3": # Opción 3: Crear una reserva.

            crear_reserva() 

        elif opcion == "4": # Opción 4: Mostrar los clientes registrados.

            mostrar_clientes() 

        elif opcion == "5": # Opción 5: Mostrar los servicios registrados.

            mostrar_servicios() 

        elif opcion == "6": # Opción 6: Mostrar las reservas registradas.

            mostrar_reservas() 

        elif opcion == "7": # Opción 7: Ejecutar la simulación solicitada en la guía.
           
            ejecutar_simulacion() 
            input("\nLa simulación terminó. Presione ENTER...")

        elif opcion == "0":  # Opción 0: Finaliza el programa.

            print(Fore.GREEN + "\nGracias por utilizar Sistema Software FJ.")
            break

        else:  # Se ejecuta cuando la opción no existe.

            print(Fore.RED + "\nOpción inválida.")

            pausar()