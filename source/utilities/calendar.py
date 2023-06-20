import locale

import flet as ft
import datetime
import calendar
from calendar import HTMLCalendar
from dateutil import relativedelta

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

'''
FletCalendar in Python.

Flet does not have one so I needed to make my own
and I thought I would share.

Author: C. Nichols <mohawke@gmail.com>
License: WTFPL
    WTFPL — Do What the Fuck You Want to Public License

Requirements: You need to install the following.

pip install flet

I suggest you use a Python virtual environment.
That will keep your system Python clean and make
it easier to manage you Flet project.

https://docs.python.org/3/library/venv.html 
'''


class FletCalendar(ft.UserControl):

    def __init__(self, page):
        super().__init__()

        self.page = page
        self.get_current_date()
        self.set_theme()

        # Init the container control.
        self.calendar_container = ft.Container(width=355, height=310,
                                               padding=ft.padding.all(2),
                                               border=ft.border.all(2, self.border_color),
                                               border_radius=ft.border_radius.all(5),
                                               alignment=ft.alignment.bottom_center,
                                               # bgcolor=ft.colors.WHITE,
                                               )

        self.build()  # Build the calendar.
        self.output = ft.Text()  # Add output control.

    def get_current_date(self):
        '''Get the initial current date'''
        today = datetime.datetime.today()
        self.current_month = today.month
        self.current_day = today.day
        self.current_year = today.year

    def selected_date(self, e):
        '''User selected date'''
        self.output.value = e.control.data
        self.current_month = e.control.data[0]
        self.current_day = e.control.data[1]
        self.current_year = e.control.data[2]
        # self.output.update()
        self.build()
        self.calendar_container.update()
        # return e.control.data

    def set_current_date(self):
        '''Set the calendar to the current date.'''
        today = datetime.datetime.today()
        self.current_month = today.month
        self.current_day = today.day
        self.current_year = today.year
        # self.build()
        # self.update()

    def get_next(self, e):
        '''Move to the next month.'''
        current = datetime.date(self.current_year, self.current_month, self.current_day)
        add_month = relativedelta.relativedelta(months=1)
        next_month = current + add_month

        self.current_year = next_month.year
        self.current_month = next_month.month
        self.current_day = next_month.day
        self.build()
        self.calendar_container.update()

    def get_prev(self, e):
        '''Move to the previous month.'''
        current = datetime.date(self.current_year, self.current_month, self.current_day)
        add_month = relativedelta.relativedelta(months=1)
        next_month = current - add_month
        self.current_year = next_month.year
        self.current_month = next_month.month
        self.current_day = next_month.day
        self.build()
        self.calendar_container.update()

    def get_calendar(self):
        '''Get the calendar from the calendar module.'''
        cal = HTMLCalendar()
        return cal.monthdayscalendar(self.current_year, self.current_month)

    def set_theme(self,
                  border_color=ft.colors.GREY_400,
                  text_color=ft.colors.GREY_900,
                  current_day_color=ft.colors.BLUE_ACCENT,
                  selected_button=ft.colors.PURPLE, ):

        self.border_color = border_color
        self.text_color = text_color
        self.current_day_color = current_day_color
        self.selected_button = selected_button

    def build(self):
        '''Build the calendar for flet.'''

        current_calendar = self.get_calendar()

        str_date = '{0} {1}, {2}'.format(calendar.month_name[self.current_month], self.current_day, self.current_year)

        date_display = ft.Text(str_date, text_align='center', size=20, color=self.text_color)

        next_button = ft.Container(
            ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED, icon_size=20,
                          style=ft.ButtonStyle(
                              {"": ft.colors.GREY_400,
                               "hovered": ft.colors.BLUE_ACCENT}
                          )),
            on_click=self.get_next)

        div = ft.Divider(height=1, thickness=2.0, color=self.border_color)

        prev_button = ft.Container(
            ft.IconButton(ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, icon_size=20,
                          style=ft.ButtonStyle(
                              {"": ft.colors.GREY_400,
                               "hovered": ft.colors.BLUE_ACCENT}
                          )),
            on_click=self.get_prev)

        calendar_column = ft.Column(
            [ft.Row([prev_button, date_display, next_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER, height=40, expand=False), div],
            spacing=2, width=355, height=330, alignment=ft.MainAxisAlignment.START, expand=False)

        # Loop weeks and add row.
        for week in current_calendar:
            week_row = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
            # Loop days and add days to row.
            for day in week:
                if day > 0:
                    # print(day)
                    is_current_day_font = ft.FontWeight.W_300
                    is_current_day_bg = ft.colors.WHITE
                    display_day = str(day)
                    if len(str(display_day)) == 1: display_day = '0%s' % display_day
                    if day == self.current_day:
                        is_current_day_font = ft.FontWeight.BOLD
                        is_current_day_bg = self.current_day_color

                    date_button = ft.TextButton(text=display_day,
                                                width=40,
                                                height=40,
                                                aspect_ratio=1,
                                                data=(self.current_month, day, self.current_year),
                                                on_click=self.selected_date,
                                                style=ft.ButtonStyle(color=ft.colors.BLACK,
                                                                     bgcolor=is_current_day_bg,
                                                                     padding=0,
                                                                     shape={
                                                                         ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                                                                             radius=2)
                                                                     },
                                                                     )
                                                )
                    day_button = ft.Container(date_button,
                                              # on_click=self.selected_date,
                                              data=(self.current_month, day, self.current_year),
                                              width=40,
                                              height=40,
                                              ink=True,
                                              alignment=ft.alignment.center,
                                              border_radius=ft.border_radius.all(0),
                                              padding=0,
                                              margin=0,
                                              bgcolor="#fafafa"
                                              )

                else:
                    day_button = ft.Container(width=40,
                                              height=40,
                                              border_radius=ft.border_radius.all(0))

                week_row.controls.append(day_button)

            # Add the weeks to the main column.
            calendar_column.controls.append(week_row)

        # Add column to our page container.
        self.calendar_container.content = calendar_column
        return self.calendar_container
