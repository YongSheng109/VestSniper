import requests
import json
import asyncio
import colorama
from colorama import Fore, Style
from utils.moto import moto
from utils.util import aprint
from utils.load import clear, loading_screen
from utils.color import cconvert
from utils.func import *


art = [
    " __     __        _   ____        _                 ",
    " \\ \\   / /__  ___| |_/ ___| _ __ (_)_ __   ___ _ __ ",
    "  \\ \\ / / _ \\/ __| __\\___ \\| '_ \\| | '_ \\ / _ \\ '__|",
    "   \\ V /  __/\\__ \\ |_ ___) | | | | | |_) |  __/ |   ",
    "    \\_/ \\___||___/\\__|____/|_| |_|_| .__/ \\___|_|   ",
    "                                   |_|              " + Fore.RESET,
]

async def main():
    colorama.init()

    api_key = config_load('antisniper_api')
    hypixel_api = config_load('hypixel_api')
    status_time = config_load('status_interval')
    winstreak_time = config_load('winstreak_interval')
    if not api_key or not hypixel_api:
        return

    loading_screen(2)
    clear()

    print()
    aprint(f" {Fore.LIGHTCYAN_EX}Welcome to VestSniper, the only sniper you need!")
    aprint(f" {Fore.LIGHTCYAN_EX}Made by {Fore.RESET}YongSheng {Fore.LIGHTCYAN_EX}(^・ω・^ ){Style.RESET_ALL}")
    print()
    print(f" {Fore.LIGHTCYAN_EX}Status interval{Fore.RESET}: {status_time}")
    print(f" {Fore.LIGHTCYAN_EX}Winstreak interval{Fore.RESET}: {winstreak_time}")
    print()
    username = cinput(f" ♦️ Target: {Fore.RESET}")

    uuid, ign = await get_info(api_key, username)
    if not uuid:
        return

    data = await request_api(api_key, "winstreak", username)
    if data:
        player_info = await get_player_info(api_key, username)
        name = cconvert(player_info.get('minecraft_string'))
        if player_info:
            print_result(username, data)
            player_alt_names = await find_alt(api_key, username)
            blacklist_status = await get_blacklist_status(api_key, username)

            # In the main function, implement separate timers for winstreak and other information
            cached_winstreak = None
            other_info_timer = 0

            while True:
                if player_info:
                    print()
                    moto(art)
                    print(Fore.RESET)
                    print(f"  {Style.RESET_ALL}{Fore.RED}Information{Fore.RESET}")
                    print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}Player{Fore.RESET}: {name}")
                    if player_alt_names:
                        alt_names = [alt.get('ign') for alt in player_alt_names if alt.get('ign') != username]
                        if alt_names:
                            print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}P-Alt{Fore.RESET}: {Style.BRIGHT}{', '.join(alt_names)}{Style.RESET_ALL}")

                # Print cached winstreak initially if available
                if cached_winstreak:
                    print()
                    print(f"{Fore.RED}  Winstreak")
                    print_winstreaks(cached_winstreak)
                    print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}Blacklist{Fore.RESET}: {'True' if blacklist_status else 'False'}")

                if cached_winstreak is None or winstreak_timer >= winstreak_time:
                    data = await request_api(api_key, "winstreak", username)
                    if data:
                        cached_winstreak = data
                        winstreak_timer = 0

                if other_info_timer >= status_time:
                    print_hypixel_status(hypixel_api, uuid)
                    other_info_timer = 0

                winstreak_timer += 2
                other_info_timer += 2

                await wait(1)
                clear()

if __name__ == "__main__":
    asyncio.run(main())