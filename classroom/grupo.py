from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        Grupo.asignarNombre("Grado 12")
        self._grupo = grupo
        if(estudiantes != None):
            self.listadoAlumnos=[]
            self.listadoAlumnos.append(estudiantes)
        else:
            self.listadoAlumnos = []
        if(asignaturas != None):
            self._asignaturas=[]
            self._asignaturas.append(asignaturas)
        else:
            self._asignaturas = []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if(lista is None):
            self.listadoAlumnos.append(alumno)
        else:
            for x in lista:
                self.listadoAlumnos.append(x)
            self.listadoAlumnos.append(alumno)

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
