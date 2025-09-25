# gestor_notas.py
# Sprint 1: Versión mínima
# Permite agregar estudiantes y sus notas, y listarlos

from typing import Dict, Optional

class GestorNotas:
    """Gestiona la adición y recuperación de estudiantes y sus notas."""

    def __init__(self):
        """Inicializa un gestor de notas vacío."""
        self.estudiantes: Dict[str, float] = {}

    def agregar_estudiante(self, nombre: str, nota: float) -> None:
        """
        Agrega un estudiante y su nota al gestor.
        Si el estudiante ya existe, su nota será actualizada.
        """
        self.estudiantes[nombre] = nota

    def obtener_estudiantes(self) -> Dict[str, float]:
        """Devuelve un diccionario con todos los estudiantes y sus notas."""
        return self.estudiantes


def solicitar_datos_estudiante(gestor: GestorNotas) -> None:
    """Solicita al usuario el nombre y la nota de un estudiante y lo agrega al gestor."""
    while True:
        nombre = input("Nombre del estudiante: ")
        if nombre.replace(" ", "").isalpha() and nombre.strip():
            break
        else:
            print("Error: El nombre debe contener solo letras y no estar vacío.")
    
    while True:
        try:
            nota_str = input("Nota: ")
            nota = float(nota_str)
            if 0 <= nota <= 20:
                gestor.agregar_estudiante(nombre, nota)
                print("Estudiante agregado con éxito.")
                break
            else:
                print("Error: La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Error: La nota debe ser un valor numérico.")


def mostrar_estudiantes(gestor: GestorNotas) -> None:
    """Muestra por consola la lista de estudiantes registrados."""
    estudiantes = gestor.obtener_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- Lista de Estudiantes ---")
        for nombre, nota in estudiantes.items():
            print(f"{nombre}: {nota}")


def main():
    """Función principal que ejecuta el menú de la aplicación."""
    gestor = GestorNotas()

    while True:
        print("\n--- Menú Gestor de Notas ---")
        print("1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            solicitar_datos_estudiante(gestor)
        elif opcion == "2":
            mostrar_estudiantes(gestor)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__== "__main__":
    main()