import flet
import flet as ft
import job_popup
from utilities.calendar import FletCalendar
from sidemenu import SideMenu
from job_popup import JobPopup
from appbar import AppBar
from app_layout import AppLayout
from assets.theme import AppTheme
from assets.dark_theme import DarkTheme

BC = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.BASIC,
    drag_interval=50,
)


class HumanartApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.title = "Humanart"
        self.page.theme_mode = 'light'
        self.page.spacing = 0
        self.page.window_min_width = 300
        self.page.auto_scroll = True

        self.page.fonts = {
            "FiraSans": "source/assets/FiraSans-Regular.ttf",
            "FiraSansBold": "source/assets/FiraSans-Bold.ttf",
            "FiraSansExtraBold": "source/assets/FiraSans-ExtraBold.ttf",
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }

    def build(self):
        self.app_layout = AppLayout(self, self.page, expand=True)
        self.layout = [self.app_layout]

        return self.layout

    def initialize(self):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                self.layout,
                padding=0,
                spacing=0,
            )
        )

        self.page.update()


def main(page: ft.Page):
    # def window_events(e=None):
    #     print(e.data)
    #
    # def route_change(e=None):
    #     pass
    #
    # def on_keyboard(e: ft.KeyboardEvent):
    #     if e.key == 'Escape' and page.app_menu.visible is True:
    #         page.app_menu.visible = False
    #         page.update()
    #
    #     if e.key == 'Escape' and page.mobile_menu.visible is True:
    #         page.mobile_menu.visible = False
    #         page.update()
    #
    # def open_job_popup(e=None):
    #     job_popup_dialog = JobPopup(page)
    #     page.add(job_popup_dialog)
    #     job_popup_dialog.open = True
    #     page.update()
    #     job_popup_dialog.on_resize()
    #
    # def page_resize(e=None):
    #     if page.width < 768:
    #         page.floating_action_button.visible = True
    #
    #         page.side_menu_container.visible = False
    #         page.update()
    #     else:
    #         page.floating_action_button.visible = False
    #
    #         if page.side_menu_is_opened is True:
    #             page.side_menu_container.visible = True
    #
    #         hide_mobile_menu()
    #         page.update()
    #
    # def open_mobile_menu(e=None):
    #
    #     page.app_menu.visible = False
    #     page.dialog = page.mobile_menu
    #     page.mobile_menu.visible = True
    #     page.floating_action_button.icon = ft.icons.CLOSE
    #     page.floating_action_button.on_click = hide_mobile_menu
    #     page.update()
    #
    # def hide_mobile_menu(e=None):
    #     page.mobile_menu.visible = False
    #     page.floating_action_button.icon = ft.icons.MENU
    #     page.floating_action_button.on_click = open_mobile_menu
    #     page.update()
    #
    # def toggle_theme(e=None):
    #     if page.theme_mode == 'dark':
    #         page.theme_mode = 'light'
    #     else:
    #         page.theme_mode = 'dark'
    #     page.update()
    #
    # def open_app_menu(e=None):
    #     hide_mobile_menu(None)
    #     page.dialog = page.app_menu
    #     if page.app_menu.visible is True:
    #         page.app_menu.visible = False
    #
    #     else:
    #         page.app_menu.visible = True
    #
    #     page.update()
    #
    # page.title = "Humanart"
    # page.theme_mode = 'light'
    # page.theme = AppTheme()
    # page.dark_theme = DarkTheme()
    # page.update()
    #
    # page.spacing = 0
    # page.window_min_width = 300
    # # page.window_maximized = True
    # page.auto_scroll = True
    # page.fonts = {
    #     "FiraSans": "source/assets/FiraSans-Regular.ttf",
    #     "FiraSansBold": "source/assets/FiraSans-Bold.ttf",
    #     "FiraSansExtraBold": "source/assets/FiraSans-ExtraBold.ttf",
    #     "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    # }
    # page.on_resize = page_resize
    # page.on_route_change = route_change
    # page.on_window_event = window_events
    # page.calendar = FletCalendar(page)
    # page.padding = 0
    # page.side_menu_is_opened = True
    # page.floating_action_button = ft.FloatingActionButton(
    #     icon=ft.icons.MENU, bgcolor=ft.colors.LIME, on_click=open_mobile_menu, visible=False
    # )
    #
    # column = ft.Column([
    #     page.calendar,
    #     ft.ElevatedButton("Open dialog", on_click=open_mobile_menu),
    #     ft.ElevatedButton("Open modal dialog", on_click=open_job_popup),
    #     ft.ElevatedButton("Dark/Light mode",
    #                       on_click=toggle_theme,
    #                       bgcolor=page.theme.custom_colors["sucess"],
    #                       color=ft.colors.ON_PRIMARY,
    #                       style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
    #                       )
    # ])
    #
    # page.appbar = AppBar(page)
    # page.side_menu_object = SideMenu(page)
    # page.side_menu_container = ft.Container(page.side_menu_object, visible=True, width=200, padding=0, margin=0)
    # main_row = ft.Row([page.side_menu_container, column])
    # content = ft.Container(main_row, expand=True, padding=0)
    # page.add(content)
    #
    # # page.appbar = ft.AppBar(
    # #     color=ft.colors.PURPLE,
    # #     leading_width=100,
    # #     title=ft.Container(
    # #         ft.Text("HUMANART",
    # #                 color='white',
    # #                 weight=ft.FontWeight.BOLD,
    # #                 ),
    # #         alignment=flet.alignment.center_left,
    # #         expand=False,
    # #         width=150,
    # #         height=75,
    # #     ),
    # #     center_title=False,
    # #     bgcolor=ft.colors.LIGHT_BLUE,
    # #     actions=[
    # #         ft.Container(ft.Row(
    # #             [
    # #                 ft.IconButton(ft.icons.NOTIFICATIONS, style=white_menu_button_style),
    # #                 ft.IconButton(ft.icons.MORE_VERT, style=white_menu_button_style, on_click=open_app_menu),
    # #             ],
    # #             spacing=3,
    # #         ),
    # #             padding=10,
    # #         )
    # #     ],
    # # )
    # # page.appbar.toolbar_height = 75
    #
    # page.mobile_menu = ft.Stack(
    #     [
    #         ft.Row(
    #             [
    #                 SideMenu(page),
    #                 ft.Container(BC, bgcolor='black', expand=True, on_click=hide_mobile_menu, opacity=0.45)
    #             ],
    #             spacing=0,
    #         ),
    #     ],
    #     expand=True,
    # )
    #
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
    #
    # page.app_menu = ft.Stack(
    #     [
    #         ft.Container(
    #             BC,
    #             on_click=open_app_menu,
    #             opacity=0.45,
    #         ),
    #         menu_display,
    #     ],
    #     visible=False
    # )
    #
    # # page.add(
    # #     ft.ElevatedButton("Open dialog", on_click=open_mobile_menu),
    # #     ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    # # )
    #
    # page.on_keyboard_event = on_keyboard
    # page.go('/')
    # # page.update()

    app = HumanartApp(page)
    page.theme = AppTheme()
    page.dark_theme = DarkTheme()
    page.auto_scroll = True
    page.add(app)
    page.update()
    app.initialize()


ft.app(target=main, assets_dir="assets", view=ft.FLET_APP)
