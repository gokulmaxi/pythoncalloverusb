import os

import time


device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()

print(device)


print("Waiting for connection ...")

connect = os.popen("adb connect " + device ).read()

print(connect)

os.system("adb shell input tap 340 1030 340 650 100")


os.system("adb shell input keyevent 4")

