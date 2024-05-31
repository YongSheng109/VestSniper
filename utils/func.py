import time
import requests
import json
import asyncio
from colorama import Fore, Style
from utils.load import clear
from utils.util import aprint

async def wait(second):
    await asyncio.sleep(second)


def cinput(prompt):
    print(Fore.LIGHTCYAN_EX + prompt, end='', flush=True)
    user_input = input()
    print(Style.RESET_ALL, end='', flush=True)
    return user_input

def config_load(cfg):
    try:
        with open('config.json') as f:
            config = json.load(f)
            return config.get(cfg)
    except FileNotFoundError:
        print(Fore.RED + " Wait what, config.json is missing, how?!")
        return None
    except json.JSONDecodeError:
        print(Fore.RED + " Whoa you edited config.json in the wrong way :<")
        return None

async def get_info(api_key, username):
    url = f"https://api.antisniper.net/v2/convert/hypixel?key={api_key}&player={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data.get('uuid'), data.get('ign')
        else:
            print(Fore.RED + f" > Error retrieving UUID for {username}")
            return None, None
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"Error retrieving UUID: {e}")
        return None, None
    except requests.RequestException as e:
        print(Fore.RED + f"Error retrieving UUID: {e}")
        return None, None

def get_hypixel_status(hypixel_api, uuid):
    url = f"https://api.hypixel.net/v2/status?key={hypixel_api}&uuid={uuid}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data.get('session')
        else:
            print(Fore.RED + f" > Error retrieving status for UUID: {uuid}")
            return None
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"Error retrieving status: {e}")
        return None
    except requests.RequestException as e:
        print(Fore.RED + f"Error retrieving status: {e}")
        return None

async def request_api(api_key, endpoint, username):
    url = f"https://api.antisniper.net/v2/player/{endpoint}?key={api_key}&player={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data
        else:
            print(Fore.RED + f" > Error retrieving data for {username}")
            return None
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"Error making API request: {e}")
        return None
    except requests.RequestException as e:
        print(Fore.RED + f"Error making API request: {e}")
        return None

async def get_player_info(api_key, username):
    url = f"https://api.antisniper.net/v2/player/string?key={api_key}&player={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data
        else:
            print(Fore.RED + f" > Error retrieving player info for {username}")
            return None
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"Error retrieving player info: {e}")
        return None
    except requests.RequestException as e:
        print(Fore.RED + f"Error retrieving player info: {e}")
        return None

async def find_alt(api_key, username):
    url = f"https://api.antisniper.net/v2/player/altfinder?key={api_key}&player={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data.get('data', [])
        else:
            print(Fore.RED + f" > Error retrieving alternative names for {username}")
            return []
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"Error retrieving alternative names: {e}")
        return []

    except requests.RequestException as e:
        print(Fore.RED + f"Error retrieving alternative names: {e}")
        return []

async def get_blacklist_status(api_key, username):
    url = f"https://api.antisniper.net/v2/blacklist?key={api_key}&player={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data.get('blacklisted', False)
        else:
            print(Fore.RED + f" > Error retrieving blacklist status for {username}")
            return False
    except requests.exceptions.HTTPError as e:
        print(Fore.RED + f"Error retrieving blacklist status: {e}")
        return False
    except requests.RequestException as e:
        print(Fore.RED + f"Error retrieving blacklist status: {e}")
        return False

def print_result(username, data):
    aprint(Style.RESET_ALL + Fore.LIGHTCYAN_EX + f" !  Target found in the database (=^-ω-^=)")
    wait(3)
    clear()

def print_winstreaks(data):
    winstreaks = {
        f"{Fore.RESET}- {Fore.LIGHTRED_EX}Overall": "overall_winstreak",
        f"{Fore.RESET}- {Fore.LIGHTRED_EX}Solo": "eight_one_winstreak",
        f"{Fore.RESET}- {Fore.LIGHTRED_EX}Doubles": "eight_two_winstreak",
        f"{Fore.RESET}- {Fore.LIGHTRED_EX}Threes": "four_three_winstreak",
        f"{Fore.RESET}- {Fore.LIGHTRED_EX}Fours": "four_four_winstreak"
    }

    for mode, key in winstreaks.items():
        print(f"  {Fore.LIGHTRED_EX}{mode} E-WS{Fore.RESET}: {data.get(key, 0)}")

def print_hypixel_status(hypixel_api, uuid):
    hypixel_status = get_hypixel_status(hypixel_api, uuid)
    if hypixel_status is None:
        return
    print()
    print(f"{Fore.RED}  Hypixel{Fore.RESET}")
    print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}Status{Fore.RESET}: {'Online' if hypixel_status['online'] else 'Offline'}")
    if hypixel_status.get('gameType'):
        print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}Game Type{Fore.RESET}: {hypixel_status['gameType']}")
    if hypixel_status.get('mode'):
        print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}Mode{Fore.RESET}: {hypixel_status['mode']}")
    if hypixel_status.get('map'):
        print(f"  {Fore.RESET}- {Fore.LIGHTRED_EX}Map{Fore.RESET}: {hypixel_status['map']}")
