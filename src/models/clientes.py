class Cliente():
    def __init__(self, cedula, nombres, apellidos, celular, foto, activo=True):
        self.__cedula = cedula
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__celular = celular
        self.__foto = foto
        self.__activo = activo
    
   
    def get_cedula(self): 
        return self.__cedula
    
    def get_nombre_completo(self):
        return f"{self.__nombres} {self.__apellidos}"
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_celular(self):
        return self.__celular
    
    def get_foto(self):
        return self.__foto
    
    def get_activo(self):
        return self.__activo
    
   
    def set_cedula(self, nueva_cedula): 
        self.__cedula = nueva_cedula
    
    def set_nombres(self, nuevos_nombres):
        self.__nombres = nuevos_nombres
    
    def set_apellidos(self, nuevos_apellidos): 
        self.__apellidos = nuevos_apellidos

    def set_celular(self, nuevo_celular): 
        self.__celular = nuevo_celular
    
    def set_foto(self, nueva_foto):
        self.__foto = nueva_foto

    def set_activo(self, nuevo_activo): 
        self.__activo = nuevo_activo

    # METODOS
    def imprimir(self):
        return f"Cedula: {self.__cedula} | Nombre: {self.get_nombre_completo()} | Celular: {self.__celular} | Activo: {self.__activo}"
    
    def cambiar_estado(self):
        if self.__activo:
            self.__activo = False
        else:
            self.__activo = True
    
    

