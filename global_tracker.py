from tkinter import *
import argparse
import keyboard
import os
import threading
import time

image_offset = 5
global_count = 0

########################################################################################################################
def get_highlight_coords(count):
    count = count % 10
    highlight_size = (225, 34)
    highlight_base_coord = (0 + image_offset, 67 + image_offset)
    highlight_increment = 34
    
    x = highlight_base_coord[0]
    y = highlight_base_coord[1] + (highlight_increment * count)
    return ((x, y), (x + highlight_size[0], y + highlight_size[1]))

########################################################################################################################
def timed_highlight_move(canvas, rect_id):
    global_count = 0
    while True:
        time.sleep(2)
        global_count += 1
        move_highlight(global_count, canvas, rect_id)

########################################################################################################################
def move_highlight(count_increment, canvas, rect_id):
    global global_count
    if count_increment is None:
        global_count = 0
    else:
        global_count += count_increment
    new_coords = get_highlight_coords(global_count)[0]
    canvas.moveto(rect_id, new_coords[0], new_coords[1])

########################################################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('--small', '-s', help='Use the small version of the item drops image', action='store_true')
args = parser.parse_args()

root = Tk()

# Create the canvas and the item drops image
if args.small:
    c = Canvas(root, height=410, width=230, bg='black', bd=3)
else:
    c = Canvas(root, height=410, width=704, bg='black', bd=3)

cwd = os.getcwd()
cwd.replace('\\', '/')
image_path = f'{cwd}/itemdrops.png'
img = PhotoImage(file=image_path)
i = c.create_image(image_offset, image_offset, anchor=NW, image=img, activeimage=img, disabledimage=img)

# Create the highlight rectangle
hc = get_highlight_coords(0)
r_width = 5
r = c.create_rectangle(hc[0], hc[1], outline='red', activeoutline='red', disabledoutline='red', width=r_width, activewidth=r_width, disabledwidth=r_width)

c.pack()

# Start the background thread for moving the highlight on a 2s timer for testing
#threading.Thread(target=timed_highlight_move, args=(c, r), daemon=True).start()

# Register the hotkeys for moving the highlight
numpad_codes = [82, 79, 80, 81, 75, 76, 77, 71, 72, 73]
for i in range(1, 10):
    keyboard.add_hotkey(numpad_codes[i], move_highlight, args=(i, c, r))

# Special case for reset which is numpad 0
keyboard.add_hotkey(numpad_codes[0], move_highlight, args=(None, c, r))

root.mainloop()
