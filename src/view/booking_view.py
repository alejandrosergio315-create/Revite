import flet as ft
from models.clientes import Cliente
from models.carros import Carro
from models.reservas import Reserva


def booking_view(page):

    reservas = []

    
    cedula = ft.TextField(hint_text="Cedula", color="black")
    nombre = ft.TextField(hint_text="Nombres", color="black")
    apellido = ft.TextField(hint_text="Apellidos", color="black")
    celular = ft.TextField(hint_text="Celular", color="black")
    foto = ft.TextField(hint_text="Foto (Ruta)", color="black")
    activo = ft.Switch(label="Activo", value=True)


    carros_por_ciudad = {
        "Bogota": [
            Carro("ABC123", "Toyota", "2020"),
            Carro("DEF456", "Ford", "2022"),
            Carro("GHI789", "Mazda", "2021")
        ],
        "Ibague": [
            Carro("LXS029", "Chevrolet", "2023"),
            Carro("JKL111", "Kia", "2020"),
            Carro("MNO222", "Nissan", "2019")
        ],
        "Espinal": [
            Carro("PQR333", "Hyundai", "2022"),
            Carro("STU444", "Renault", "2021"),
            Carro("VWX555", "Suzuki", "2020")
        ]
    }

    seleccion_carro = ft.Dropdown(hint_text="Carro", options=[])

    

    def actualizar_carros(e):
        ciudad = destino.value

        if ciudad is None:
            return

        seleccion_carro.options.clear()

        for carro in carros_por_ciudad[ciudad]:
            seleccion_carro.options.append(
                ft.dropdown.Option(carro.get_placa())
            )

        seleccion_carro.value = None
        seleccion_carro.update()

    
    destino = ft.Dropdown(
        hint_text="Destino",
        options=[
            ft.dropdown.Option("Bogota"),
            ft.dropdown.Option("Ibague"),
            ft.dropdown.Option("Espinal")
        ]
    )

    boton_cargar = ft.ElevatedButton(
        "Cargar carros",
        on_click=actualizar_carros
    )

    horario = ft.Dropdown(
        hint_text="Hora de salida",
        options=[
            ft.dropdown.Option("5:00"),
            ft.dropdown.Option("5:30"),
            ft.dropdown.Option("6:00"),
            ft.dropdown.Option("7:00")
        ]
    )

    fecha = ft.TextField(hint_text="Fecha (DD-MM-AAAA)", color="black")

    lista = ft.Column()

    

    def confirmar(reserva, texto, boton):
        reserva.confirmar_reserva()
        texto.value = reserva.imprimir()

        # limpiar campos
        cedula.value = ""
        nombre.value = ""
        apellido.value = ""
        celular.value = ""
        foto.value = ""
        destino.value = None
        horario.value = None
        fecha.value = ""
        seleccion_carro.value = None

        boton.visible = False
        page.update()

    

    def reservar(e):

        lista.controls.clear()

        if (
            cedula.value == "" or
            nombre.value == "" or
            destino.value is None or
            horario.value is None or
            fecha.value == "" or
            seleccion_carro.value is None
        ):
            lista.controls.append(ft.Text("Complete todos los campos"))
            page.update()
            return

        cliente = Cliente(
            cedula.value,
            nombre.value,
            apellido.value,
            celular.value,
            foto.value,
            activo.value
        )

        if not cliente.get_activo():
            lista.controls.append(ft.Text("Cliente inactivo"))
            page.update()
            return

        carro_obtenido = None

        for carro in carros_por_ciudad[destino.value]:
            if carro.get_placa() == seleccion_carro.value:
                carro_obtenido = carro

        
        if carro_obtenido is None:
            lista.controls.append(ft.Text("Seleccione un carro válido"))
            page.update()
            return

        if carro_obtenido.get_en_mantenimiento():
            lista.controls.append(ft.Text("Carro en mantenimiento"))
            page.update()
            return

        contador = 0

        for r in reservas:
            if (
                r.get_carro().get_placa() == carro_obtenido.get_placa() and
                r.get_hora_salida() == horario.value and
                r.get_destino() == destino.value
            ):
                contador += 1

        if contador >= 4:
            lista.controls.append(ft.Text("Carro lleno (Max 4 pasajeros)"))
        else:
            nueva = Reserva(
                cliente,
                destino.value,
                horario.value,
                fecha.value,
                carro_obtenido
            )

            reservas.append(nueva)
            contador += 1

            lista.controls.append(
                ft.Text(f"Pasajeros actuales: {contador}/4")
            )

            texto_reserva = ft.Text(nueva.imprimir())

            boton_confirmar = ft.ElevatedButton("Confirmar")

            boton_confirmar.on_click = lambda e, r=nueva, t=texto_reserva, b=boton_confirmar: confirmar(r, t, b)

            lista.controls.append(
                ft.Row([texto_reserva, boton_confirmar])
            )

        page.update()

    

    return ft.Container(
        padding=30,
        content=ft.Column(
            [
                ft.Row(
                    [ft.Text("Sistema ReViTe", size=25, weight="bold", color="black")],
                    alignment="center"
                ),

                ft.Text("Datos del cliente", color="black"),
                cedula,
                nombre,
                apellido,
                celular,
                foto,
                activo,

                ft.Divider(),

                ft.Text("Datos del viaje", color="black"),
                destino,
                boton_cargar,
                horario,
                fecha,
                seleccion_carro,

                ft.ElevatedButton(
                    "Reservar",
                    on_click=reservar,
                    bgcolor="blue",
                    color="white"
                ),

                ft.Divider(),

                ft.Text("Reservas realizadas", color="black"),
                lista
            ],
            spacing=15,
            scroll="auto"
        )
    )



