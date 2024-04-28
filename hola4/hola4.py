import reflex as rx
import hola4.styles.styles as styles

# paginas
from hola4.paginas.login import index


class State(rx.State):
    pass

# Pagina principal de inicio de sesion


# creacion de la pagina
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Concert+One&display=swap",
    ],
    style=styles.BASE_STYLE
)

app.add_page(index)
