# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import sys
from pyfiglet import Figlet
from random import choice

# use the module
figlet = Figlet()

# get a list of available fonts
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    # make a random choice from the font_list
    figlet.setFont(font=choice(font_list))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in font_list:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")

print(figlet.renderText(text))