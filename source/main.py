import flet
import flet as ft
import dialog
import job_popup


def main(page: ft.Page):
    page.title = "AlertDialog examples"
    page.theme_mode = 'light'

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
        # page.dialog.page_resize(e)

    def open_dlg_modal_2(e):

        page.dialog = job_popup.JobPopup(page)
        page.dialog.open = True
        page.update()
        # page.dialog.page_resize(e)

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg),
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
        ft.ElevatedButton("Open modal dialog 2", on_click=open_dlg_modal_2),
    )

    page.scroll = flet.ScrollMode.AUTO


ft.app(target=main)

