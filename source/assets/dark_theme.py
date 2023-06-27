import flet as ft


class DarkTheme(ft.Theme):
    def __init__(self):
        super().__init__()
        self.color_scheme_seed = 'blue'
        self.color_scheme = ft.ColorScheme(
            primary="#8aceff",
            on_primary="#00344e",
            primary_container="#004b6f",
            on_primary_container="#c9e6ff",
            secondary="#51dbcc",
            on_secondary="#003732",
            secondary_container="#005049",
            on_secondary_container="#72f8e8",
            tertiary="#ffb0c9",
            on_tertiary="#650034",
            tertiary_container="#8e004b",
            on_tertiary_container="#ffd9e2",
            error="#ffb4ab",
            on_error="#690005",
            error_container="#93000a",
            on_error_container="#ffdad6",
            background="#001f25",
            on_background="#a6eeff",
            surface="#001f25",
            on_surface="#a6eeff",
            outline="#8b9198",
            surface_variant="#41474d",
            on_surface_variant="#c1c7ce",
        )
        self.custom_colors = {
            "sucess": "b7f55a"
        }
