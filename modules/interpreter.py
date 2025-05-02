def process_code (line:str) -> str:
    if line.startswith("بگو "):
        content = line[4:].strip()
        return f"print ({content})"
    if line.startswith("اجرا "):
        content = line[5:].strip()
        return f"os.system({content})"
    if line.startswith("گاو "):
        content = line[4:].strip()
        return f"os.system('cowsay {content}')"
    if line.startswith("روباه "):
        content = line[6:]
        return f"os.system('cowsay -f fox {content}')"
    

    else:
        return line