import webbrowser, csv, pyautogui, time
from bs4 import BeautifulSoup


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_extension('/home/akshat/Workspace/Naruto_Scrapping/Nimbus-Screenshot-&-Screen-Video-Recorder_v8.6.5.crx')
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.set_window_size(1366, 768)
## chrome_options.add_extension('/home/akshat/Workspace/Naruto_Scrapping/uBlock-Origin_v1.16.16.crx')



listFile = open('list.csv')
listReader = csv.reader(listFile)



for row in listReader:
    while True:
        try:
            # do stuff
            url = "http://naruto.wikia.com/wiki/%s" % str(row)[8:-2]
            webbrowser.open(url)

            #TO SAVE TIME
            # start = 295

            #INSTEAD OF
            time.sleep(6)
            def detect_start():
                return pyautogui.locateOnScreen('Start2.png')
            # time.sleep(1)

            #TO OPEN NIMBUS SCREEN SELECT & SCROLL
            pyautogui.click(1280,75,button='right')
            pyautogui.typewrite(['down','down','right','down','down','down','enter'])
            time.sleep(1)

            #TO DETECT START
            start = detect_start()
            pyautogui.mouseDown(169, start[1]+15,button='left')
            time.sleep(1)
            #TO DETECT END
            i = 1
            while (i>0):
                if (i==11):
                    #intentional mistake
                    y
                pyautogui.scroll(-5)
                if (pyautogui.locateOnScreen('End2.png') is not None):
                    i=0
                    break
                elif (pyautogui.locateOnScreen('End3.png') is not None):
                    end = pyautogui.locateOnScreen('End3.png')
                    break
                i=i+1

            pend = pyautogui.position()
            if (i==0):
                end = pyautogui.locateOnScreen('End2.png')
            print(end[1])

            #TO SAVE
            pyautogui.dragRel(735,end[1]-pend[1],duration=1)
            pyautogui.moveRel(-364,9,duration=1)
            pyautogui.click()
            time.sleep(5)
            pyautogui.typewrite(['enter'])
            time.sleep(3)
            pyautogui.keyDown('ctrl');pyautogui.press('w');pyautogui.keyUp('ctrl')

        except Exception as e :
            print(e)
            pyautogui.keyDown('ctrl');pyautogui.press('w');pyautogui.keyUp('ctrl')
            continue
        break
