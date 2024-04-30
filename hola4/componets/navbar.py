import reflex as rx
import hola4.styles.styles as styles
from hola4.componets.formato_button import icon_pushbutton

# barra de navegacion


def navbar() -> rx.Component:
    return rx.hstack(
        rx.avatar(fallback="EM", color_scheme="cyan"),
        rx.text(
            "EdgarM",
            height="40px",
        ),
        rx.button("Hola"),
        rx.button("Hola"),
        rx.button("Hola"),
        icon_pushbutton("heart", ""),
        rx.avatar(fallback="EM", color_scheme="cyan"),
        icon_pushbutton("heart", ""),
        position="sticky",
        bg="blue",
        padding_x="16",
        padding_y="16",
        z_index="999",
    )

# textos para titulos


def textos_titulos(text: str, font: str):
    return rx.container(
        rx.text(
            text,
            size="8",
            weight="medium",
            as_="div",
            color="white",
            font_family="Concert One"
        ),
        margin_y=styles.spacer.VERY_BIG
    )
