# Overview
This is a simple visual tracker for global drops in The Legend of Zelda

## Requirements
Python 3 is required to run this, and you will also need to install a couple of packages. These are specified in the `requirements.txt` file and can be installed from the command line. Navigate to the repository root and run:
    `pip install -r ./requirements.txt`

Or the requirements can be installed manually as there are only 2:
    TKinter for UI (installed with `pip install tk`)
    keyboard for registering keyboard hotkeys (installed with `pip install keyboard`)

## Running and using the tracker
The tracker can be launched by simply running:
    `python global_tracker.py`

This will open the window and set the current global counter at zero. The numpad keys can be used to increment the count by their respective number. In other words press numpad-1 after killing a single enemy to increment the counter once, or numpad-8 after killing 8 enemies to increment it 8 times.

Pressing numpad 0 will reset the counter back to 0

The script can also be run with just the item table showing by passing in `--small` or simply `-s` on the command line:
    `python global_tracker.py --small`

## Limitations and future work
* The window is not currently resizeable.
* A future update will add a mode that only shows the drop table and not the enemy images
* Hotkeys can't be easily changed.
* The `keyboard` module detects the arrow keys as numpad keys for some reason. 
    * This can be fixed but involves other changes that I'm procrastinating
* There is no way to set the counter to a specific position, only increment it.