#!/usr/bin/env python3

preColor = "\x1b"

colorsCommands = {
    "RESET": "[0m",
    "CLEAR": "[2J"
}

colorsForeground = {
    "BLACK": "[2;30m",
    "RED": "[2;31m",
    "GREEN": "[2;32m",
    "YELLOW": "[2;33m",
    "BLUE": "[2;34m",
    "MAGENTA": "[2;35m",
    "CYAN": "[2;36m",
    "WHITE": "[2;37m",
    "BRIGHT_BLACK": "[1;30m",
    "BRIGHT_RED": "[1;31m",
    "BRIGHT_GREEN": "[1;32m",
    "BRIGHT_YELLOW": "[1;33m",
    "BRIGHT_BLUE": "[1;34m",
    "BRIGHT_MAGENTA": "[1;35m",
    "BRIGHT_CYAN": "[1;36m",
    "BRIGHT_WHITE": "[1;37m"
}

colorsBackground = {
    "BLACK": "[24;40m",
    "RED": "[24;41m",
    "GREEN": "[24;42m",
    "YELLOW": "[24;43m",
    "BLUE": "[24;44m",
    "MAGENTA": "[24;45m",
    "CYAN": "[24;46m",
    "WHITE": "[24;47m",
    "BRIGHT_BLACK": "[4;40m",
    "BRIGHT_RED": "[4;41m",
    "BRIGHT_GREEN": "[4;42m",
    "BRIGHT_YELLOW": "[4;43m",
    "BRIGHT_BLUE": "[4;44m",
    "BRIGHT_MAGENTA": "[4;45m",
    "BRIGHT_CYAN": "[4;46m",
    "BRIGHT_WHITE": "[4;47m"
}

if __name__ == "__main__":
    for bg in colorsBackground:
        for fg in colorsForeground:
            color = preColor + colorsBackground[bg]
            color += preColor + colorsForeground[fg]
            reset = preColor + colorsCommands["RESET"]
            print(color + bg + " | " + fg + reset)