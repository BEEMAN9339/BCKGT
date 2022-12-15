import ctypes
import glob, random, os.path
import time


os.system('cmd /c"start chrome.exe"')
time.sleep(3)
file_path_type = ["./3nfi3iofi/*.png", "./3nfi3iofi/*.jpg"]
images = glob.glob(random.choice(file_path_type))
random_image = random.choice(images)
random_image = os.path.abspath(random_image)

def changeBG(random_image):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, random_image, 2)
    return;

changeBG(random_image)

