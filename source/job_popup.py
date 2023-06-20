import flet
import flet_core
from flet import (AlertDialog,
                  TextButton,
                  Text,
                  MainAxisAlignment,
                  Container,
                  Row,
                  colors,
                  alignment,
                  Column,
                  Slider,
                  border_radius,
                  IconButton,
                  icons,
                  Tabs,
                  Tab,
                  TextField,
                  Markdown,
                  ResponsiveRow
                  )

from flet_core import RoundedRectangleBorder, CountinuosRectangleBorder

txt_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed https://flet.dev/docs/controls/markdown#on_tap_link do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n **Ut enim ad minim veniam**, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea ~~commodo consequat~~. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur _sint occaecat cupidatat non proident_, sunt in culpa qui officia deserunt *mollit anim id est laborum.*. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed https://flet.dev/docs/controls/markdown#on_tap_link do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n **Ut enim ad minim veniam**, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea ~~commodo consequat~~. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur _sint occaecat cupidatat non proident_, sunt in culpa qui officia deserunt *mollit anim id est laborum.*"


def header_menu_build():
    button_delete = IconButton(icons.DELETE, icon_size=20,
                               style=flet.ButtonStyle(
                                   {"": colors.GREY_400,
                                    "hovered": colors.RED}
                               ))
    button_play = IconButton(icons.PLAY_CIRCLE, icon_size=20,
                             style=flet.ButtonStyle(
                                 {"": colors.GREY_400,
                                  "hovered": colors.LIGHT_BLUE_400}
                             ))
    button_attach = IconButton(icons.ATTACH_FILE, icon_size=20,
                               style=flet.ButtonStyle(
                                   {"": colors.GREY_400,
                                    "hovered": colors.LIGHT_BLUE_400}
                               ))

    header_options = Container(Row([
        button_delete,
        button_play,
        button_attach,
    ],
        alignment=flet.MainAxisAlignment.END,
        vertical_alignment=flet.CrossAxisAlignment.CENTER,
        width=185),
        margin=flet.margin.only(25, 10, 10, 10)
    )

    return header_options


def header_build():
    style = flet.TextStyle(weight=flet.FontWeight.W_500)

    job_name_input = TextField(value="Nome do trabalho",
                               height=55,
                               border_color='transparent',
                               bgcolor='white',
                               focused_border_width=1.5,
                               content_padding=flet.padding.only(15, 10, 15, 10),
                               filled=True,
                               expand=True,
                               text_size=25,
                               text_style=style
                               )
    title_line = Row([
        job_name_input,
        header_menu_build()],
        vertical_alignment=flet.CrossAxisAlignment.CENTER,
        alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
        height=80
    )

    header = Container(
        content=title_line,
        padding=flet.padding.only(25, 15, 15, 25),
        bgcolor=colors.WHITE,
    )

    return header


class TabsContent(Container):
    def __init__(self):
        super(TabsContent, self).__init__()
        self.content = None
        self.height = 360
        # self.width = float("inf")


class JobPopup(AlertDialog):

    def tabs_build(self):

        self.tab_1 = Column(
            [
                Container(
                    Column(
                        [
                            Text("Descrição"),
                            Text(txt_content)
                        ],
                    ),
                    padding=20)
            ],
            scroll=flet.ScrollMode.HIDDEN,
            visible=True,
        )

        self.tab_2 = Column(
            [
                Container(
                    Column(
                        [
                            Text("Tab2 content"),
                        ],
                    ),
                    padding=20,
                    bgcolor=colors.LIME_50,
                    width=float("inf")
                ),
            ],
            scroll=flet.ScrollMode.HIDDEN,
            visible=True,
        )

    def main_row_build(self):

        def toggle_tabs(b):
            self.content_tab.content = b.data
            self.update()

        style = flet.ButtonStyle(
            shape={
                "": RoundedRectangleBorder(radius=0)
            }
        )

        button_tab1 = TextButton("Detalhes", data=self.tab_1, height=40, style=style, on_click=lambda e: toggle_tabs(button_tab1))
        button_tab2 = TextButton("Arquivos", data=self.tab_2, height=40, style=style, on_click=lambda e: toggle_tabs(button_tab2))
        button_tab3 = TextButton("Artbook", data=self.tab_2, height=40, style=style, on_click=toggle_tabs)

        tabs_header = Container(
            Row(
                [
                    button_tab1,
                    button_tab2,
                    button_tab3
                ],
                scroll=flet.ScrollMode.AUTO,
                spacing=10
            ),
            # height=40,
            padding=flet.padding.only(30, 0, 30, 0),
        )

        tabs = Container(
            Column([
                tabs_header,
                Container(height=1, bgcolor='#dbdbdb', margin=flet.margin.only(25, 0, 25, 0)),
                self.content_tab,
            ],
                spacing=0,
                # scroll=flet.ScrollMode.AUTO,
            ),
            expand=True,
            bgcolor=colors.WHITE,
            padding=0,
            col={"sm": 2, "xs": 3}
        )

        side_container = Container(
            Column(
                [Row(controls=[Text("oi")])
                 ],
                spacing=0,
            ),
            # bgcolor=colors.DEEP_ORANGE_400,
            expand=True,
            height=150,
            padding=10,
            col={"sm": 1, "xs": 3},
        )

        main_row = Container(
            ResponsiveRow([
                tabs,
                side_container
            ],
                columns=3,
                expand=True,
                spacing=0,
            ),
            bgcolor="#f5f5f5",
            # bgcolor=colors.PINK,
            padding=0,
        )

        return main_row

    def close_dlg(self, e):
        self.open = False

    def __init__(self, app):
        super(JobPopup, self).__init__()
        self.modal = False
        self.shape = CountinuosRectangleBorder()
        self.shape.radius = 3.0
        self.content_padding = 0.0
        self.actions_padding = 0.0
        self.app = app
        self.content_tab = TabsContent()
        self.tab_1 = None
        self.tab_2 = None

        self.tabs_build()
        self.content_tab.content = self.tab_1

        self.main_content = Column([
            header_build(),
            self.main_row_build()
        ],
            scroll=flet.ScrollMode.HIDDEN,
            expand=True,
            spacing=0,
        )

        self.content = Container(self.main_content,
                                 width=700,
                                 # height=550,
                                 bgcolor="white",
                                 # expand=True,
                                 )
