'''
    Ansi Colors For FAI-ASISTANT
    Made By Hakan Kaygusuz
    teamflatios@gmail.com send this email for help
'''

# Colors
RESET = '\033[0m'
RED = '\033[31m'
ORANGE = '\033[33m'
YELLOW = '\033[93m'
GREEN = '\033[32m'
BLUE = '\033[34m'
PURPLE = '\033[35m'

# Light Colors
DARK_GREY = '\033[90m'
LIGHT_RED = '\033[91m'
LIGHT_GREEN = '\033[92m'
LIGHT_YELLOW = '\033[93m'
LIGHT_BLUE = '\033[94m'
LIGHT_MAGENTA = '\033[95m'
LIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

# Fonts
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
STRIKETHROUGH = '\033[9m'
INVERT = '\033[7m'

# Effects
BLINK = '\033[5m'
GROW = '\033[6m'
REVERSE = '\033[7m'


# Custom Color
def rgb(r, g, b): return f'\033[38;2;{r};{g};{b}m'

def hex(hex_code): r, g, b = int(hex_code[1:3], 16), int(hex_code[3:5], 16), int(hex_code[5:7], 16); return f'\033[38;2;{r};{g};{b}m'

def rainbow_text(text):
    colored_text, colors = "", [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
    for i, char in enumerate(text): colored_text += colors[i % len(colors)] + char
    return colored_text + RESET
