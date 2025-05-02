#!/usr/bin/env python3

def process_code (line:str) -> str:
    if line.startswith("بگو "):
        content = line[4:].strip()
        return f"print ({content})"

code = 'بگو "Hello World"'
translated = process_code(code)
print (translated)
exec(translated)

