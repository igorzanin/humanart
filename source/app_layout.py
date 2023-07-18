import flet as ft
from appbar import AppBar
from sidemenu2 import SideMenu
from job_popup import JobPopup
from utilities.calendar import FletCalendar


class AppLayout(ft.Column):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.auto_scroll = True
        self.side_menu = SideMenu(self, page, expand=False)
        self.spacing = 0
        self.calendar = FletCalendar(page)

        # content_area = ft.Column([
        #     self.calendar,
        #     ft.ElevatedButton("Open dialog",
        #                       # on_click=open_mobile_menu
        #                       style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
        #                       ),
        open_job_button = ft.ElevatedButton("Open modal dialog",
                                            on_click=self.open_job_popup,
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                                            )
        dark_light_button = ft.ElevatedButton("Dark/Light mode",
                                              on_click=self.toggle_theme,
                                              bgcolor=page.theme.custom_colors["sucess"],
                                              color=ft.colors.ON_PRIMARY,
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                                              )
        # ])

        content_area = ft.Container(
            ft.Column(
                [
                    ft.ResponsiveRow(
                        [
                            ft.ElevatedButton(content=ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("Planejamento", size=12, color=ft.colors.ON_PRIMARY_CONTAINER),
                                        ft.Text("10", size=35, color=ft.colors.ON_PRIMARY_CONTAINER)
                                    ],
                                    alignment=ft.alignment.center,
                                    tight=True,
                                    spacing=3,
                                ),
                                alignment=ft.alignment.center_left,
                                padding=3,
                            ),
                                expand=True,
                                bgcolor=ft.colors.BACKGROUND,
                                height=110,
                                col=2,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                            ),

                            ft.ElevatedButton(content=ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("Produção", size=12, color=ft.colors.ON_SECONDARY_CONTAINER),
                                        ft.Text("25", size=35, color=ft.colors.ON_SECONDARY_CONTAINER)
                                    ],
                                    alignment=ft.alignment.center,
                                    tight=True,
                                    spacing=3,
                                ),
                                alignment=ft.alignment.center_left,
                                padding=3,
                            ),
                                expand=True,
                                bgcolor=ft.colors.BACKGROUND,
                                style=ft.ButtonStyle(side={
                                    ft.MaterialState.DEFAULT: ft.BorderSide(1.5, ft.colors.BLUE),
                                },
                                    shape=ft.RoundedRectangleBorder(radius=5)),
                                height=110,
                                col=2,
                                # style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                            ),

                            ft.ElevatedButton(content=ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("Aprovação interna", size=12, color=ft.colors.ON_PRIMARY_CONTAINER),
                                        ft.Text("6", size=35, color=ft.colors.ON_PRIMARY_CONTAINER)
                                    ],
                                    alignment=ft.alignment.center,
                                    tight=True,
                                    spacing=3,
                                ),
                                alignment=ft.alignment.center_left,
                                padding=3,
                            ),
                                expand=True,
                                bgcolor=ft.colors.BACKGROUND,
                                height=110,
                                col=2,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                            ),

                            ft.ElevatedButton(content=ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("Aprovação externa", size=12, color=ft.colors.ON_PRIMARY_CONTAINER),
                                        ft.Text("8", size=35, color=ft.colors.ON_PRIMARY_CONTAINER)
                                    ],
                                    alignment=ft.alignment.center,
                                    tight=True,
                                    spacing=3,
                                ),
                                alignment=ft.alignment.center_left,
                                padding=3,
                            ),
                                expand=True,
                                bgcolor=ft.colors.BACKGROUND,
                                height=110,
                                col=2,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                            ),

                            ft.ElevatedButton(content=ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("Arquivo", size=12, color=ft.colors.ON_PRIMARY_CONTAINER),
                                        ft.Text("32", size=35, color=ft.colors.ON_PRIMARY_CONTAINER)
                                    ],
                                    alignment=ft.alignment.center,
                                    tight=True,
                                    spacing=3,
                                ),
                                alignment=ft.alignment.center_left,
                                padding=3,
                            ),
                                expand=True,
                                bgcolor=ft.colors.BACKGROUND,
                                height=110,
                                col=2,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                            ),

                        ],
                        columns=10
                    ),
                    dark_light_button,
                    open_job_button,
                ],
            ),
            padding=15,
            expand=True,
        )

        self.appbar = AppBar(self, page)
        main_row = ft.Row([self.side_menu, content_area], vertical_alignment=ft.CrossAxisAlignment.START)
        self.controls = [self.appbar, main_row]

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
        job_popup_dialog.on_resize(None)
        self.page.update()
