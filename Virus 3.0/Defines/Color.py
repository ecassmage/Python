BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (252, 140, 3)


def getColor(color):
    if not isinstance(color, str):
        return color

    match color.lower():
        case 'black':
            return BLACK
        case 'gray' | 'grey':
            return GRAY
        case 'white':
            return WHITE
        case 'red':
            return RED
        case 'green':
            return GREEN
        case 'blue':
            return BLUE
        case 'yellow':
            return YELLOW
        case 'cyan':
            return CYAN
        case 'magenta':
            return MAGENTA
        case 'orange':
            return ORANGE
