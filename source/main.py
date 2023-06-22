import flet
import flet as ft
import job_popup
from utilities.calendar import FletCalendar


def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == 'Escape' and page.app_menu.visible is True:
            page.app_menu.visible = False
            page.update()

        if e.key == 'Escape' and page.mobile_menu.visible is True:
            page.mobile_menu.visible = False
            page.update()

    def open_dlg_modal(e):
        page.dialog = dialog.ModalDialog(page)
        page.dialog.open = True
        page.update()
        page.dialog.on_resize(None)

    def on_resize(e):
        if page.width < 768:
            page.floating_action_button.visible = True
            page.update()
        else:
            hide_mobile_menu(None)
            page.floating_action_button.visible = False
            page.update()

    def open_dlg(e):
        page.dialog = page.mobile_menu
        page.mobile_menu.visible = True
        page.floating_action_button.icon = ft.icons.CLOSE
        page.floating_action_button.on_click = hide_mobile_menu
        page.update()

    def hide_mobile_menu(e):
        page.mobile_menu.visible = False
        page.floating_action_button.icon = ft.icons.MENU
        page.floating_action_button.on_click = open_dlg
        page.update()

    def open_app_menu(e):
        page.dialog = page.app_menu
        if page.app_menu.visible is True:
            page.app_menu.visible = False

        else:
            page.app_menu.visible = True

        page.update()

    page.title = "Humanart"
    page.theme_mode = 'light'
    page.window_min_width = 300
    page.window_maximized = True
    page.auto_scroll = True
    page.on_resize = on_resize
    page.calendar = FletCalendar(page)
    dialog = job_popup
    page.add(page.calendar)
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.MENU, bgcolor=ft.colors.LIME, on_click=open_dlg, visible=False
    )
    white_menu_button_style = ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.WHITE},
                                             shape={ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=100)})

    page.appbar = ft.AppBar(
        leading_width=100,
        title=ft.Container(ft.Text("HUMANART",
                                   color='white',
                                   weight=ft.FontWeight.BOLD,
                                   ),
                           alignment=flet.alignment.center_left,
                           expand=False,
                           width=150,
                           height=75,
                           ),
        center_title=False,
        bgcolor=ft.colors.LIGHT_BLUE,
        actions=[
            ft.Container(ft.Row(
                [
                    ft.IconButton(ft.icons.NOTIFICATIONS, style=white_menu_button_style),
                    ft.IconButton(ft.icons.MORE_VERT, style=white_menu_button_style, on_click=open_app_menu),
                ],
                spacing=3,
            ),
                padding=10,
            )
        ],
    )
    page.appbar.toolbar_height = 75

    page.mobile_menu = ft.Stack(
        [
            ft.Row(
                [
                    ft.Container(width=220, height=float("inf"), bgcolor='#fafafa'),
                    ft.Container(bgcolor='black', expand=True, on_click=hide_mobile_menu, opacity=0.45)
                ],
                spacing=0,
            ),
        ],
        expand=True,
    )

    menu_display = ft.Container(
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

    page.app_menu = ft.Stack(
        [
            ft.Container(
                on_click=open_app_menu,
                opacity=0.45,
            ),
            menu_display,
        ],
        visible=False
    )

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg),
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )

    page.on_keyboard_event = on_keyboard
    on_resize(None)


ft.app(target=main)
