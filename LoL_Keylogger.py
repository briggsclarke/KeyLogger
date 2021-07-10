import pynput
import sys
from pynput.keyboard import Key, Listener

def on_press(key):
    global keys, count

    print('{0} pressed '.format(key))
    keys.append(key)
    write_file(keys)
    keys = []


def on_release(key):
    if key == Key.ctrl_l:
        keyChosen = input("Choose a key to count, then press enter: ")[0]
        numPresses = keyCounter(keyChosen)
        print(keyChosen + ' Was pressed ' + str(numPresses) + ' times')
    elif key == Key.esc:
        file = open('log.txt', 'r+')
        file.truncate(0)
        file.close()
        sys.exit()


def keyCounter(chosenKey):
    with open("log.txt", "r+") as infile:
        data = infile.read()
        return data.count(chosenKey)


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:        
            k = str(key).replace("'", "")
            if k.find("Key") != -1:
                k = k.replace("Key", " ")
            f.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
