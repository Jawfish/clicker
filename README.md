# clicker

clicker is a command line click automation tool built in Python for the X window system.

## Requirements

X window system

tkinter

## Installation

**1. Install tkinter:**

Debian and Ubuntu-based distributions:

`sudo apt install python3-tk`

Arch-based distributions:

`sudo pacman -S community/python-pmw`

Solus:

`sudo eopkg it python3-tkinter`

**2. Clone the repository:**

`git clone https://github.com/Jawfish/clicker.git && cd clicker`

**3. Create a virtual environment in which to install clicker and install it:**

`python -m venv clicker && pip install -r requirements.txt -e .`

## Usage

Modify `config.ini` to specify the following values:

`PixelToCheck`, the location of the pixel to watch in the format of X-axis by Y-axis, with the bottom left of the screen being 0x0.

`ClickLocation`, the location to click when the watched pixel matches the desired color in the format of X-axis by Y-axis, with the bottom left of the screen being 0x0.

`ColorToCheck`, the color to check for on the watched pixel in R, G, B format.

`TimeBetweenChecks`, the time between checks in seconds.

`OneShot`, stops the loop after clicking once if set to True, otherwise the program will continue to click at the rate set in TimeBetweenChecks while the watched pixel matches the desired color

## Use Cases

* Clicking a button when a progress bar reaches a certain point

* Switching window focus when a notification appears

## Limitations

Only works on the primary monitor.
