import flet as ft
from models.clientes import Cliente
from models.carros import Carro
from models.reservas import Reserva
from controllers.mensajes import mostrar_mensaje
from controllers.validaciones import validar_campos
from controllers.validaciones import validar_fecha
from controllers.sesion import Sesion
from controllers.decorador import cargar_reservas

from database.main_sqlite3 import insertar_usuario, insertar_reserva, actualizar_usuario, login_usuario, buscar_usuario_cedula, obtener_carros_por_ciudad


def booking_view(page):
    
    usuario_actual = {"id": None, "cedula": "", "nombre": "", "apellido": "", "celular": ""}
    sesion = Sesion()
    reservas = []

    
    cedula_busqueda = ft.TextField(hint_text="Ingrese su cédula", width=300)
    
    registro_cedula = ft.TextField(hint_text="Cédula", width=300)
    registro_nombre = ft.TextField(hint_text="Nombre", width=300)
    registro_apellido = ft.TextField(hint_text="Apellido", width=300)
    registro_celular = ft.TextField(hint_text="Celular", width=300)
    
    registro_password = ft.TextField(
        hint_text="Contraseña",
        password=True,
        width=300
    )

    password_login = ft.TextField(
        hint_text="Contraseña",
        password=True,
        width=300
    )
    
    
    

    
    horario = ft.Dropdown(
        hint_text="Hora de salida",
        width=300,
        options=[
            ft.dropdown.Option("5:00"),
            ft.dropdown.Option("5:30"),
            ft.dropdown.Option("6:00"),
            ft.dropdown.Option("7:00"),
        ],
    )
    
    fecha = ft.TextField(hint_text="Seleccione una fecha", read_only=True, width=300)
    
    seleccion_carro = ft.Dropdown(hint_text="Carro", width=300, options=[])
    seleccion_sector = ft.Dropdown(
        hint_text="Selecciona un sector",
        width=300,
        options=[],
        disabled=True
    )
    
    lista_reservas = ft.Column()
    lista_mensajes = ft.Column()

    
    inicio = ft.Column(horizontal_alignment="center")
    barra_tabs = ft.Row(alignment="center", visible=False)
    vista_reservar = ft.Column(visible=False, horizontal_alignment="center")
    vista_reservas = ft.Column(visible=False)
    vista_perfil = ft.Column(visible=False)

    
    

    # -------- FUNCIONES UI --------
    def cambiar_vista(nombre):
        inicio.visible = False
        vista_reservar.visible = False
        vista_reservas.visible = False
        vista_perfil.visible = False

        if nombre == "reservar":
            vista_reservar.visible = True
        elif nombre == "mis_reservas":
            vista_reservas.visible = True
        elif nombre == "perfil":
            vista_perfil.visible = True

        actualizar_reservas(
            usuario=usuario_actual,
            reservas=reservas
        )
        actualizar_perfil()
        page.update()

    def entrar_cliente(e):

        if cedula_busqueda.value == "" or password_login.value == "":
            mostrar_mensaje(lista_mensajes, page, "Completa los campos", error=True)
            return

        usuario = login_usuario(
            cedula_busqueda.value,
            password_login.value
        )

        if not usuario:
            mostrar_mensaje(lista_mensajes, page, "Cédula o contraseña incorrecta", error=True)
            return

        usuario_actual["id"] = usuario[0]
        usuario_actual["nombre"] = usuario[1]
        usuario_actual["cedula"] = usuario[3]
        usuario_actual["celular"] = usuario[4]

        sesion.iniciar_sesion(usuario_actual)

        mostrar_mensaje(lista_mensajes, page, "✅ Bienvenido")

        inicio.visible = False
        barra_tabs.visible = True

        cambiar_vista("reservar")

    def registrar_nuevo(e):

        if (
            registro_cedula.value == "" or
            registro_nombre.value == "" or
            registro_apellido.value == "" or
            registro_celular.value == "" or
            registro_password.value == ""
        ):
            mostrar_mensaje(lista_mensajes, page, "Completa todos los campos", error=True)
            return

        # ✅ Validar que no exista
        if buscar_usuario_cedula(registro_cedula.value):
            mostrar_mensaje(lista_mensajes, page, "La cédula ya existe", error=True)
            return

        insertar_usuario(
            registro_nombre.value,
            f"{registro_nombre.value.lower()}@revite.com",
            registro_cedula.value,
            registro_celular.value,
            registro_password.value,
        )

        mostrar_mensaje(lista_mensajes, page, "✅ Usuario registrado")

        # ✅ Limpiar campos
        registro_cedula.value = ""
        registro_nombre.value = ""
        registro_apellido.value = ""
        registro_celular.value = ""
        registro_password.value = ""

        page.update()



    def entrar_nuevo(e):

        inicio.controls = [

            ft.Text("Registro nuevo usuario", size=25, weight="bold"),
            registro_cedula,
            registro_nombre,
            registro_apellido,
            registro_celular,
            registro_password,

            ft.ElevatedButton("Guardar registro", on_click=registrar_nuevo)
        ]
        page.update()

    def seleccionar_destino(ciudad):

        destino_actual["valor"] = ciudad

        # -------------------
        # CARGAR CARROS
        # -------------------

        seleccion_carro.options.clear()

        carros = obtener_carros_por_ciudad(ciudad)

        for carro in carros:

            seleccion_carro.options.append(
                ft.dropdown.Option(carro[0])
            )

        # -------------------
        # CARGAR SECTORES
        # -------------------

        seleccion_sector.options.clear()

        sectores = sectores_por_ciudad.get(ciudad, [])

        for sector in sectores:

            seleccion_sector.options.append(
                ft.dropdown.Option(sector)
            )

        seleccion_sector.disabled = False

        page.update()

    def seleccionar_fecha(e):
        fecha.value = e.control.value.strftime("%Y-%m-%d")
        page.update()

    calendario = ft.DatePicker(on_change=seleccionar_fecha)
    page.overlay.append(calendario)

    destino_actual = {"valor": None}

    sectores_por_ciudad = {
        "Bogotá": [
            "Suba",
            "Kennedy",
            "Chapinero",
            "Usaquén"
        ],

        "Ibagué": [
            "El Salado",
            "Picaleña",
            "Mirolindo",
            "Centro"
        ],

        "Espinal": [
            "Caballero y Góngora",
            "Centro",
            "Arkabal",
            "Betania"
        ]
    }

    def reservar(e):
        if not validar_campos(destino_actual["valor"], horario, fecha, seleccion_carro):
            mostrar_mensaje(lista_mensajes, page, "Completa los datos del viaje", error=True)
            return

        if not validar_fecha(fecha):
            mostrar_mensaje(lista_mensajes, page, "No puedes reservar en fechas pasadas", error=True)
            return
            

        cliente = Cliente(
            usuario_actual["cedula"],
            usuario_actual["nombre"],
            usuario_actual["apellido"],
            usuario_actual["celular"],
            "",
            True,
        )

        placa = seleccion_carro.value

        carro = Carro(
            placa,
            "Sin marca",
            "Sin modelo"
        )

        nueva = Reserva(
            cliente,
            destino_actual["valor"],
            horario.value,
            fecha.value,
            carro
        )

        reservas.append(nueva)

        insertar_reserva(
            usuario_actual["id"],
            destino_actual["valor"],
            horario.value,
            fecha.value,
            placa
        )

        cambiar_vista("mis_reservas")

    def confirmar_reserva(reserva, texto, boton):
        reserva.confirmar_reserva()
        texto.value = reserva.imprimir()
        boton.visible = False
        page.update()

    def eliminar_reserva(reserva):
        if reserva in reservas:
            reservas.remove(reserva)
            actualizar_reservas(
                usuario=usuario_actual,
                reservas=reservas
            )
            page.update()
    
    def cerrar_sesion(e):

        page.controls.clear()


        page.add(booking_view(page))

        page.update()
        

    @cargar_reservas
    def actualizar_reservas(**kwargs):

        lista_reservas.controls.clear()

        for r in reservas:

            reserva_id = r.get_id()
            destino = r.get_destino()
            horario = r.get_hora_salida()
            fecha = r.get_fecha_salida()
            carro = r.get_carro()

            texto = ft.Text(
                f"{destino} - {horario} - {fecha} - {carro.get_placa()}"
            )

            boton_confirmar = ft.ElevatedButton("Confirmar")

            boton_confirmar.on_click = lambda e, rr=r, t=texto, b=boton_confirmar: confirmar_reserva(rr, t, b)

            boton_eliminar = ft.ElevatedButton(
                "Eliminar",
                color="white",
                bgcolor="red",
                on_click=lambda e, rr=r: eliminar_reserva(rr)
            )

            lista_reservas.controls.append(
                ft.Container(
                    content=ft.Column([
                        texto,
                        ft.Row([
                            boton_confirmar,
                            boton_eliminar
                        ])
                    ]),
                    bgcolor="#F5F5F5",
                    border_radius=15,
                    padding=15
                )
            )

    def actualizar_perfil():
        perfil_cedula.value = f"Cédula: {usuario_actual['cedula']}"
        perfil_nombre_input.value = usuario_actual["nombre"]
        perfil_celular_input.value = usuario_actual["celular"]
    
    def guardar_cambios_perfil(e):
        print("CLICK EN GUARDAR PERFIL")  

        nombre = perfil_nombre_input.value   
        celular = perfil_celular_input.value

        if nombre == "" or celular == "":   
            mostrar_mensaje(lista_mensajes, page, "Completa los campos del perfil", error=True)
            return

        usuario_actual["nombre"] = nombre
        usuario_actual["celular"] = celular

        actualizar_usuario(
            usuario_actual["cedula"],
            nombre,
            celular
        )

        mostrar_mensaje(lista_mensajes, page, "Perfil actualizado correctamente")

        actualizar_perfil()   
        page.update()
    
    barra_tabs.controls = [
        ft.ElevatedButton("Reservar", on_click=lambda e: cambiar_vista("reservar")),
        ft.ElevatedButton("Mis reservas", on_click=lambda e: cambiar_vista("mis_reservas")),
        ft.ElevatedButton("Mi perfil", on_click=lambda e: cambiar_vista("perfil")),
        ft.ElevatedButton("Cerrar sesión", on_click=cerrar_sesion)
    ]

    inicio.controls = [

        ft.Text(
            "Reserva tu viaje"
        ),

        cedula_busqueda,
        password_login,

        ft.Row([
            ft.ElevatedButton(
                "Soy cliente",
                on_click=entrar_cliente
            ),

            ft.ElevatedButton(
                "Soy nuevo",
                on_click=entrar_nuevo
            ),
        ],
        alignment="center"
        )
    ]

    vista_reservar.controls = [
        ft.Text("Datos del viaje", size=22, weight="bold"),

        ft.Row([
            ft.Container(
                content=ft.Text("Bogotá"),
                bgcolor="#F5F5F5",
                padding=20,
                border_radius=20,
                on_click=lambda e: seleccionar_destino("Bogotá")
            ),

            ft.Container(
                content=ft.Text("Ibagué"),
                bgcolor="#F5F5F5",
                padding=20,
                border_radius=20,
                on_click=lambda e: seleccionar_destino("Ibagué")
            ),

            ft.Container(
                content=ft.Text("Espinal"),
                bgcolor="#F5F5F5",
                padding=20,
                border_radius=20,
                on_click=lambda e: seleccionar_destino("Espinal")
            ),
        ], alignment="center"),

        horario,

        fecha,

        ft.ElevatedButton(
            "Seleccionar fecha",
            on_click=lambda e: setattr(
                calendario,
                "open",
                True
            ) or page.update()
        ),

        seleccion_carro,
        seleccion_sector,

        ft.ElevatedButton(
            "Reservar",
            bgcolor="#1976D2",
            color="white",
            on_click=reservar
        ),

        # MENSAJES DE ERROR O CONFIRMACIÓN
        lista_mensajes
    ]

    vista_reservas.controls = [
        ft.Text("Mis reservas", size=22, weight="bold"),
        lista_reservas,
    ]

    perfil_cedula = ft.Text()

    perfil_nombre_input = ft.TextField(
        label="Nombre"
    )

    perfil_celular_input = ft.TextField(
        label="Celular"
    )

    vista_perfil.controls = [
        ft.Text(
            "Mi perfil",
            size=22,
            weight="bold"
        ),

        ft.Container(
            content=ft.Column([
                perfil_cedula,
                perfil_nombre_input,
                perfil_celular_input,

                ft.ElevatedButton(
                    "Guardar cambios",
                    on_click=guardar_cambios_perfil
                )
            ]),
            bgcolor="#F5F5F5",
            border_radius=20,
            padding=20,
        ),

        lista_mensajes
    ]

    return ft.Container(
        padding=30,
        content=ft.Column([

            
            ft.Image(
                src="logo.png",
                width=320,
                height=320
            ),

            barra_tabs,

            inicio,

            vista_reservar,

            vista_reservas,

            vista_perfil,

        ],
        horizontal_alignment="center",
        spacing=20,
        scroll="auto")
    )



