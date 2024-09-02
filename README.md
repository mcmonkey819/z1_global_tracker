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

## Limitations and future work
The window is not currently resizeable and the hotkeys can't be easily changed. There is also no way to set the counter to a specific position, only increment it.