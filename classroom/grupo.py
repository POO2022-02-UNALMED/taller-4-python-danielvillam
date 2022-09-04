from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        Grupo.asignarNombre("Grado 12")
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        

    def listadoAsignaturas(self, **kwargs):
        self._asignaturas=[]
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            lista=[]
        self.listadoAlumnos = [alumno]
        self.listadoAlumnos = lista + self.listadoAlumnos

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        cadena="Grupo de estudiantes: "+self._grupo
        return cadena
