import os
import time
import sys
import colorama
from colorama import Fore, Style
import shutil

colorama.init(autoreset=True)

vestsniper_art_lines = [
    Fore.LIGHTRED_EX + Style.BRIGHT + " __     __        _   ____        _                 ",
    Fore.LIGHTRED_EX + Style.BRIGHT + " \\ \\   / /__  ___| |_/ ___| _ __ (_)_ __   ___ _ __ ",
    Fore.LIGHTRED_EX + Style.BRIGHT + "  \\ \\ / / _ \\/ __| __\\___ \\| '_ \\| | '_ \\ / _ \\ '__|",
    Fore.LIGHTRED_EX + Style.BRIGHT + "   \\ V /  __/\\__ \\ |_ ___) | | | | | |_) |  __/ |   ",
    Fore.LIGHTRED_EX + Style.BRIGHT + "    \\_/ \\___||___/\\__|____/|_| |_|_| .__/ \\___|_|   ",
    Fore.LIGHTRED_EX + Style.BRIGHT + "                                   |_|              ",
]

loading_art = [
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}          {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}#         {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}##        {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}###       {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}####      {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}#####     {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}######    {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}#######   {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}########  {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}######### {Fore.LIGHTRED_EX}]",
    Fore.RESET + "              Initializing" + Style.BRIGHT + f" {Fore.LIGHTRED_EX}[{Fore.RESET}##########{Fore.LIGHTRED_EX}]",
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_terminal_size():
    size = shutil.get_terminal_size((80, 20))
    return size.lines, size.columns

def loading_screen(duration):
    clear()
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for frame in loading_art:
            clear()
            rows, columns = get_terminal_size()
            for _ in range(rows // 2 - len(vestsniper_art_lines) // 2 - 2):
                print()
            for line in vestsniper_art_lines:
                print(line.center(columns))
            print()
            print(frame.center(columns))
            time.sleep(duration / len(loading_art))

colorama.deinit()
