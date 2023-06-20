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

txt_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed https://flet.dev/docs/controls/markdown#on_tap_link do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n **Ut enim ad minim veniam**, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea ~~commodo consequat~~. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur _sint occaecat cupidatat non proident_, sunt in culpa qui officia deserunt *mollit anim id est laborum.*"


class ModalDialog(AlertDialog):

    def tab_content_build(self):

        tab1 = Container(content=(
            Column([
                Text("Descrição:"),
                self.description_input,
                self.description_container,
                self.description_container,
                self.description_container,
            ],
                # wrap=True,
                expand=False,
                scroll=flet.ScrollMode.ALWAYS
            )
        ),
            bgcolor=colors.BROWN,
            padding=flet.padding.only(5, 15, 5, 5),
            border=flet.border.only(top=flet.border.BorderSide(1, '#dbdbdb')),
            expand=True,
        )

        tab2 = Container(
            Column(controls=[Text('Texto Tab 2')]),
            bgcolor=colors.PURPLE,
            expand=False,
            border=flet.border.only(top=flet.border.BorderSide(1, '#dbdbdb'))

        )

        tab3 = Container(
            Column(controls=[Text('Texto Tab 3')]),
            bgcolor=colors.LIME_50,
            expand=False,
            border=flet.border.only(top=flet.border.BorderSide(1, '#dbdbdb'))
        )

        tabs = Container(
            Column([Tabs(
                selected_index=0,
                animation_duration=250,
                tabs=[
                    Tab(text='Detalhes', content=tab1),
                    Tab(text='Arquivos', content=tab2),
                    Tab(text="Artbook", content=tab3)
                ])],
                # scroll=flet.ScrollMode.AUTO,
            ),
            bgcolor=colors.PINK,
            # col={"sm": 2},
            expand=True,
            padding=10,
        )
        return tabs

    def page_resize(self, e):
        if self.app.width <= 635:
            if self.side_column in self.main_row.controls:
                self.side_column.visible = False
                self.under_colum.content = self.side_container
                self.under_colum.visible = True
                self.content.height = None

        else:
            self.side_column.visible = True
            self.side_container.visible = True
            self.under_colum.visible = False
            self.content.height = 550

        self.update()
        print(self.app.width)

    def close_dlg(self, e):
        self.open = False

    def __init__(self, app):

        super(ModalDialog, self).__init__()
        self.modal = False
        self.shape = CountinuosRectangleBorder()
        self.shape.radius = 3.0
        self.content_padding = 0.0
        self.actions_padding = 0.0
        self.app = app

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
            header_options],
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
            height=80
        )

        header = Container(
            content=title_line,
            padding=flet.padding.only(25, 15, 15, 25),
            bgcolor=colors.WHITE,
        )

        def update_description_text(e):

            if self.description_input.visible is True:
                self.description_text.value = self.description_input.value
                self.description_input.visible = False
                self.description_container.visible = True
                self.description_container.bgcolor = 'white'

            else:
                self.description_input.visible = True
                self.description_container.visible = False
                self.description_input.focus()
            self.update()

        self.description_text = Markdown(value=txt_content,
                                         auto_follow_links=True,
                                         selectable=False,
                                         extension_set=flet.MarkdownExtensionSet.GITHUB_FLAVORED)

        def hover_txt_container(e):
            e.control.bgcolor = "#f5f5f5" if e.data == "true" else "white"
            e.control.update()

        self.description_container = Container(self.description_text,
                                               on_hover=hover_txt_container,
                                               visible=True,
                                               on_click=update_description_text,
                                               padding=flet.padding.all(5)
                                               )

        self.description_input = TextField(value=txt_content, border=flet.InputBorder.NONE,
                                           visible=False,
                                           content_padding=2,
                                           multiline=True,
                                           text_size=13,
                                           on_blur=update_description_text)

        self.side_container = Container(Row(controls=[Text("oi")]), expand=True, bgcolor='#f5f5f5')
        self.side_column = Column(
            [self.side_container],
            # expand=True,
            alignment=flet.alignment.top_right,
            visible=True,
            col={"sm": 1},
        )
        tab_header = Container(
            Text("Opções"),
            bgcolor=colors.WHITE,
            height=35,
            # expand=True
        )

        self.tabs_content = Column([
            self.description_container,
            self.description_container,
            self.description_container
        ],
            expand=True,
            # scroll=flet.ScrollMode.AUTO
        )

        tab_content = Column([
            tab_header,
            self.tabs_content
        ],
            expand=True,
            scroll=flet.ScrollMode.AUTO,
            col={"sm": 2},
        )
        self.main_row = ResponsiveRow([tab_content, self.side_column],
                                      expand=True,
                                      columns=3,
                                      vertical_alignment=flet.CrossAxisAlignment.STRETCH,
                                      spacing=10,
                                      )

        self.main_column = Column(
                [
                    Container(header),
                    Container(self.main_row,
                              bgcolor=colors.BROWN,
                              expand=True,
                              padding=flet.padding.only(0, 0, 0, 0),
                              margin=0,
                              # height=550,
                              alignment=flet.alignment.center),
                ],
                expand=True,
                spacing=0,
            )

        content = Container(
            content=Column([self.main_column],
                           expand=True,
                           # scroll=flet.ScrollMode.AUTO
                           ),
            bgcolor=colors.WHITE,
            width=700,
            height=550,
            padding=0,
            margin=0,
            expand=False
        )

        self.content = content
        # self.app.on_resize = self.page_resize
        self.actions_alignment = MainAxisAlignment.END
