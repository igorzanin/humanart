import flet as ft

BC = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.BASIC,
    drag_interval=50,
)


class MobileMenu(ft.UserControl):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.visible = False
        self.expand = True
        self.controls = [
            ft.Row(
                [
                    ft.Container(width=220, height=float("inf"), bgcolor='#fafafa'),
                    ft.Container(BC, bgcolor='black', expand=True, on_click=self.hide_mobile_menu, opacity=0.45)
                ],
                spacing=0,
            ),
        ]
        print('depois aqui ')

    def hide_mobile_menu(self, e=None):
        self.visible = False
        self.app.floating_action_button.icon = ft.icons.MENU
        self.update()

