import reflex as rx
import hola4.styles.styles as styles
from hola4.api.api import ping
# paginas
from hola4.paginas.login import index


class State(rx.State):
    "pass"

# Pagina principal de inicio de sesion


# creacion de la pagina
app = rx.App(
    stylesheets=[
        "/styles.css",
        "https://fonts.googleapis.com/css2?family=Concert+One&display=swap",
    ],
    style=styles.BASE_STYLE
)
app.api.add_api_route("/hello", ping)
