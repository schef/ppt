#!/usr/bin/env python3

preColor = "\x1b"

colorsCommands = {
    "RTT_CTRL_RESET": "[0m",
    "RTT_CTRL_CLEAR": "[2J"
}

colorsForeground = {
    "RTT_CTRL_TEXT_BLACK": "[2;30m",
    "RTT_CTRL_TEXT_RED": "[2;31m",
    "RTT_CTRL_TEXT_GREEN": "[2;32m",
    "RTT_CTRL_TEXT_YELLOW": "[2;33m",
    "RTT_CTRL_TEXT_BLUE": "[2;34m",
    "RTT_CTRL_TEXT_MAGENTA": "[2;35m",
    "RTT_CTRL_TEXT_CYAN": "[2;36m",
    "RTT_CTRL_TEXT_WHITE": "[2;37m",
    "RTT_CTRL_TEXT_BRIGHT_BLACK": "[1;30m",
    "RTT_CTRL_TEXT_BRIGHT_RED": "[1;31m",
    "RTT_CTRL_TEXT_BRIGHT_GREEN": "[1;32m",
    "RTT_CTRL_TEXT_BRIGHT_YELLOW": "[1;33m",
    "RTT_CTRL_TEXT_BRIGHT_BLUE": "[1;34m",
    "RTT_CTRL_TEXT_BRIGHT_MAGENTA": "[1;35m",
    "RTT_CTRL_TEXT_BRIGHT_CYAN": "[1;36m",
    "RTT_CTRL_TEXT_BRIGHT_WHITE": "[1;37m"
}

colorsBackground = {
    "RTT_CTRL_BG_BLACK": "[24;40m",
    "RTT_CTRL_BG_RED": "[24;41m",
    "RTT_CTRL_BG_GREEN": "[24;42m",
    "RTT_CTRL_BG_YELLOW": "[24;43m",
    "RTT_CTRL_BG_BLUE": "[24;44m",
    "RTT_CTRL_BG_MAGENTA": "[24;45m",
    "RTT_CTRL_BG_CYAN": "[24;46m",
    "RTT_CTRL_BG_WHITE": "[24;47m",
    "RTT_CTRL_BG_BRIGHT_BLACK": "[4;40m",
    "RTT_CTRL_BG_BRIGHT_RED": "[4;41m",
    "RTT_CTRL_BG_BRIGHT_GREEN": "[4;42m",
    "RTT_CTRL_BG_BRIGHT_YELLOW": "[4;43m",
    "RTT_CTRL_BG_BRIGHT_BLUE": "[4;44m",
    "RTT_CTRL_BG_BRIGHT_MAGENTA": "[4;45m",
    "RTT_CTRL_BG_BRIGHT_CYAN": "[4;46m",
    "RTT_CTRL_BG_BRIGHT_WHITE": "[4;47m"
}

if __name__ == "__main__":
    for bg in colorsBackground:
        for fg in colorsForeground:
            color = preColor + colorsBackground[bg]
            color += preColor + colorsForeground[fg]
            reset = preColor + colorsCommands["RTT_CTRL_RESET"]
            print(color + bg + " | " + fg + reset)