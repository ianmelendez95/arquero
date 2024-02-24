
from subprocess import *

proc = Popen(['python', 'tell-me-why.py'], stdin=PIPE, text=True)
proc.stdin.write("Ain't nothing but a heartache\n")
proc.stdin.write("Ain't nothing but a mistake\n")
proc.stdin.flush()
