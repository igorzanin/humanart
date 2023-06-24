import flet
import flet as ft
import job_popup
from utilities.calendar import FletCalendar
from app import AppLayout
from mobile_menu import MobileMenu

BC = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.BASIC,
    drag_interval=50,
)


class HumanartApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.appbar = ft.Container(width=float("inf"),
                                   margin=0,
                                   padding=0,
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

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.MENU,
            bgcolor=ft.colors.LIME,
            on_click=self.open_mobile_menu,
            visible=False
        )

        self.page.floating_action_button = self.floating_action_button

        mobile_menu = MobileMenu(self, self.page)
        menu_stack = ft.Stack([mobile_menu], height=float("inf"), width=float("inf"))
        self.page.mobile_menu = menu_stack

        self.menu_display = ft.Container(
            width=275,
            height=350,
            bgcolor='white',
            right=10,
            border_radius=ft.border_radius.only(0, 0, 5, 5),
            animate=ft.animation.Animation.curve,
            border=ft.border.only(bottom=ft.border.BorderSide(3, ft.colors.LIME)),
            padding=0,
            shadow=ft.BoxShadow(
                spread_radius=3,
                blur_radius=8,
                color=ft.colors.BLUE_GREY_100,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.NORMAL,
            )
        )

        self.app_menu = ft.Stack(
            [
                ft.Container(
                    BC,
                    on_click=self.open_app_menu,
                    opacity=0.45,
                ),
                self.menu_display,
            ],
        )

        self.page.appbar = self.appbar
        self.page.update()
        self.page.on_keyboard_event = self.on_keyboard

    def build(self):
        self.layout = AppLayout(
                self,
                self.page,
                tight=True,
                expand=True,
                vertical_alignment="start",
            )

        return self.layout

    def initialize(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [self.appbar, self.layout],
                padding=ft.padding.all(0),
                spacing=0,
            )
        )

        self.page.update()
        self.page.go("/")

    def on_keyboard(self, e: ft.KeyboardEvent):
        if e.key == 'Escape' and self.app_menu.visible is True:
            self.app_menu.visible = False
            self.update()

        if e.key == 'Escape' and self.page.mobile_menu.visible is True:
            self.page.mobile_menu.visible = False
            self.update()

    def open_mobile_menu(self, e=None):
        print('passou aqui')
        self.page.mobile_menu.visible = True
        self.page.update()

    def open_app_menu(self, e=None):
        self.layout.page.mobile_menu.hide_mobile_menu()
        if self.app_menu.visible is True:
            self.app_menu.visible = False

        else:
            self.app_menu.visible = True

        self.update()


def main(page: ft.Page):
    # def on_keyboard(e: ft.KeyboardEvent):
    #     if e.key == 'Escape' and page.app_menu.visible is True:
    #         page.app_menu.visible = False
    #         page.update()
    #
    #     if e.key == 'Escape' and page.mobile_menu.visible is True:
    #         page.mobile_menu.visible = False
    #         page.update()
    #
    # def open_dlg_modal(e):
    #     page.dialog = dialog.ModalDialog(page)
    #     page.dialog.open = True
    #     page.update()
    #     page.dialog.on_resize(None)
    #
    # def on_resize(e):
    #     if page.width < 768:
    #         page.floating_action_button.visible = True
    #         page.update()
    #     else:
    #         page.floating_action_button.visible = False
    #         page.update()
    #
    # def open_mobile_menu(e):
    #     page.app_menu.visible = False
    #     page.dialog = page.mobile_menu
    #     page.mobile_menu.visible = True
    #     page.floating_action_button.icon = ft.icons.CLOSE
    #     page.floating_action_button.on_click = hide_mobile_menu
    #     page.update()
    #
    # def hide_mobile_menu(e):
    #     page.mobile_menu.visible = False
    #     page.floating_action_button.icon = ft.icons.MENU
    #     page.floating_action_button.on_click = open_mobile_menu
    #     page.update()
    #
    # def open_app_menu(e):
    #     hide_mobile_menu(None)
    #     page.dialog = page.app_menu
    #     if page.app_menu.visible is True:
    #         page.app_menu.visible = False
    #
    #     else:
    #         page.app_menu.visible = True
    #
    #     page.update()

    # bc = ft.GestureDetector(
    #     mouse_cursor=ft.MouseCursor.BASIC,
    #     drag_interval=50,
    # )
    page.title = "Humanart"
    page.padding = 0
    page.theme_mode = 'light'
    page.window_min_width = 350
    # page.window_maximized = True
    # page.auto_scroll = True
    app = HumanartApp(page)
    page.add(app)
    page.update()
    app.initialize()


    # page.calendar = FletCalendar(page)
    # dialog = job_popup
    # page.on_resize = on_resize
    # page.bgcolor = 'blue'
    # page.add(page.calendar)
    # page.floating_action_button = ft.FloatingActionButton(
    #     icon=ft.icons.MENU, bgcolor=ft.colors.LIME, on_click=open_mobile_menu, visible=False
    # )
    # white_menu_button_style = ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
    #                                          shape={ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=100)})
    #
    # column = ft.Column([
    #     page.calendar,
    #     ft.ElevatedButton("Open dialog", on_click=open_mobile_menu),
    #     ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    # ])
    #
    # page.appbar = ft.Container(width=float("inf"),
    #                            margin=0,
    #                            padding=0,
    #                            height=75,
    #                            gradient=ft.LinearGradient(
    #             begin=ft.alignment.top_left,
    #             end=ft.Alignment(0.8, 1),
    #             colors=[
    #                 '#0072ff',
    #                 '#00c6ff',
    #             ],
    # )
    # )
    #
    # content = ft.Container(column, expand=True, padding=10)
    # page.add(content)

    # page.appbar = ft.AppBar(
    #     color=ft.colors.PURPLE,
    #     leading_width=100,
    #     title=ft.Container(
    #         ft.Text("HUMANART",
    #                 color='white',
    #                 weight=ft.FontWeight.BOLD,
    #                 ),
    #         alignment=flet.alignment.center_left,
    #         expand=False,
    #         width=150,
    #         height=75,
    #     ),
    #     center_title=False,
    #     bgcolor=ft.colors.LIGHT_BLUE,
    #     actions=[
    #         ft.Container(ft.Row(
    #             [
    #                 ft.IconButton(ft.icons.NOTIFICATIONS, style=white_menu_button_style),
    #                 ft.IconButton(ft.icons.MORE_VERT, style=white_menu_button_style, on_click=open_app_menu),
    #             ],
    #             spacing=3,
    #         ),
    #             padding=10,
    #         )
    #     ],
    # )
    # page.appbar.toolbar_height = 75

    # page.mobile_menu = ft.Stack(
    #     [
    #         ft.Row(
    #             [
    #                 ft.Container(width=220, height=float("inf"), bgcolor='#fafafa'),
    #                 ft.Container(bc, bgcolor='black', expand=True, on_click=hide_mobile_menu, opacity=0.45)
    #             ],
    #             spacing=0,
    #         ),
    #     ],
    #     expand=True,
    # )

    # menu_display = ft.Container(
    #     width=275,
    #     height=350,
    #     bgcolor='white',
    #     right=10,
    #     border_radius=ft.border_radius.only(0, 0, 5, 5),
    #     animate=ft.animation.Animation.curve,
    #     border=ft.border.only(bottom=ft.border.BorderSide(3, ft.colors.LIME)),
    #     padding=0,
    #     shadow=ft.BoxShadow(
    #         spread_radius=3,
    #         blur_radius=8,
    #         color=ft.colors.BLUE_GREY_100,
    #         offset=ft.Offset(0, 0),
    #         blur_style=ft.ShadowBlurStyle.NORMAL,
    #     )
    # )

    # page.app_menu = ft.Stack(
    #     [
    #         ft.Container(
    #             bc,
    #             on_click=open_app_menu,
    #             opacity=0.45,
    #         ),
    #         menu_display,
    #     ],
    #     visible=False
    # )

    # page.add(
    #     ft.ElevatedButton("Open dialog", on_click=open_mobile_menu),
    #     ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    # )

    # page.on_keyboard_event = on_keyboard
    # on_resize(None)


ft.app(target=main)
