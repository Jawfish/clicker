# clicker

clicker is a command line click automation tool built in Python for the X window system.

## Requirements

X window system

tkinter

## Usage

Modify `config.ini` to specify the following values:

`PixelToCheck`, The location of the pixel to watch in the format of X-axis by Y-axis, with the top left of the screen being 0x0.

`ClickLocation`, The location to click when the watched pixel matches the desired color in the format of X-axis by Y-axis, with the top left of the screen being 0x0.

`ColorToCheck`, The color to check for on the watched pixel in R, G, B format.

`TimeBetweenChecks`, The time between checks in seconds.

`OneShot`, Stops the loop after clicking once if set to True, otherwise the program will continue to click at the rate set in TimeBetweenChecks while the watched pixel matches the desired color

## Use Cases

* Clicking a button when a progress bar reaches a certain point

* Switching window focus when a notifiation appears

## Limitations

Only works on the primary monitor.
