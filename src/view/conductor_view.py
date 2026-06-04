import flet as ft

from database.main_sqlite3 import insertar_carro, obtener_reservas, confirmar_reserva, insertar_conductor, obtener_reservas_ciudad

def conductor_view(page, conductor):

    # -------------------------
    # CAMPOS AGREGAR CARRO
    # -------------------------

    placa = ft.TextField(
        label="Placa"
    )

    marca = ft.TextField(
        label="Marca"
    )

    modelo = ft.TextField(
        label="Modelo"
    )

    ciudad = ft.Dropdown(
        label="Ciudad",
        width=300,
        options=[
            ft.dropdown.Option("Bogotá"),
            ft.dropdown.Option("Ibagué"),
            ft.dropdown.Option("Espinal")
        ]
    )

    # -------------------------
    # PERFIL CONDUCTOR
    # -------------------------

    nombre_conductor = ft.TextField(
        label="Nombre"
    )

    cedula_conductor = ft.TextField(
        label="Cédula",
        read_only=True
    )

    celular_conductor = ft.TextField(
        label="Celular"
    )

    nombre_conductor.value = conductor[1]
    cedula_conductor.value = conductor[2]
    celular_conductor.value = conductor[3]

    # -------------------------
    # LISTAS
    # -------------------------

    lista_reservaciones = ft.Column()
    
    ciudad_conductor = {
        "valor": conductor[5]
    }

    # -------------------------
    # VISTAS
    # -------------------------

    vista_carro = ft.Column(
        visible=True,
        horizontal_alignment="center"
    )

    vista_reservas = ft.Column(
        visible=False
    )

    vista_perfil = ft.Column(
        visible=False
    )

    

    # -------------------------
    # FUNCIONES
    # -------------------------

    def cambiar_vista(nombre):

        vista_carro.visible = False
        vista_reservas.visible = False
        vista_perfil.visible = False

        if nombre == "carro":
            vista_carro.visible = True

        elif nombre == "reservas":
            vista_reservas.visible = True
            actualizar_reservaciones()

        elif nombre == "perfil":
            vista_perfil.visible = True

        page.update()


    def actualizar_reservaciones():

        if ciudad.value is None:

            lista_reservaciones.controls.clear()

            lista_reservaciones.controls.append(
                ft.Text("Primero selecciona una ciudad")
            )

            page.update()
            return
        
        
        lista_reservaciones.controls.clear()


        reservas = obtener_reservas_ciudad(
            ciudad.value
        )

        if not reservas:

            lista_reservaciones.controls.append(
                ft.Text(
                    "No hay reservaciones registradas."
                )
            )

            page.update()
            return

        for reserva in reservas:

            lista_reservaciones.controls.append(

                ft.Container(

                    content=ft.Column(

                        [

                            ft.Text(
                                f"Cédula: {reserva[1]}"
                            ),

                            ft.Text(
                                f"Destino: {reserva[2]}"
                            ),

                            ft.Text(
                                f"Hora: {reserva[3]}"
                            ),

                            ft.Text(
                                f"Fecha: {reserva[4]}"
                            ),

                            ft.Text(
                                f"Carro: {reserva[5]}"
                            ),

                            ft.Text(
                                f"Estado: {reserva[6]}"
                            ),

                            ft.ElevatedButton(
                                "Confirmar",
                                on_click=lambda e, idr=reserva[0]:
                                confirmar(idr)
                            )

                        ]
                    ),

                    bgcolor="#F5F5F5",
                    border_radius=15,
                    padding=15

                )
            )

        page.update()


    def guardar_carro(e):

        if (
            placa.value == "" or
            marca.value == "" or
            modelo.value == "" or
            ciudad.value is None
        ):
            return

        insertar_carro(
            placa.value,
            marca.value,
            modelo.value,
            ciudad.value
        )

        ciudad_conductor["valor"] = ciudad.value

        placa.value = ""
        marca.value = ""
        modelo.value = ""
        

        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                "Vehículo guardado correctamente"
            )
        )

        page.snack_bar.open = True

        page.update()


    def guardar_perfil(e):

        insertar_conductor(
            nombre_conductor.value,
            cedula_conductor.value,
            celular_conductor.value,
            placa.value
        )

        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                "Perfil guardado"
            )
        )

        page.snack_bar.open = True

        page.update()
    
    def confirmar(id_reserva):

        confirmar_reserva(id_reserva)

        actualizar_reservaciones()

    # -------------------------
    # BARRA DE OPCIONES
    # -------------------------

    barra_tabs = ft.Row(
        [
            ft.ElevatedButton(
                "Agregar carro",
                on_click=lambda e:
                cambiar_vista("carro")
            ),

            ft.ElevatedButton(
                "Reservaciones",
                on_click=lambda e:
                cambiar_vista("reservas")
            ),

            ft.ElevatedButton(
                "Mi perfil",
                on_click=lambda e:
                cambiar_vista("perfil")
            )
        ],
        alignment="center"
    )

    # -------------------------
    # VISTA AGREGAR CARRO
    # -------------------------

    vista_carro.controls = [

        ft.Text(
            "Agregar vehículo",
            size=22,
            weight="bold"
        ),

        placa,

        marca,

        modelo,

        ciudad,

        ft.ElevatedButton(
            "Guardar vehículo",
            on_click=guardar_carro
        )
    ]

    # -------------------------
    # VISTA RESERVACIONES
    # -------------------------

   
    

    vista_reservas.controls = [

        ft.Text(
            "Reservaciones",
            size=22,
            weight="bold"
        ),

        lista_reservaciones
    ]

    # -------------------------
    # VISTA PERFIL
    # -------------------------

    vista_perfil.controls = [

        ft.Text(
            "Mi Perfil",
            size=22,
            weight="bold"
        ),

        nombre_conductor,

        cedula_conductor,

        celular_conductor,

        ft.ElevatedButton(
            "Guardar cambios",
            on_click=guardar_perfil
        )
    ]

    # -------------------------
    # RETORNO
    # -------------------------

    return ft.Container(
        padding=30,

        content=ft.Column(
            [

                ft.Image(
                    src="logo.png",
                    width=250,
                    height=250
                ),

                barra_tabs,

                vista_carro,

                vista_reservas,

                vista_perfil

            ],

            horizontal_alignment="center",
            spacing=20,
            scroll="auto"
        )
    )