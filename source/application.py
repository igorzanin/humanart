import flet as ft
from flet import Page
from flet_core.connection import Connection

import job_popup


# from source.utilities.calendar import FletCalendar

class humanartApp(ft.Container):

    def on_resize(self, e):
        if self.page.width < 768:
            self.floating_action_button.visible = True
            self.page.update()
        else:
            self.hide_mobile_menu(None)
            self.floating_action_button.visible = False
            self.page.update()

    def hide_mobile_menu(self, e):
        self.mobile_menu.visible = False
        self.floating_action_button.icon = ft.icons.MENU
        self.floating_action_button.on_click = self.open_dlg_modal
        self.page.update()

    def open_dlg(self, e):
        self.mobile_menu.visible = True
        self.floating_action_button.icon = ft.icons.CLOSE
        self.floating_action_button.on_click = self.hide_mobile_menu
        self.page.update()

    def open_dlg_modal(self, e):
        self.job_popup.open = True
        self.update()
        self.job_popup.on_resize(None)

    def __init__(self, page: Page):
        super().__init__(width=float("inf"), height=float("inf"))
        self.page = page
        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.MENU, bgcolor=ft.colors.LIME, on_click=self.open_dlg, visible=False
        )
        self.job_popup = job_popup.ModalDialog(self)
        self.mobile_menu = ft.Stack(
            [
                ft.Row(
                    [
                        ft.Container(width=220, height=float("inf"), bgcolor='blue'),
                        ft.Container(bgcolor='black', expand=True, on_click=self.hide_mobile_menu, opacity=0.45)
                    ],
                    spacing=0,
                ),
            ],
            expand=True,
        )

        # calendar = FletCalendar(page)
        # self.add(calendar)

        self.page.add(
            ft.ElevatedButton("Open dialog", on_click=self.open_dlg),
            ft.ElevatedButton("Open modal dialog", on_click=self.open_dlg_modal),
        )

        self.on_resize = self.on_resize
        self.page.update()

