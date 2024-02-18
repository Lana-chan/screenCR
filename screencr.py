import math
from PIL import Image, ImageChops
import os

"""
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42 modified):
 * <maple@maple.pet> wrote this file.  As long as you retain this notice and
 * my credit somewhere you can do whatever you want with this stuff.  If we
 * meet some day, and you think this stuff is worth it, you can buy me a beer
 * in return.
 * ----------------------------------------------------------------------------
 */
"""

lower_dir = os.path.join("letters", "lower")
upper_dir = os.path.join("letters", "upper")
special_dir = os.path.join("letters", "special")

names = {
	'slash': '/',
	'plus': '+',
	'colon': ':',
	'semicolon': ';',
	'comma': ',',
	'equals': '='
}

letters = {}
start_y = 4
offset_y = 17
threshold = 80

for filename in os.listdir(lower_dir):
	file = os.path.join(lower_dir, filename)
	letter, type = os.path.splitext(filename)
	if os.path.isfile(file):
		image = Image.open(file)
		letters[letter] = image

for filename in os.listdir(upper_dir):
	file = os.path.join(upper_dir, filename)
	letter, type = os.path.splitext(filename)
	if os.path.isfile(file):
		image = Image.open(file)
		letters[letter.upper()] = image

for filename in os.listdir(special_dir):
	file = os.path.join(special_dir, filename)
	letter, type = os.path.splitext(filename)
	letter = names[letter] if letter in names else letter
	if os.path.isfile(file):
		image = Image.open(file)
		letters[letter] = image

letters = dict(sorted(letters.items(), key=lambda item: item[1].width * item[1].height, reverse=True))

input = Image.open("input.png")

output = Image.new('RGB', input.size, (255,255,255))
outcount = 0
outtext = ""

try:
	for oy in range(math.floor(input.height / offset_y)):
		y = start_y + oy * offset_y
		x = 0
		while x < input.width:
			cdiff = {}
			for letter in letters:
				image = letters[letter]
				box = (x, y, x + image.width, y + image.height)
				test = input.crop(box)
				diff = ImageChops.difference(image,test)
				cdiff[letter] = diff.convert("L").getextrema()[1]
			cdiff = dict(sorted(cdiff.items(), key=lambda item: item[1]))
			letter = list(cdiff)[0]
			if (cdiff[letter] < threshold):
				# ugly hack
				if (letter == 'r' and cdiff['n'] < threshold): letter = 'n'
				box = (x, y, x + letters[letter].width, y + letters[letter].height)
				output.paste(letters[letter], box)
				outtext += letter
				if letter == 'r':
					x += letters[letter].width - 2
				else:
					x += letters[letter].width - 1
			x += 1
except KeyboardInterrupt:
	pass

output.save("output.png")
with open("output.txt", 'w') as f:
	f.write(outtext)

morediff = ImageChops.difference(input.convert("RGB"), output)
morediff.save("diff.png")