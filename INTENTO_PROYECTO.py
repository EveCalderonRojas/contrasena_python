#Librerias.
import string
import random

#Clase para generar una contraseña segura.
class GENERADOR_CONTRASENA_SEGURA:
    def __init__(self, longitud:int = 0, caracteres:int = 0):
        self.__longitud = longitud
        self.__caracteres = caracteres
    
    @property
    def longitud(self):
        return self.__longitud 
    
    @property
    def caracteres(self):
        return self.__caracteres
    
    @longitud.setter
    def longitud(self, longitud:int = 0):
        self.__longitud = longitud
        
    @caracteres.setter
    def caracteres(self, caracteres:int = 0):
        self.__caracteres = caracteres

    def GENERADOR_CONTRASENA(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''
        for i in range(self.__longitud):
            contrasena += random.choice(caracteres)
        return contrasena

    def GENERADOR_CICLO(self):
        if self.__caracteres > self.__longitud:
            print('Los caracteres especiales que indico no deben ser mayores a la longitud de su contraseña')
    nueva_contrasena = self.GENERADOR_CONTRASENA()
    print('La nueva contraseña es:', nueva_contrasena)
            
    print("¡Muchas gracias por utilizar nuestro generador de contraseñas seguras!")