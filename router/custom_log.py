def Log(tag ="" , message = ""):
    with open("Log.text","a") as log:
        log.write(f"{tag}:{message}\n")

