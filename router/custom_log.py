def Log(tag : str ="" , message : str = ""):
    with open("Log.txt","a",encoding="utf-8") as log:
        log.write(f"{tag}: {message}\n")

