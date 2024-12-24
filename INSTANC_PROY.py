from INTENTO_PROYECTO import GENERADOR_CONTRASENA_SEGURA as GCS

longitud = int(input('Indique la longitud de la contraseña deseada: '))
caracteres = int(input('Indique cuantos caracteres especiales desea: '))
contraseña = GCS(longitud,caracteres)
contraseña.GENERADOR_CICLO()    


