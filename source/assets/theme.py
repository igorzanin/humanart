import flet as ft


class AppTheme(ft.ColorScheme):
    def __init__(self, light_mode: bool = True):
        super().__init__()
        if light_mode is True:
            self.color_scheme = ft.ColorScheme(
                primary="#006491",
                on_primary="#ffffff",
                primary_container="#f5f5f5",
                on_primary_container="#001e2f",
                secondary="#006b5d",
                on_secondary="#ffffff",
                secondary_container="#77f8e0",
                on_secondary_container="#00201b",
                tertiary="#b90064",
                on_tertiary="#ffffff",
                tertiary_container="#ffd9e2",
                on_tertiary_container="#3e001e",
                error="#ba1a1a",
                on_error="#ffffff",
                error_container="#ffdad6",
                on_error_container="#410002",
                outline="#71787e",
                outline_variant ="#C3C7CF",
                background="#71787e",
                on_background="#001f25",
                surface="#f8fdff",
                on_surface="#001f25",
                surface_tint="#004766",
                surface_variant="#999999",
                on_surface_variant="#41474d",
                inverse_surface="#2F3033",
                on_inverse_surface="#F1F0F4",
                inverse_primary="#5fcfff",
                shadow="#000000",
                scrim="#000000"
            )

        else:
            self.color_scheme = ft.ColorScheme(
                primary="#8aceff",
                on_primary="#00344e",
                primary_container="#004b6f",
                on_primary_container="#c9e6ff",
                secondary="#57dbc4",
                on_secondary="#00372f",
                secondary_container="#005046",
                on_secondary_container="#77f8e0",
                tertiary="#ffb0c9",
                on_tertiary="#650034",
                tertiary_container="#8e004b",
                on_tertiary_container="#ffd9e2",
                error="#ffb4ab",
                on_error="#690005",
                error_container="#93000a",
                on_error_container="#ffdad6",
                outline="#8b9198",
                outline_variant="#C3C7CF",
                background="#001f25",
                on_background="#a6eeff",
                surface="#001f25",
                on_surface="#a6eeff",
                surface_tint="#004766",
                surface_variant="#999999",
                on_surface_variant="#43474E",
                inverse_surface="#2F3033",
                on_inverse_surface="#F1F0F4",
                inverse_primary="#5fcfff",
                shadow="#000000",
                scrim="#000000"
            )
