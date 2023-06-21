import flet
import flet as ft
import dialog
from utilities.calendar import FletCalendar


def main(page: ft.Page):
    page.title = "AlertDialog examples"
    page.theme_mode = 'light'
    page.calendar = FletCalendar(page)
    page.add(page.calendar)
    # page.add(page.calendar.output)
    page.window_maximized = True
    page.window_min_width = 450

    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_dlg_modal(e):

        page.dialog = dialog.ModalDialog(page)
        page.dialog.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg),
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )


ft.app(target=main)

