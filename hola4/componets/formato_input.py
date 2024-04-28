import reflex as rx
import hola4.styles.styles as styles

# Formato de input


def formato_input(icon: str, placeholder: str, _type: str):
    return rx.container(
        rx.hstack(
            rx.icon(
                tag=icon,
                size=40,
                align="center",
                color="white"
            ),
            rx.input(
                placeholder=placeholder,
                type=_type,
                style=styles.INPUT_STYLES,
            ),
            margin_y=styles.spacer.DEFAULT
        )
    )
