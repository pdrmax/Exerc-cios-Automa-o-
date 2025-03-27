import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1

pa.press('win')
pa.write("opera")
pa.press('ENTER')
time.sleep(3)
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(4)
pa.click(x=413, y=156)
pa.write("Arctic Momkeys Pink Pop 2007")
pa.press('ENTER')
time.sleep(3)
pa.click(x=330, y=329)