# C:\Users\ASIM ASLAM\Desktop\project\router\custom_log.py

def Log(tag="", message=""):
    with open("Log.txt", "a") as f:
        f.write(f"{tag}: {message}\n")
