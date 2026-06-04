import sys
import os
import flet as ft

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(base_path, "..", "assets")


from view.booking_view import booking_view
from view.conductor_view import conductor_view
from view.login_conductor_view import login_conductor_view

from database.main_sqlite3 import crear_base_de_datos, crear_tabla_reservas, crear_tabla_carros, crear_tabla_conductores


def menu_principal(page):

    def abrir_cliente(e):
        page.controls.clear()
        page.add(booking_view(page))
        page.update()

    def abrir_conductor(e):
        page.controls.clear()
        page.add(login_conductor_view(page))
        page.update()

    return ft.Container(
        padding=30,
        content=ft.Column(
            [
                ft.Image(
                    src="logo.png",
                    width=300,
                    height=300
                ),

                ft.Text(
                    "Bienvenido a ReViTe",
                    size=28,
                    weight="bold"
                ),

                ft.ElevatedButton(
                    "Cliente",
                    width=250,
                    on_click=abrir_cliente
                ),

                ft.ElevatedButton(
                    "Conductor",
                    width=250,
                    on_click=abrir_conductor
                )
            ],
            horizontal_alignment="center"
        )
    )

def main(page: ft.Page):

    crear_base_de_datos()
    crear_tabla_reservas()
    crear_tabla_carros()
    crear_tabla_conductores()

    page.title = "ReViTe"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "white"
    page.theme_mode = "light"

    page.scroll = "auto"

    
    page.add(menu_principal(page))

ft.app(
    target=main,
    assets_dir="../assets"
)



