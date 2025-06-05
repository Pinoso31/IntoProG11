class Estudiante():
    def __init__(self, nombre, apellidos, carrera, cif):
        self.first_name = nombre
        self.last_name = apellidos
        self.major = carrera
        self.cif = cif

    def __str__(self):
        return f"{self.firs_name} {self.last_name} {self.major}"
