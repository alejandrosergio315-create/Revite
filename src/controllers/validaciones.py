from datetime import datetime



def validar_campos(
    destino,
    horario,
    fecha,
    seleccion_carro
    ):

    if (
        destino is None
        or horario.value is None
        or fecha.value == ""
        or seleccion_carro.value is None
    ):
        return False

    return True

def validar_fecha(fecha):

    fecha_reserva = datetime.strptime(
        fecha.value,
        "%d-%m-%Y"
    )

    hoy = datetime.now()

    if fecha_reserva.date() < hoy.date():
        return False

    return True