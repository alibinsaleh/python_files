#!/usr/bin python

import pyperclip
import pprint

text = pyperclip.paste()
count = {}
for ch in text:
    count.setdefault(ch, 0)
    count[ch] = count[ch] + 1
    
pprint.pprint(count)


