# Importa el módulo 'os' para interactuar con el sistema operativo.
import os

def clean_screen():
    """
    Limpia la pantalla de la consola.

    Esta función detecta el sistema operativo y ejecuta el comando
    de limpieza de pantalla correspondiente ('cls' para Windows, 'clear'
    para otros sistemas como Linux o macOS).
    """
    os.system('cls' if os.name == 'nt' else 'clear')