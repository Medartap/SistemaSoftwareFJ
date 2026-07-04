# Sistema Software FJ

## Descripción

Sistema desarrollado en Python para la gestión de servicios tecnológicos, aplicando los principios de Programación Orientada a Objetos (POO).

El sistema permite administrar clientes, servicios y reservas, además de ejecutar una simulación para comprobar el correcto funcionamiento de las operaciones y el manejo de excepciones.

---

## Funcionalidades

- Registrar clientes.
- Registrar servicios.
- Crear reservas.
- Mostrar clientes registrados.
- Mostrar servicios registrados.
- Mostrar reservas registradas.
- Ejecutar una simulación completa del sistema.
- Registrar errores en un archivo de log.

---

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Colorama
- Git
- GitHub

---

## Estructura del proyecto

```
SistemaSoftwareFJ/
│
├── excepciones/
│   ├── __init__.py
│   └── excepciones.py
│
├── logs/
│   └── errores.log
│
├── modelos/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria.py
│
├── pruebas/
│   ├── __init__.py
│   └── simulacion.py
│
├── util/
│   ├── __init__.py
│   └── logger.py
│
├── main.py
└── README.md
```

---

## Requisitos

Tener instalado:

- Python 3.10 o superior
- Biblioteca Colorama

Instalación:

```bash
pip install colorama
```

---

## Ejecución

Desde la carpeta principal ejecutar:

```bash
python main.py
```

---

## Menú principal

El sistema permite las siguientes opciones:

1. Registrar cliente.
2. Registrar servicio.
3. Crear reserva.
4. Mostrar clientes.
5. Mostrar servicios.
6. Mostrar reservas.
7. Ejecutar simulación.
0. Salir.

---

## Programación Orientada a Objetos aplicada

Durante el desarrollo se implementaron los siguientes conceptos:

- Clases.
- Objetos.
- Herencia.
- Polimorfismo.
- Encapsulamiento.
- Clases abstractas.
- Manejo de excepciones.
- Registro de errores mediante logging.

---

## Registro de errores

Los errores generados durante la ejecución del sistema se almacenan automáticamente en:

```
logs/errores.log
```

---

## Autores

- Medardo Tabares Prieto
  - C.C. 1122647056

- Oscar Julian Roman
  - C.C 16378190

- Integrante 3
  - Pendiente

---

## Licencia

Proyecto desarrollado con fines académicos.
