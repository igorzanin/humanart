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
                  Tab
                  )
from flet_core import RoundedRectangleBorder, CountinuosRectangleBorder


class ModalDialog(AlertDialog):

    def close_dlg(self, e):
        self.open = False

    def __init__(self):
        super(ModalDialog, self).__init__()
        self.modal = False
        self.shape = CountinuosRectangleBorder()
        self.shape.radius = 3.0
        self.content_padding = 0.0
        self.actions_padding = 0.0

        header_options = Row([
            IconButton(icons.DELETE, icon_size=20,
                       style=flet.ButtonStyle(
                           {"": colors.GREY_400,
                            "hovered": colors.RED}
                       )),

            IconButton(icons.PLAY_CIRCLE, icon_size=20,
                       style=flet.ButtonStyle(
                           {"": colors.GREY_400,
                            "hovered": colors.LIGHT_BLUE_400}
                       )),

            IconButton(icons.ATTACH_FILE, icon_size=20,
                       style=flet.ButtonStyle(
                           {"": colors.GREY_400,
                            "hovered": colors.LIGHT_BLUE_400}
                       )),
        ],
            alignment=flet.MainAxisAlignment.SPACE_AROUND
        )

        title_line = Row([
            Text("   Nome do trabalho"),
            header_options],
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
            height=70
        )

        header = Container(
            content=title_line,
            padding=flet.padding.only(15, 5, 15, 0),
            bgcolor=colors.WHITE,
        )

        tab1 = Container(
            bgcolor=colors.RED
        )

        tab2 = Container(
            Column(controls=[Text('Texto Tab 2')]),
            bgcolor=colors.PURPLE,
        )

        tab = Column([
            Tabs(
                selected_index=0,
                animation_duration=300,
                tabs=[
                    Tab(text='Detalhes', content=tab1),
                    Tab(text='Arquivos', content=tab2),
                ],
                expand=1)
        ]
        )

        side_column = Column(
            [Container(
                content=Text('OI'),
                bgcolor=colors.BLACK54)],
            width=150,
        )

        content = Container(

            content=Column(
                [
                    header,
                    Column([tab, side_column])
                ],
                # alignment=MainAxisAlignment.START,
                scroll=flet.ScrollMode.ALWAYS
            ),
            bgcolor=colors.RED_50,
            width=600,
            height=500
        )
        self.content = content
        self.actions_alignment = MainAxisAlignment.END
