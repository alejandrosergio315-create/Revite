import flet as ft


def mostrar_mensaje(lista, page, *args, error=False):

    texto = ""

    for arg in args:

        texto += str(arg) + " "

    if error:

        lista.controls.append(
            ft.Text(
                texto,
                color="red"
            )
        )

    else:

        lista.controls.append(
            ft.Text(texto)
        )

    page.update()