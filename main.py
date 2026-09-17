import pyautogui,keyboard,time


try:
    while True:
        if keyboard.is_pressed("esc"):
            print("\nUser stopped Macro")
            break

        pyautogui.move(100,0,duration=0.2)
        pyautogui.click()

        pyautogui.move(0,100,duration=0.2)
        pyautogui.click()

        
        pyautogui.move(-100,0,duration=0.2)
        pyautogui.click()

        
        pyautogui.move(0,-100,duration=0.2)
        pyautogui.click()

except KeyboardInterrupt:
    print("\nMacro stopped with Ctrl+C")

