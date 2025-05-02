#!/usr/bin/env python3
from modules import interpreter
import os

with open("test_code.fy") as code:
    for line in code:
        if line:
            # print (line)
            translated = interpreter.process_code(line)
            # print (translated)
            exec(translated)

