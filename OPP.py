

class Profesor:

    #COnstructor de la clase profesor
    def __init__(self, nombre, email):
        self.__nombre__ = nombre
        self.__email__ = email

    #Metodo de la clase profesor
    def get_nombre(self):
        return self.nombre



class Alumno:
    
    #Constructor de la clase Alumno
    def __init__(self, nombre):
        self.__nombre__ = nombre
        self.__inasistencias__ = 0
        self.__dieta__ = ''
        self.__profesor__ = None

    def mentoria(self, maestro):
        self.__profesor__ = maestro    
    
    #Metodo para sumar una falta
    def falta(self):
        self.__inasistencias__ += 1

    #Metodo para quedarse libre, para eso inasistencias >= 5
    def libre(self):
        if self.__inasistencias__ > 5:
            return 'Estas Libre'
        else:
            return 'Todo okey wacho'

    #Metodo para asignar la dieta del alumno
    def dieta_especial(self, dieta):
        self.__dieta__ = dieta

    def vegano(self):
        self.__dieta__ = 'vegano'

#Asignar los atributos 
profe_elio = Profesor('Elio', 'elio@gmail.com')
profe_gabi = Profesor('Gabriel', 'gabriel@um.edu.ar')


#Asignar los atributos 
alumno_martin = Alumno('Martin')
alumno_josefina = Alumno('Josefina')

#Sumar faltas a martin
alumno_martin.falta()
alumno_martin.falta()
alumno_martin.falta()
alumno_martin.falta()
alumno_martin.falta()
alumno_martin.falta()

los_alumnos = [alumno_martin, alumno_josefina]

#Metodo dieta
alumno_josefina.dieta_especial('vegetariana')
alumno_martin.vegano()

#Asignar profesor
alumno_martin.mentoria(profe_elio)

print(f'El email de {alumno_martin.__nombre__} es {profe_elio.__email__}')
print(f'Las inasistencias de {alumno_martin.__nombre__} son {alumno_martin.__inasistencias__}, por lo tanto {alumno_martin.libre()}')
print(f'La dieta de {alumno_josefina.__nombre__} es {alumno_josefina.__dieta__}')
print(f'El alumno {alumno_martin.__nombre__} es {alumno_martin.__dieta__}, su profesor es {alumno_martin.__profesor__.__nombre__}')