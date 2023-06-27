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

        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("Boards"),
                label="Boards",
                icon=ft.icons.BOOK_OUTLINED,
                selected_icon=ft.icons.BOOK_OUTLINED
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Members"),
                label="Members",
                icon=ft.icons.PERSON,
                selected_icon=ft.icons.PERSON
            ),

        ]
        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=ft.colors.SURFACE_VARIANT,
            extended=True,
            height=110
        )
        self.bottom_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        self.toggle_nav_rail_button = ft.IconButton(ft.icons.ARROW_BACK)
        self.page.on_route_change = self.set_styles

    def set_styles(self):
        print("olá")

    def build(self):
        self.view = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Workspace"),
                ], alignment="spaceBetween"),
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                self.bottom_nav_rail
            ], tight=True),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            expand=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
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

