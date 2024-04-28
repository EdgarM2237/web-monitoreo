import reflex as rx
import hola4.styles.styles as styles
import hola4.styles.links as links


def pushbutton(icon: str, text: str):
    return rx.button(
        text,
        rx.icon(icon),
        margin_top=styles.spacer.DEFAULT,

    )


def icon_pushbutton(icon: str, link: str):
    return rx.link(
        rx.icon_button(
            icon,
            margin_y=styles.spacer.BIG
        ),
        href=link,
        is_external=True,
        button=True
    )
