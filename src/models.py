from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    nota = Column(Float, nullable=False)

# Configuración de la BD
engine = create_engine("sqlite:///notas.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def agregar_estudiante(nombre, nota):
    session = Session()
    nuevo = Estudiante(nombre=nombre, nota=nota)
    session.add(nuevo)
    session.commit()
    session.close()

def obtener_estudiantes():
    session = Session()
    estudiantes = session.query(Estudiante).all()
    session.close()
    return estudiantes