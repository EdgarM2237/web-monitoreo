from enum import Enum
import reflex as rx

# espacioadores


class spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    VERY_BIG = "4em"


# fuentes
FUENTE_PREDEFINIDA = "Concert One"

# constantes

# estilos base
BASE_STYLE = {
    rx.button: {
        "width": "200px",
        "height": "60px",
        "font_size": "18px",
        "border": "1px solid #28184d",
        "border_radius": "25px",
        "font_family": "Concert One",
        "background_image": """radial-gradient(circle at -4.17% 4.55%,
                                #321f59 0, #321f59 50%, #321f59 100%)""",
        "_hover": {
            "background_image": """radial-gradient(circle at 56.29% 73.49%, 
                    #342050 0, #321f50 50%, #301e57 100%)"""
        }
    },
    rx.icon_button: {
        "width": "40px",
        "height": "40px",
        "border": "1px solid #28184d",
        "border_radius": "25px",
        "background_image": """radial-gradient(circle at -4.17% 4.55%,
                                #321f59 0, #321f59 50%, #321f59 100%)""",

    }
}

INPUT_STYLES = {
    "font_family": FUENTE_PREDEFINIDA,
    "color": "white",
    "maxheight": "50px",
    "width": "250px",
    "height": "50px",
    "font_size": "18px",
    # "::placeholder": {
    #    "color": "white",
    # },
}
