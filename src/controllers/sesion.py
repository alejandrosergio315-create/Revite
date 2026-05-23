class Sesion:

    _instancia = None

    def __new__(cls):

        if cls._instancia is None:

            cls._instancia = super().__new__(cls)

            cls._instancia.usuario = {}

        return cls._instancia

    def iniciar_sesion(self, datos_usuario):

        self.usuario = datos_usuario

    def obtener_usuario(self):

        return self.usuario