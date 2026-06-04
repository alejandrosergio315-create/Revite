import flet as ft

from view.conductor_view import conductor_view
from database.main_sqlite3 import insertar_conductor, buscar_conductor

def registro_conductor_view(page):

    nombre = ft.TextField(label="Nombre")
    
    cedula = ft.TextField(label="Cédula")
    
    celular = ft.TextField(label="Celular")

    ciudad = ft.Dropdown(
        label="Ciudad",
        width=300,
        options=[
            ft.dropdown.Option("Bogotá"),
            ft.dropdown.Option("Ibagué"),
            ft.dropdown.Option("Espinal")
        ]
    )
    
    password = ft.TextField(
        label="Contraseña",
        password=True
    )
    

    def registrar(e):

        

        if (
            nombre.value == "" or
            cedula.value == "" or
            celular.value == "" or
            password.value == ""
        ):
            return
        

        insertar_conductor(
            nombre.value,
            cedula.value,
            celular.value,
            "",
            ciudad.value,
            password.value
        )

        conductor = buscar_conductor(
            cedula.value
        )

        page.controls.clear()

        page.add(
            conductor_view(
                page,
                conductor
            )
        )

        page.update()

    return ft.Container(
        padding=30,
        content=ft.Column(
            [
                ft.Text(
                    "Registro conductor",
                    size=22,
                    weight="bold"
                ),

                nombre,
                cedula,
                celular,
                ciudad,
                password,

                ft.ElevatedButton(
                    "Registrarme",
                    on_click=registrar
                )
            ],
            horizontal_alignment="center"
        )
    )