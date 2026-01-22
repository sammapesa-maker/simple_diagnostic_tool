# ansi.py
# Simple ANSI color utility with a single public API: design()

_ESC = "\x1b["
_RESET = f"{_ESC}0m"

# Foreground colors
_FG_COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "default": 39,
}

# Background colors
_BG_COLORS = {
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47,
    "default": 49,
}

# Text styles
_STYLES = {
    "bold": 1,
    "dim": 2,
    "underline": 4,
    "blink": 5,
    "reverse": 7,
    "hidden": 8,
}


def design(text, fg=None, bg=None, styles=None, reset=True):
    """
    Apply ANSI colors/styles to text and return the formatted string.

    Parameters:
        text   : any value convertible to str
        fg     : foreground color name (str) or None
        bg     : background color name (str) or None
        styles : list of style names (str) or None
        reset  : whether to append ANSI reset code (bool)

    Returns:
        str
    """
    codes = []

    if fg in _FG_COLORS:
        codes.append(str(_FG_COLORS[fg]))

    if bg in _BG_COLORS:
        codes.append(str(_BG_COLORS[bg]))

    if styles:
        for style in styles:
            if style in _STYLES:
                codes.append(str(_STYLES[style]))

    if not codes:
        return str(text)

    start = f"{_ESC}{';'.join(codes)}m"
    end = _RESET if reset else ""

    return f"{start}{text}{end}"