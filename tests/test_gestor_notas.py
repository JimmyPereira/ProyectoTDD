from src.gestor_notas_tdd import GestorNotas

def test_agregar_estudiante():
    gestor = GestorNotas()
    gestor.agregar_estudiante("Juan", 15.0)
    estudiantes = gestor.obtener_estudiantes()
    assert 1 in estudiantes
    assert estudiantes[1]["nombre"] == "Juan"
    assert estudiantes[1]["nota"] == 15.0

def test_editar_estudiante():
    gestor = GestorNotas()
    gestor.agregar_estudiante("Ana", 12.0)
    actualizado = gestor.editar_estudiante(1, 18.0)
    assert actualizado is True
    assert gestor.obtener_estudiantes()[1]["nota"] == 18.0

def test_eliminar_estudiante():
    gestor = GestorNotas()
    gestor.agregar_estudiante("Pedro", 10.0)
    eliminado = gestor.eliminar_estudiante(1)
    assert eliminado is True
    assert gestor.obtener_estudiantes() == {}

def test_buscar_estudiante():
    gestor = GestorNotas()
    gestor.agregar_estudiante("Luis", 17.0)
    resultado = gestor.buscar_estudiante("Luis")
    assert resultado["nombre"] == "Luis"
    assert resultado["nota"] == 17.0