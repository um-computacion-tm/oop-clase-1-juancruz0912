class Persona:
    
    def __init__(self, nombre: str = 'Roberto', apellido: str = 'Garcia', du: int = 0):
       self.__nombre__ = nombre
       self.__apellido__ = apellido
       self.__du__ = du

    def __str__ (self):
        return f'nombre: {self.__nombre__}\napellido: {self.__apellido__} \ndocumento: {self.__du__}'    

    # def mostrar_datos(self):
        # return f'nombre: {self.__nombre__}\napellido: {self.__apellido__} \ndocumento: {self.__du__}'

    # def mostrar_datos(self):
    #     print(f'nombre: {self.__nombre__}\napellido: {self.__apellido__} \ndocumento: {self.__du__}')
