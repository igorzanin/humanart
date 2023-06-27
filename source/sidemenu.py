import flet as ft
from assets import theme


class SideMenu(ft.UserControl):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.visible = True
        # self.theme: ft.Theme = page.theme
        self.sidebar = ft.Container(
                                     width=200,
                                     padding=0,
                                     margin=0,
                                     bgcolor=ft.colors.SURFACE_VARIANT
                                    )

        self.page.on_route_change = self.set_styles

    def set_styles(self):
        print("olá")

    def build(self):
        return self.sidebar


