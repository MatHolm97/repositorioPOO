import random

class Estudiante:
    def __init__(self, nombre, apellido_paterno, apellido_materno, año_nacimiento, carrera ):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.año_nacimiento = año_nacimiento
        self.carrera = carrera
        

    def generar_matricula(self):
       
        año_nacimiento = str(self.año_nacimiento)[-2:]
        
        primera_letra_nombre = self.nombre[0]
        tres_letras_apellido_paterno = self.apellido_paterno[:3]
        tres_letras_apellido_materno = self.apellido_materno[:3]
        tres_digitos_aleatorios = str(random.randint(100, 999))
        tres_primeras_letras_carrera = self.carrera[:3].upper()

        #matricula = año_actual + año_nacimiento + primera_letra_nombre + tres_letras_apellido_paterno + tres_letras_apellido_materno + tres_digitos_aleatorios + tres_primeras_letras_carrera 

        matricula = tres_primeras_letras_carrera  + año_nacimiento + primera_letra_nombre + tres_letras_apellido_paterno + tres_letras_apellido_materno + tres_digitos_aleatorios
        
        return matricula