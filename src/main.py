import flet as ft
from view.booking_view import booking_view

from database.main_sqlite3 import crear_base_de_datos, crear_tabla_reservas

def main(page: ft.Page):

    crear_base_de_datos()
    crear_tabla_reservas()

    page.title = "ReViTe"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "white"
    page.theme_mode = "light"

    page.scroll = "auto"

    page.add(booking_view(page))

ft.app(
    target=main,
    assets_dir="../assets"
)



