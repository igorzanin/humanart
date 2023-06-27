import flet as ft


class AppBar(ft.UserControl):
    def __init__(self,app_layout, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_layout = app_layout
        self.page = page
        self.page.on_resize = self.on_resize
        self.hide_menu_button = ft.IconButton(ft.icons.MENU_OPEN, icon_color='white', on_click=self.toggle_side_menu)
        appbar_content = ft.Row([
            self.hide_menu_button,
            ft.Text("HUMANART",
                    font_family="FiraSansBold",
                    size=25,
                    color='white')
        ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.appbar = ft.Container(
            appbar_content,
            width=float("inf"),
            margin=0,
            padding=15,
            height=75,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.Alignment(0.8, 1),
                colors=[
                    '#0072ff',
                    '#00c6ff',
                ],
            )
        )

    def build(self):
        return self.appbar

    def on_resize(self, e=None):
        if self.page.width < 768:
            self.hide_menu_button.visible = False
        else:
            self.hide_menu_button.visible = True
        self.update()

    def toggle_side_menu(self, e=None):
        if self.app_layout.side_menu.visible is True:
            self.hide_menu_button.icon = ft.icons.MENU
            self.app_layout.side_menu.visible = False

        else:
            self.hide_menu_button.icon = ft.icons.MENU_OPEN
            self.app_layout.side_menu.visible = True

        self.update()
        self.page.update()
