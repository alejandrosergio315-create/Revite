class Reserva:
    def __init__(self, cliente, destino, hora_salida, fecha_salida, carro, confirmado=False, reserva_id=None):
        self.__cliente = cliente
        self.__destino = destino
        self.__hora_salida = hora_salida
        self.__fecha_salida = fecha_salida
        self.__carro = carro
        self.__confirmado = confirmado
        self.__reserva_id = reserva_id
    

    # GETTERS
    def get_cliente(self):
        return self.__cliente
    
    def get_destino(self):
        return self.__destino
    
    def get_hora_salida(self):
        return self.__hora_salida
    
    def get_fecha_salida(self):
        return self.__fecha_salida
    
    def get_carro(self):
        return self.__carro
    
    def get_confirmado(self):
        return self.__confirmado
    
    def get_id(self):
        return self.__reserva_id
    
    
    # SETTERS
    def set_cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente
    
    def set_destino(self, nuevo_destino):
        self.__destino = nuevo_destino
    
    def set_hora_salida(self, nueva_hora_salida):
        self.__hora_salida = nueva_hora_salida
    
    def set_fecha_salida(self, nueva_fecha_salida):
        self.__fecha_salida = nueva_fecha_salida
    
    def set_carro(self, nuevo_carro):
        self.__carro = nuevo_carro
    
    def set_confirmado(self, nuevo_confirmado):
        self.__confirmado = nuevo_confirmado
    
    # METODOS
    def confirmar_reserva(self):
        self.__confirmado = True
    
    def imprimir(self):
        if self.__confirmado:
            estado = "Confirmado"
        else:
            estado = "Pendiente"

        return f"Cliente: {self.__cliente.get_nombre_completo()} | Destino: {self.__destino} | Hora: {self.__hora_salida} | Fecha: {self.__fecha_salida} | Estado: {estado}"
    
    def imprimir_confirmados(self):
        if self.__confirmado:
            return self.imprimir_cliente()
        else:
            return "Reserva no confirmada"
    
    

    
    
    


        
        
        