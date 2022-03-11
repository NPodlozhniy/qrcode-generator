import os
from PIL import Image
import pyqrcode as pyqr
from getpass import getpass
from termcolor import colored

banner = [
    r"   _    __      _  _   _      ___  __  __   __   ",
    r" / _ \ | _ \   | || \ | |    / __||  \/  | |   \  ",
    r"| (_) ||   /   | || \ \ |   | (__ | |\/| | | |) | ",
    r" \__\_\|_|_\   |_||_| \_|    \___||_|  |_| |___/  "
]

for reset in range(0, 2):
    os.system("cls||clear")
    for line in banner:
        for char in line:
            print(colored(char, "white", attrs=["bold"]), end="")
        print()
    print(colored("—" * (len(banner[-1]) - 1), "white", attrs=["bold"]))

    if not reset:
        # Wait for user action
        getpass(colored("WARNING! To be able to read the displayed QR code," + \
                        "you might need to zoom-out your console." + \
                        ".\nPress enter to acknowledge.", "red", attrs=['blink']))

text = input("Input the content of the QR code:")
print()

# Main work by pyqrcode
qr = pyqr.create(text)
qr.show()
qr.png("temp.png")

# Save to the same workdir
qr = Image.open("temp.png")

# In order to display in console
qr_map = []
for x in range(qr.size[0]):
    qr_map.append([])
    for y in range(qr.size[1]):
        qr_map[x].append(qr.getpixel((x, y)))

# Console display
qr_colors = {0: "grey", 255: "white"}
for qr_line in qr_map:
    for qr_col in qr_line:
        print(colored("██", qr_colors[qr_col]), end="")
    print()

# Wait for user action
getpass("\nPress enter to quit.")