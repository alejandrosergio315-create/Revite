from src.database.main_sqlite3 import obtener_reservas_usuario
from src.models.reservas import Reserva
from src.models.clientes import Cliente
from src.models.carros import Carro


def cargar_reservas(func):

    def wrapper(*args, **kwargs):

        usuario = kwargs.get("usuario")

        if not usuario:
            return func(*args, **kwargs)

        datos = obtener_reservas_usuario(usuario["id"])

        reservas = []

        for r in datos:
            reserva = Reserva(
                usuario,   # cliente
                r[1],      # destino
                r[2],      # horario
                r[3],      # fecha
                r[4],      # carro
                r[0]       # ID de la reserva
            )

            reservas.append(reserva)

        kwargs["reservas"] = reservas

        return func(*args, **kwargs)

    return wrapper