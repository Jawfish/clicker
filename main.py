#!/usr/bin/env python3
import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
import pyautogui
import logging
import sys
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='log.log')


def PixelAt(x, y):
    w = Gdk.get_default_root_window()
    pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
    return pb.get_pixels()


try:
    watch_x = int(config['DEFAULT']['PixelToCheck'].split('x')[0])
    watch_y = int(config['DEFAULT']['PixelToCheck'].split('x')[1])
    click_x = int(config['DEFAULT']['ClickLocation'].split('x')[0])
    click_y = int(config['DEFAULT']['ClickLocation'].split('x')[1])
    sleep = int(config['DEFAULT']['TimeBetweenChecks'])
    pixel_color = tuple(map(int,
        config['DEFAULT']['ColorToCheck'].replace(' ', '').split(',')))
    one_shot = config['DEFAULT']['OneShot']
except:
    logging.exception('Config error:')


while True:
    if tuple(PixelAt(watch_x, watch_y)) == pixel_color:
        logging.info(f'Found pixel at {watch_x} x {watch_y}')
        pyautogui.click(click_x, click_y)
        logging.info(f'Clicked at {click_x} x {click_x}')
        if one_shot == 'True':
            break;
    time.sleep(sleep)
