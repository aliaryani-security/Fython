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
        content = line[6:].strip()
        return f"os.system('cowsay -f fox {content}')"
    if line.startswith("گیت "):
        if line[4:].startswith("فشاربده"):
            return "os.system('git push')"
        elif line[4:].startswith("بکش"):
            return "os.system('git pull')"
    

    else:
        return line