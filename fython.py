#!/usr/bin/env python3
from modules import interpreter
import os

code = [
    "بگو 'سلام دنیا'"
    , "اجرا 'neofetch'"
    , 'گاو "Hello from Fython , the Farsi Python \\!"'
]
for line in code:
    if line:
        translated = interpreter.process_code(line)
        # print (translated)
        exec(translated)

