import flet
import flet as ft
import job_popup
from utilities.calendar import FletCalendar


def main(page: ft.Page):
    page.title = "Humanart"
    page.theme_mode = 'light'
    page.window_min_width = 300
    page.window_maximized = True
    page.auto_scroll = True

    page.calendar = FletCalendar(page)
    page.add(page.calendar)

    def on_resize(e):
        if page.width < 768:
            page.floating_action_button.visible = True
            page.update()
        else:
            hide_mobile_menu(None)
            page.floating_action_button.visible = False
            page.update()

    page.on_resize = on_resize

    def open_dlg(e):
        page.dialog = dlg
        dlg.visible = True
        page.floating_action_button.icon = ft.icons.CLOSE
        page.floating_action_button.on_click = hide_mobile_menu
        page.update()

    def hide_mobile_menu(e):
        dlg.visible = False
        page.floating_action_button.icon = ft.icons.MENU
        page.floating_action_button.on_click = open_dlg
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.MENU, bgcolor=ft.colors.LIME, on_click=open_dlg, visible=False
    )

    dlg = ft.Stack(
        [
            ft.Row(
                [
                    ft.Container(width=220, height=float("inf"), bgcolor='blue'),
                    ft.Container(bgcolor='black', expand=True, on_click=hide_mobile_menu, opacity=0.45)
                ],
                spacing=0,
            ),
        ],
        # width=40,
        # height=40,
        expand=True,
    )

    dialog = job_popup

    def open_dlg_modal(e):
        page.dialog = dialog.ModalDialog(page)
        page.dialog.open = True
        page.update()
        page.dialog.on_resize(None)

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg),
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )

    on_resize(None)


ft.app(target=main)
