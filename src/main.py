import flet as ft
from view.booking_view import booking_view

def main(page: ft.Page):
    page.title = "ReViTe"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "white"
    page.theme_mode = "light"

    page.scroll = "auto"



    page.add(booking_view(page))

ft.app(target=main)



