from pathlib import Path
"""
path = Path("Indepth-Python\Day8\dice2.py")
print(path.exists())
print(path.rmdir()) #.mkdir() creates a folder while .rmdir removes it.
"""


path = Path()
# print(path.glob("*.*")) #get the files in the current directory
"""
for file in path.glob("*.py"): #all py files in current directory
    print(file)
"""    
for file in path.glob("*"): #all files in current directory
    print(file)
    
    # PyPI   https://pypi.org