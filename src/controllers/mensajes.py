import flet as ft


def mostrar_mensaje(lista, page, *args, error=False, **kwargs):

    texto = ""

    for arg in args:
        texto += str(arg) + " "

    if "usuario" in kwargs:
        texto += f"Usuario: {kwargs['usuario']}"

    lista.controls.append(ft.Text(texto))

    page.update()