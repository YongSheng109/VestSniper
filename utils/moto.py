from colorama import Fore, Style

def moto(lines):
    for line in lines:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + line + Fore.RESET + Style.RESET_ALL)

