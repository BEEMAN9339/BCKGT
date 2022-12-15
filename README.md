from the read me.txt in the zip file

BCKGT was written by N@N0

If you found this ITS NOT MALEWARE I promise.

All it does is change the background when you open the fake chrome shortcut.


The folder "3nfi3iofi" just contains the .png and .jpg files that are choosen to be the new background.

The fake chrome shortcut is just a short cut to bckgt.exe

bckgt.exe is the script below


Here is the code

'''
import ctypes
import glob, random, os.path
import time


os.system('cmd /c"start chrome.exe"')#		------------------------	this starts chrome(acting like the real chrome shortcut)
time.sleep(3)
file_path_type = ["./3nfi3iofi/*.png", "./3nfi3iofi/*.jpg"]#------------	this is contains the list of .png and .jpg that it chooses from
images = glob.glob(random.choice(file_path_type))#	----------------------	grabs the write file path
random_image = random.choice(images)#	--------------------------------	chooses random file
random_image = os.path.abspath(random_image)#	---------------------------	makes the write path that the code can use(i think, im not really sure)

def changeBG(random_image):#	--------------------------------------------	the function being run
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, random_image, 2)#	----	the code changing the bckground
    return;

changeBG(random_image)#	-------------------------------------------------	running the script that changes the background
'''
written 100% in python 
