import time

def aprint(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

