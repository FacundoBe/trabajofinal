import os
import locale

# Precio de la entrada sin descuento, esta aqui provisorio, habria que ponerlo en una base de datos ***
PRECIO=100 
# Letras
MAINBAR =("Verdana", 24, 'bold')
TITLE = ("Verdana", 16)
TITLEBOLD = ("Verdana", 16, 'bold')
STDFONT=("Verdana", 12)
SMALLFONT=("Verdana", 10)

# Colores
DARKCOLOR='#363636'
BUTTONCOL='#2d7086'
BUTTONHOV='#19404d'
BUTTONPRESS='#398fac'
BUTTONCLEAR='#bcc2cc'
BACKGROUND='#e3e5e8'
REDBUTTON='#ff5050'




# Ubicacion de assets
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'img') # Ubicacion de las imagenes e iconos img

# Idioma de para los dias y meses de datetime en español
locale.setlocale(locale.LC_TIME, "es_ES")