import flet as ft


class AppTheme(ft.Theme):
    def __init__(self):
        super().__init__()
        self.color_scheme_seed = 'blue'
        self.color_scheme = ft.ColorScheme(
            primary="#006491",
            on_primary="#ffffff",
            primary_container="#c9e6ff",
            on_primary_container="#001e2f",
            secondary="#006a62",
            on_secondary="#ffffff",
            secondary_container="#72f8e8",
            on_secondary_container="#00201d",
            # on_secondary_container="#808080",
            tertiary="#b90064",
            on_tertiary="#ffffff",
            tertiary_container="#ffd9e2",
            on_tertiary_container="#3e001e",
            error="#ba1a1a",
            on_error="#ffffff",
            error_container="#ffdad6",
            on_error_container="#410002",
            background="#ffffff",
            on_background="#001f25",
            surface="#f8fdff",
            on_surface="#001f25",
            outline="#71787e",
            surface_variant="#f5f5f5",
            on_surface_variant="#41474d"
        )

        self.custom_colors = {
            "sucess": ft.colors.LIME
        }

        self.appbar_gradient = [
            '#0072ff',
            '#00c6ff',
        ]

