#Crear la clase estudiantes con sus atributos y metodos.
class estudiantes:
    def __init__(self, nombre, apellido, calificacion):
        """
        Constructor de la clase estudiantes"""

        """self, nombre, apellido y calificacion son los atributos de la clase estudiantes"""	
        self.nombre = nombre
        self.apellido = apellido
        self.set_calificacion(calificacion)
    #Metodos de la clase.
    def set_calificacion(self, calificacion):
        """"
        Establece la calificacion del estudiante"""
        if 0<=calificacion<=5:               #Rango de la calificación que actua como control.
            self.calificacion = calificacion
        else:
            print("Valor Incorrecto")
    def get_calificacion(self):
        """"
        función que devuelve la calificacion del estudiante"""
        return self.calificacion
    
    def informacion(self):
        """
        Devuelve la informacion del estudiante"""
        return f"El estudiante {self.nombre} {self.apellido} tiene una calificación de {self.get_calificacion()}"
estudiante = estudiantes("Johan", "Mora", 4.2)
print(estudiante.informacion())
