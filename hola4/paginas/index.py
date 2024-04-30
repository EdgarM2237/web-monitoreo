import reflex as rx
from hola4.componets.navbar import textos_titulos, navbar
from hola4.componets.formato_button import pushbutton, icon_pushbutton
from hola4.componets.formato_input import formato_input
import hola4.styles.styles as styles


tittle = "RMI | Red de Monitoreo Inteligente"
descrition = """RMI es una innovadora plataforma IoT 
                    diseñada para ofrecer un control total y un monitoreo inteligente de tus 
                    dispositivos y sistemas conectados."""
preview = ""


@rx.page(
    route="/monitoreo",
    title=tittle,
    description=descrition,
    image="/splash.png",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:tittle", "content": tittle},
        {"name": "og:description", "content": descrition},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "sumary_large_image"},
        {"name": "twitter:site", "content": "@RMI"}
    ],
)
def monitoreo() -> rx.Component:
    # Fondo de la web
    return rx.vstack(
        navbar(),
        rx.grid(
            rx.grid(
                # grafica
                rx.container(
                    "Example",
                    bg="orange",
                    width="100%"
                ),
                # datos barras
                rx.container(
                    rx.hstack(
                        "Example",
                        bg="orange",
                        width="100%"
                    )
                ),
                # datos torta
                rx.container(
                    rx.hstack(
                        "Example",
                        bg="orange",
                        width="100%"
                    )
                ),
                rows="3",
                spacing="4",
                width="100%"

            ),
            # datos derecha
            rx.container(
                rx.hstack(
                    "Example",
                    bg="orange",
                    border_radius="3px",
                    width="20%",
                ),
            ),
            columns="2",
            spacing="4",
            width="100%",
        )
    )
