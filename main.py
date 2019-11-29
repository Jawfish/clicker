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
    watch_offset_x = int(config['DEFAULT']['OffsetToCheck'].split('x')[0])
    watch_offset_y = int(config['DEFAULT']['OffsetToCheck'].split('x')[1])
    click_offset_x = int(config['DEFAULT']['OffsetToClick'].split('x')[0])
    click_offset_y = int(config['DEFAULT']['OffsetToClick'].split('x')[1])
    sleep = int(config['DEFAULT']['TimeBetweenChecks'])
    pixel_color = tuple(
        config['DEFAULT']['ColorToCheck'].replace(' ', '').split(','))
except:
    logging.exception('Config error:')


while True:
    if tuple(PixelAt(watch_offset_x, watch_offset_y)) == pixel_color:
        logging.info(f'Found pixel at {watch_offset_x} x {watch_offset_y}')
        pyautogui.click(click_offset_x, click_offset_y)
        logging.info(f'Clicked at {click_offset_x} x {click_offset_x}')
    time.sleep(sleep)
