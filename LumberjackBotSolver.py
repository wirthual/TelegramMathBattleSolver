
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from time import sleep
from pyscreeze import screenshot

GAME_URL = 'https://tbot.xyz/lumber/#...'
WEBDRIVER_PATH = '/home/raphael/Downloads/chromedriver'

browser = Chrome(WEBDRIVER_PATH)
browser.get(GAME_URL)
sleep(10)
#Start game
buttonLeft = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "button_left")))
buttonLeft.click()

buttonRight = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "button_right")))

for i in range(0,300):
    scs = screenshot()
    manLeft = scs.getpixel((540, 550))
    manLeft = manLeft[0]>205
    for y in range(478,278,-7):
        branchLeft = scs.getpixel((540, y))
        print(branchLeft)
        branchRight = scs.getpixel((660, y))
        if(branchLeft==(18,80,173)):
            pyautogui.press("right")
            pyautogui.press("right")
            break
        if(branchRight==(18,80,173)):
            pyautogui.press("left")
            pyautogui.press("left")
            break
