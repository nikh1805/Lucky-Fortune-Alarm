import time
import datetime
from tkinter import StringVar
from gui_builder import set_master_clock, set_clock, play_sound
from input import clock_info


def alarm_runner(set_alarm_timer):
    """ Set alarm runner. """
    while True:
        time.sleep(1)
        ct = datetime.datetime.now()
        now = ct.strftime("%H:%M:%S")
        date = ct.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(f'Current time: {now}, alarm set at - {set_alarm_timer}')
        if now == set_alarm_timer:
            print("Time to Wake up")
            play_sound()
            play_sound()
            play_sound()
            play_sound()
            play_sound()
            break


def set_alarm():
    """ Set alarm. """
    set_alarm_timer = f"{hour_entry.get()}:{min_entry.get()}:{sec_entry.get()}"
    alarm_runner(set_alarm_timer)


# Starts
master_clock = set_master_clock()
hour_entry = StringVar()
min_entry = StringVar()
sec_entry = StringVar()
set_clock(clock_info, master_clock, set_alarm, hour_entry, min_entry, sec_entry)
