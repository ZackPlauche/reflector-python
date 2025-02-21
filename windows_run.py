import os

os.chdir(__file__[:__file__.rfind('\\')])

os.system('poetry run main.py')
