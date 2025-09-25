class GestorNotas:
    """Gestor de estudiantes con sus notas en memoria."""

    def __init__(self):
        self.estudiantes = {}
        self.id_counter = 1

    def agregar_estudiante(self, nombre: str, nota: float):
        self.estudiantes[self.id_counter] = {"nombre": nombre, "nota": nota}
        self.id_counter += 1

    def obtener_estudiantes(self):
        return self.estudiantes

    def editar_estudiante(self, estudiante_id: int, nueva_nota: float):
        if estudiante_id in self.estudiantes:
            self.estudiantes[estudiante_id]["nota"] = nueva_nota
            return True
        return False

    def eliminar_estudiante(self, estudiante_id: int):
        if estudiante_id in self.estudiantes:
            del self.estudiantes[estudiante_id]
            return True
        return False

    def buscar_estudiante(self, nombre: str):
        for est in self.estudiantes.values():
            if est["nombre"].lower() == nombre.lower():
                return est
        return None