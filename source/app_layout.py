import flet as ft
from appbar import AppBar
from sidemenu import SideMenu
from job_popup import JobPopup
from utilities.calendar import FletCalendar


class AppLayout(ft.Column):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.side_menu = SideMenu(self, page)
        self.spacing = 0
        self.calendar = FletCalendar(page)

        content_area = ft.Column([
            self.calendar,
            ft.ElevatedButton("Open dialog",
                              # on_click=open_mobile_menu
                              ),
            ft.ElevatedButton("Open modal dialog",
                              on_click=self.open_job_popup
                              ),
            ft.ElevatedButton("Dark/Light mode",
                              on_click=self.toggle_theme,
                              bgcolor=page.theme.custom_colors["sucess"],
                              color=ft.colors.ON_PRIMARY,
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                              )
        ])

        main_row = ft.Row([self.side_menu, content_area], expand=True)
        self.controls = [AppBar(self, page), main_row]

    def toggle_theme(self, e=None):
        if self.page.theme_mode == 'dark':
            self.page.theme_mode = 'light'
        else:
            self.page.theme_mode = 'dark'
        self.page.update()

    def open_job_popup(self, e=None):
        job_popup_dialog = JobPopup(self, self.page)
        self.page.dialog = job_popup_dialog
        self.page.add(job_popup_dialog)
        job_popup_dialog.open = True
        self.page.update()
        job_popup_dialog.on_resize(None)
