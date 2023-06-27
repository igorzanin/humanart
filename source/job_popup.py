import flet
from flet import (AlertDialog,
                  Text,
                  MainAxisAlignment,
                  Container,
                  Row,
                  colors,
                  Column,
                  IconButton,
                  icons,
                  Tabs,
                  Tab,
                  TextField,
                  Markdown,
                  ResponsiveRow,
                  CountinuosRectangleBorder
                  )
from utilities.calendar import FletCalendar

txt_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed https://flet.dev/docs/controls/markdown#on_tap_link do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n **Ut enim ad minim veniam**, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea ~~commodo consequat~~. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur _sint occaecat cupidatat non proident_, sunt in culpa qui officia deserunt *mollit anim id est laborum.*"


class CalendarPopup(AlertDialog):

    def close_dlg(self, e):
        self.mother.open = True
        self.mother.update()
        self.open = False

    def __init__(self, app, mother_popup: AlertDialog):
        super(CalendarPopup, self).__init__()
        calendar = FletCalendar(app)
        column = Column([
            calendar.output,
            calendar,
        ])
        self.content = Container(calendar, expand=False, height=300, border_radius=10)
        self.shape = CountinuosRectangleBorder()
        self.shape.radius = 10.0
        self.content_padding = 0.0
        self.actions_padding = 0.0
        self.mother = mother_popup
        # self.on_dismiss = self.close_dlg    #if you want to close current popup uncomment this lines


class JobPopup(AlertDialog):

    def tab_content_build(self):

        tab1 = Container(content=(
            Column([
                Text("Descrição:"),
                self.description_input,
                self.description_container

            ],
                scroll=flet.ScrollMode.AUTO)
        ),
            padding=flet.padding.only(0, 15, 0, 15),
            border=flet.border.only(top=flet.border.BorderSide(1, '#dbdbdb')),
            bgcolor=colors.TRANSPARENT,

        )

        tab2 = Container(
            Column(controls=[
                Text('Texto Tab 2'),
            ]),
            bgcolor=colors.PURPLE,
            border=flet.border.only(top=flet.border.BorderSide(1, '#dbdbdb'))

        )

        tab3 = Container(
            Column(controls=[
                self.calendar.output,
                Container(self.calendar.calendar_container),
            ]),
            border=flet.border.only(top=flet.border.BorderSide(1, '#dbdbdb')),
            alignment=flet.alignment.center,
        )

        tabs = Tabs(
            selected_index=0,
            animation_duration=250,
            scrollable=True,
            divider_color='white',
            tabs=[
                Tab(text='Detalhes', content=tab1),
                Tab(text='Arquivos', content=tab2),
                Tab(text="Artbook", content=tab3),
            ],
            height=450,
        )

        return tabs

    def on_resize(self, e=None):
        if self.page.width < 576.0:
            self.menubutton.visible = True
            self.buttons_line.visible = False
            self.update()
        else:
            self.menubutton.visible = False
            self.buttons_line.visible = True
            self.update()

    def close_dlg(self, e):
        if self.popup_view is True:
            self.popup_view = False
            self.open = True
            self.content = self.popup_content
            self.update()
        else:
            self.open = False
            self.app.update()

    def __init__(self, app_layout, page):

        super(JobPopup, self).__init__()
        self.app_layout = app_layout
        self.modal = False
        self.theme = flet.Theme(page.theme)
        self.shape = CountinuosRectangleBorder()
        self.shape.radius = 3.0
        self.content_padding = 0.0
        self.actions_padding = 0.0
        self.app = page
        self.calendar = FletCalendar(page)
        self.popup_view = False
        self.on_dismiss = self.close_dlg
        self.popup_calendar = Container(self.calendar,
                                        expand=False,
                                        height=300,
                                        padding=flet.padding.only(20, 20, 20, 25)
                                        )

        button_delete = IconButton(icons.DELETE, icon_size=20,
                                   col={"xs": 0, "sm": 1},
                                   style=flet.ButtonStyle(
                                       {"": colors.GREY_400,
                                        "hovered": colors.RED}
                                   ))
        button_play = IconButton(icons.PLAY_CIRCLE, icon_size=20,
                                 col=1,
                                 style=flet.ButtonStyle(
                                     {"": colors.GREY_400,
                                      "hovered": colors.LIGHT_BLUE_400}
                                 ))
        button_attach = IconButton(icons.ATTACH_FILE, icon_size=20,
                                   col=1,
                                   style=flet.ButtonStyle(
                                       {"": colors.GREY_400,
                                        "hovered": colors.LIGHT_BLUE_400}
                                   ))

        self.buttons_line = Row(
            [button_delete,
             button_play,
             button_attach
             ],
            width=185,
            spacing=0,
            alignment=flet.MainAxisAlignment.END,
        )

        def open_calendar(e):
            # self.popup_view = True
            # self.content = self.popup_calendar
            # self.update()

            # bottom sheet alternative ===============================
            # bottom_sheet = flet.BottomSheet(content=self.calendar)
            # self.page.add(bottom_sheet)
            # bottom_sheet.open = True
            # bottom_sheet.update()
            #
            # popup alternative ======================================

            # TODO: Need to fix it
            popup_calendar = CalendarPopup(app_layout, self)
            self.page.add(popup_calendar)
            popup_calendar.open = True
            self.page.update()
            # self.open = False       #if you want to close current popup uncomment this lines
            # self.update()

        self.menubutton = IconButton(icons.MORE_VERT,
                                     visible=False,
                                     icon_size=20,
                                     on_click=open_calendar,
                                     style=flet.ButtonStyle(
                                         {"": colors.GREY_900,
                                          "hovered": colors.LIME}
                                     ))

        header_options = Container(Row([
            self.buttons_line,
            self.menubutton,
        ],
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
        ),
            margin=flet.margin.only(35, 10, 10, 10),
        )

        style = flet.TextStyle(weight=flet.FontWeight.W_500)

        job_name_input = TextField(value="Nome do trabalho",
                                   height=55,
                                   border_color='transparent',
                                   bgcolor=colors.BACKGROUND,
                                   focused_border_width=1.5,
                                   content_padding=flet.padding.only(15, 10, 15, 10),
                                   filled=True,
                                   expand=True,
                                   text_size=25,
                                   text_style=style,
                                   )

        title_line = Row([
            job_name_input,
            header_options],
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
            height=80,
        )

        header = Container(
            content=title_line,
            padding=flet.padding.only(25, 15, 15, 25),
            bgcolor=colors.BACKGROUND,
        )

        def update_description_text(e):

            if self.description_input.visible is True:
                self.description_text.value = self.description_input.value
                self.description_input.visible = False
                self.description_container.visible = True
                # self.description_container.bgcolor = 'white'

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
            e.control.bgcolor = colors.SURFACE_VARIANT if e.data == "true" else None
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

        self.side_container = Container(Row(controls=[Text("oi")]),
                                        height=300
                                        )
        self.side_column = Column(
            [self.side_container],
            width=210,
            alignment=flet.alignment.top_right,
            col={"xs": 3, "sm": 1}
        )
        tabs_content = Container(self.tab_content_build(),
                                 # width=float("inf"),
                                 # margin=flet.margin.only(10, 0, 10, 0),
                                 # margin=0,
                                 padding=flet.padding.only(20, 0, 20, 0),
                                 col={"xs": 3, "sm": 2},
                                 bgcolor=colors.BACKGROUND
                                 )

        self.main_row = ResponsiveRow([tabs_content, self.side_column],
                                      spacing=0,
                                      columns=3
                                      )

        self.main_column = Column(
            [
                header,
                Container(self.main_row,
                          # margin=flet.margin.only(20, 0, 20, 0),
                          margin=0,
                          padding=0,
                          ),
            ],
            spacing=0,
            scroll=flet.ScrollMode.AUTO,
        )

        self.popup_content = Container(
            content=self.main_column,
            bgcolor=colors.SURFACE_VARIANT,
            # height=550,
            width=750,
            padding=0,
            margin=0,
        )

        self.app.on_resize = self.on_resize
        self.content = self.popup_content
        self.actions_alignment = MainAxisAlignment.END
