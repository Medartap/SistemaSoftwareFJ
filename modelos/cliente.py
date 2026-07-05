# Archivo: cliente.py
# Descripción: Implementación de la clase Cliente del sistema Software FJ.
# Importa la clase Entidad.
from modelos.entidad import Entidad

# ________________Clase Cliente que hereda de Entidad_______________
class Cliente(Entidad): # Clase encargada de almacenar y validar la información de los clientes.

    # Constructor de la clase.
    def __init__(self, codigo, nombre, documento, correo, telefono):

        
        super().__init__(codigo) # Llama al constructor de la clase padre.

        # Asigna los datos utilizando los setters para validarlos.
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono       
    
    @property # Propiedad nombre
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):

        if not nombre.strip():
           raise ValueError("El nombre no puede estar vacío.")

        self._nombre = nombre      
   
    @property # Propiedad documento
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, documento):

        if not documento.strip():
            raise ValueError("El documento no puede estar vacío.")

        self._documento = documento     
    
    @property # Propiedad correo
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):

        if "@" not in correo:
            raise ValueError("Correo electrónico inválido.")

        self._correo = correo       
  
    @property # Propiedad teléfono
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):

        if not telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")

        self._telefono = telefono

    # Implementación del método abstracto.
    def mostrar_informacion(self): # muestra la informacion

        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )