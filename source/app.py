import flet as ft
import job_popup
from utilities.calendar import FletCalendar

bc = ft.GestureDetector(
    mouse_cursor=ft.MouseCursor.BASIC,
    drag_interval=50,
)


class AppLayout(ft.Row):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.job_dialog = job_popup.ModalDialog(self.page)
        self.page.on_resize = self.page_resize


        # self.mobile_menu = ft.Stack(
        #     [
        #         ft.Row(
        #             [
        #                 ft.Container(width=220, height=float("inf"), bgcolor='#fafafa'),
        #                 ft.Container(bc, bgcolor='black', expand=True, on_click=self.app.hide_mobile_menu, opacity=0.45)
        #             ],
        #             spacing=0,
        #         ),
        #     ],
        #     expand=True,
        # )

        self.container = ft.Container(bgcolor=ft.colors.BLUE)
        self.calendar = FletCalendar(self.page)

        # self.floating_action_button = ft.FloatingActionButton(
        #     icon=ft.icons.MENU,
        #     bgcolor=ft.colors.LIME,
        #     on_click=self.open_mobile_menu,
        #     visible=False
        # )

        column = ft.Column([
            self.calendar,
            ft.ElevatedButton("Open dialog", on_click=self.app.open_mobile_menu),
            ft.ElevatedButton("Open modal dialog", on_click=self.open_job_popup),
        ])

        self._active_view: ft.Control = column
        self.controls = [self._active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.controls[-1] = self._active_view
        self.update()

    def open_job_popup(self, e=None):
        self.job_dialog.open = True
        self.app.update()
        # self.job_dialog.on_resize()

    def page_resize(self, e=None):
        print(self.page.width)
        if self.page.width < 768:
            self.page.floating_action_button.visible = True
            self.page.update()
        else:
            self.page.floating_action_button.visible = False
            self.page.update()
