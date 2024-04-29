import reflex as rx
from hola4.componets.navbar import textos_titulos
from hola4.componets.formato_button import pushbutton, icon_pushbutton
from hola4.componets.formato_input import formato_input
import hola4.styles.links as links
import hola4.styles.styles as styles


tittle = "RMI | Red de Monitoreo Inteligente"
descrition = """RMI es una innovadora plataforma IoT 
                    diseñada para ofrecer un control total y un monitoreo inteligente de tus 
                    dispositivos y sistemas conectados."""
preview = ""


@rx.page(
    route="/login",
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
def index() -> rx.Component:
    # Fondo de la web
    return rx.container(
        rx.script("document.documentElement.lang='utf-8'"),
        # Contenedor principal
        rx.container(
            # Items integrados en el contenedor
            rx.vstack(
                textos_titulos("Inicio de Sesión", styles.FUENTE_PREDEFINIDA),
                formato_input("user", "Usuario", "email"),
                formato_input("rectangle-ellipsis", "Contraseña", "password"),
                pushbutton("circle-chevron-right", "Iniciar Sesión"),
                rx.container(
                    rx.hstack(
                        icon_pushbutton("github", links.GITHUB_LINK),
                        icon_pushbutton("instagram", links.INSTAGRAM_LINK),
                        icon_pushbutton("youtube", links.YOUTUBE_LINK),
                        icon_pushbutton("facebook", links.FACEBOOK_LINK)
                    )
                ),

                align="center",
            ),
            maxWidth="375px",
            margin="auto",
            width="90%",
            height="65vh",
            minHeight="546px",
            center_content=True,
            border_radius="10px",
            boxShadow="1px 1px 50px #140d3a, -1px 1px 20px 0px #523077",
        ),
        justifyContent="center",
        size="1",
        maxWidth="100%",
        height="100vh",
        background_image="""radial-gradient(circle at 62.28% -19.64%, #794398 0, 
                                #55327a 25%, #321f59 50%, #130d39 75%, #00001e 100%)""",
    )
