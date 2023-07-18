import flet as ft
from assets import theme


class SideMenu(ft.UserControl):
    def __init__(self, app_layout, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_layout = app_layout
        self.page = page
        self.theme = page.theme
        self.visible = True
        self.nav_rail_visible = True
        self.page.on_resize = self.on_resize
        self.page.on_route_change = self.page_route_change

        self.top_nav_items = ft.Column([
            ft.ElevatedButton(
                content=ft.Container(
                    ft.Row([ft.Icon("park_rounded"), ft.Text('Butão 1')]),
                    expand=True, alignment=ft.alignment.center_left,
                ),
                height=50,
                width=220,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), bgcolor=ft.colors.TRANSPARENT, elevation=False),

            ),

            ft.ElevatedButton(
                content=ft.Container(
                    ft.Row([ft.Icon(ft.icons.SOS), ft.Text('Butão 2')]),
                    expand=True, alignment=ft.alignment.center_left
                ),
                height=50,
                width=220,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
            ),

        ],
            spacing=0,
        )

        self.workspace_options = ft.Column(
                    [
                        # divider
                        ft.Container(
                            bgcolor=ft.colors.ON_SECONDARY_CONTAINER,
                            border_radius=ft.border_radius.all(30),
                            height=1,
                            alignment=ft.alignment.center_right,
                            width=200
                        ),
                        self.top_nav_items,

                        # divider
                        ft.Container(
                            bgcolor=ft.colors.ON_SECONDARY_CONTAINER,
                            border_radius=ft.border_radius.all(30),
                            height=1,
                            alignment=ft.alignment.center_right,
                            width=200
                        ),
                    ])


    def set_styles(self):
        print("olá")

    def page_route_change(self, e=None):
        troute = ft.TemplateRoute(self.page.route)
        if troute.match("/"):
            self.layout.back_button.visible = False

    def build(self):
        self.view = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Workspace"),
                ], alignment="spaceBetween"),
                self.workspace_options,
            ],
                # tight=True,
                scroll=ft.ScrollMode.ALWAYS,
            ),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=220,
            # expand=True,
            # bgcolor=ft.colors.SURFACE_VARIANT,
            # bgcolor=ft.colors.BACKGROUND,
            visible=self.nav_rail_visible,
        )

        return self.view

    def toggle_nav_rail(self, e):
        self.view.visible = not self.view.visible
        self.view.update()
        self.page.update()

    def board_name_focus(self, e):
        e.control.read_only = False
        e.control.border = "outline"
        e.control.update()

    def top_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.bottom_nav_rail.selected_index = None
        self.top_nav_rail.selected_index = index
        self.view.update()
        if index == 0:
            self.page.route = "/boards"
        elif index == 1:
            self.page.route = "/members"
        self.page.update()

    def bottom_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.page.route = f"/board/{index}"
        self.view.update()
        self.page.update()

    def on_resize(self, e=None):
        if self.page.window_width < 768:
            self.view.visible = False
        else:
            self.view.visible = self.nav_rail_visible
        self.view.update()

    # def toggle_menus(self, ):
