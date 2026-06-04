import flet as ft

from database.main_sqlite3 import login_conductor
from view.conductor_view import conductor_view
from view.registro_conductor_view import registro_conductor_view


def login_conductor_view(page):

    cedula = ft.TextField(
        label="Cédula"
    )

    password = ft.TextField(
        label="Contraseña",
        password=True
    )

    def ingresar(e):

        conductor = login_conductor(
            cedula.value,
            password.value
        )

        if conductor:

            page.controls.clear()

            page.add(
                conductor_view(
                    page,
                    conductor
                )
            )

            page.update()

        else:

            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Credenciales incorrectas"
                )
            )

            page.snack_bar.open = True

            page.update()
    def abrir_registro(e):

        page.controls.clear()

        page.add(
            registro_conductor_view(page)
        )

        page.update()

    return ft.Container(
        content=ft.Column(
            [

                ft.Image(
                    src="logo.png",
                    width=250,
                    height=250
                ),

                ft.Text(
                    "Ingreso conductor",
                    size=22,
                    weight="bold"
                ),

                cedula,

                password,

                ft.ElevatedButton(
                    "Ingresar",
                    on_click=ingresar
                ),

                ft.ElevatedButton(
                    "Registrarme",
                    on_click=abrir_registro
                ),


            ],
            horizontal_alignment="center"
        )
    )