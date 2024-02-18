# screenCR

pixel-accurate character recognition for known-font screenshots

## why?

because of a [stupid tumblr post](https://www.tumblr.com/maplesynth/742691202686730240).

if you have text data that is stored as a screenshot image only, traditional OCR will fail to recover it for a multitude of reasons. this piece of code aims to match pixel-accurate representations of every known character to reverse the image back into text without making assumptions such as shape guessing or word autocorrection.

## how?

i load up all known glyphs into memory and with a known starting point and line height, brute force my way into checking for which character matches the next one in the original image best. once one is found, it is added to a "recreation" image for verification purposes, along with the associated text being generated as it goes.

## license

```
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42 modified):
 * <maple@maple.pet> wrote this file.  As long as you retain this notice and
 * my credit somewhere you can do whatever you want with this stuff.  If we
 * meet some day, and you think this stuff is worth it, you can buy me a beer
 * in return.
 * ----------------------------------------------------------------------------
 */
 ```