import os   #Module for working with paths
print(os.getcwd())
print(os.path.relpath('nice'))
print(os.path.getsize(r'c:\Users\kofij\OneDrive\Desktop\MyPython_Library'))

from pathlib import Path

voo = Path('..\Final Paper.docx')
print(voo.home())
print(voo.exists())
print([voo.is_file()])
print(voo.absolute())
print(voo.suffix)   #This is a property not a method

'''with open("Final Paper.docx", "w") as file'''
# open() works best with .txt files
# "w" gives us the option to write the file

