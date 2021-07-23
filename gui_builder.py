import winsound
from tkinter import *


def set_master_clock():
    """ Tk object. """
    master_clock = Tk()
    return master_clock


def create_label(obj, kwargs, place_kwargs):
    """Create label"""
    return Label(obj, **kwargs).place(**place_kwargs)


def create_entry(obj, text_variable, kwargs, place_kwargs):
    """Create entry"""
    return Entry(obj, textvariable=text_variable, **kwargs).place(**place_kwargs)


def create_button(obj, kwargs, command, place_kwargs):
    """Create button"""
    return Button(obj, **kwargs, command=command).place(**place_kwargs)


def play_sound():
    """Play alarm sound. """
    # You can use pygame for custom sound
    # pip install pygame
    # import pygame
    # pygame.mixer.init()
    # pygame.mixer.music.load("Iphone Alarm.mp3")
    # pygame.mixer.music.play()
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


def set_clock(clock_info, master_clock, button_command, hour_entry, min_entry, sec_entry):
    """ Build master_clock. """
    master_clock.title(clock_info.get('title', ''))
    master_clock.geometry(clock_info.get('geometry', "400x200"))
    create_label(obj=master_clock,
                 kwargs=clock_info['time_format']['label'],
                 place_kwargs=clock_info['time_format']['place']
                 )
    create_label(obj=master_clock,
                 kwargs=clock_info['add_time']['label'],
                 place_kwargs=clock_info['add_time']['place']
                 )
    create_label(obj=master_clock,
                 kwargs=clock_info['set_alarm']['label'],
                 place_kwargs=clock_info['set_alarm']['place']
                 )
    create_entry(obj=master_clock,
                 text_variable=hour_entry,
                 kwargs=clock_info['hour_entry']['label'],
                 place_kwargs=clock_info['hour_entry']['place']
                 )
    create_entry(obj=master_clock,
                 text_variable=min_entry,
                 kwargs=clock_info['min_entry']['label'],
                 place_kwargs=clock_info['min_entry']['place']
                 )
    create_entry(obj=master_clock,
                 text_variable=sec_entry,
                 kwargs=clock_info['sec_entry']['label'],
                 place_kwargs=clock_info['sec_entry']['place']
                 )
    create_button(obj=master_clock,
                  kwargs=clock_info['set_alarm_button']['label'],
                  command=button_command,
                  place_kwargs=clock_info['set_alarm_button']['place']
                  )

    master_clock.mainloop()
