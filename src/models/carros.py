class Carro:
    def __init__(self, placa, marca, modelo, en_mantenimiento=False):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__en_mantenimiento = en_mantenimiento
    

    def get_placa(self):
        return self.__placa
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_en_mantenimiento(self):
        return self.__en_mantenimiento
    
    # SETTERS
    def set_placa(self, nueva_placa):
        self.__placa = nueva_placa
    
    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    def set_en_mantenimiento(self, nuevo_mantenimiento):
        self.__en_mantenimiento = nuevo_mantenimiento


    def imprimir_carro(self):
        return f"Placa: {self.__placa} | Marca: {self.__marca} | Modelo: {self.__modelo} | Mantenimiento: {self.__en_mantenimiento}"
    
    def cambiar_mantenimiento(self):
        if self.__en_mantenimiento:
            self.__en_mantenimiento = False
        else:
            self.__en_mantenimiento = True
