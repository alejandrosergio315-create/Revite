import sys
import os
import flet as ft

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(base_path, "..", "assets")


from src.view.booking_view import booking_view

from src.database.main_sqlite3 import crear_base_de_datos, crear_tabla_reservas

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
    assets_dir="assets"
)



