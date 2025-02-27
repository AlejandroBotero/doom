import os

list_of_files = os.listdir()

if "DOOM.WAD" in list_of_files:
    os.rename("DOOM.WAD", "DOOM.WADnot")
    os.rename("DOOM2.WADnot", "DOOM2.WAD")

else:
    os.rename("DOOM.WADnot", "DOOM.WAD")
    os.rename("DOOM2.WAD", "DOOM2.WADnot")