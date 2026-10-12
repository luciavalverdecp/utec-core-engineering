#!/usr/bin/env python3
letters = ''
for c in range(97, 123):
    if chr(c) != "q" and chr(c) != "e":
        letters += chr(c)
print(letters)
