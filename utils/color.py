from colorama import Fore, Style


MINECRAFT_COLORS = {
    '§0': Fore.BLACK,
    '§1': Fore.LIGHTBLUE_EX,
    '§2': Fore.LIGHTGREEN_EX,
    '§3': Fore.LIGHTCYAN_EX,
    '§4': Fore.LIGHTRED_EX,
    '§5': Fore.LIGHTMAGENTA_EX,
    '§6': Fore.LIGHTYELLOW_EX,
    '§7': Fore.LIGHTWHITE_EX,
    '§8': Fore.LIGHTBLACK_EX,
    '§9': Fore.LIGHTBLUE_EX,
    '§a': Fore.LIGHTGREEN_EX,
    '§b': Fore.LIGHTCYAN_EX,
    '§c': Fore.LIGHTRED_EX,
    '§d': Fore.LIGHTMAGENTA_EX,
    '§e': Fore.LIGHTYELLOW_EX,
    '§f': Fore.WHITE,
}

def cconvert(text):
    for code, color in MINECRAFT_COLORS.items():
        text = text.replace(code, color)
    return text + Style.RESET_ALL 
