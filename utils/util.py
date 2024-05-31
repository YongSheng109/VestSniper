import time

def aprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

