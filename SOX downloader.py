# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:15:22 2021

@author: R252202
"""

import numpy as np
import cv2
from PIL import ImageGrab
import os
import shutil
import pyautogui as pya
from time import sleep

def getScreenshot():
    img = ImageGrab.grab() #x, y, w, h
    img_np = np.array(img)
    return convertToGrey(img_np)

def convertToGrey(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def findImageLocation09(scr, img):
    w, h = img.shape[::-1]
    res = cv2.matchTemplate(scr, img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    co_x_y = ()
    for pt in zip(*loc[::-1]):
        cv2.rectangle(scr, pt, (pt[0] + w, pt[1] +h), (0, 0, 255), 2)
        co_x_y = pt
    return co_x_y, w, h

def click(loc, w ,h):
    pya.click(loc[0]+w/2, loc[1]+h/2)

    


def searchForFav():
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\fav.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)
    
    #pya.moveTo(co_x_y[0]+w/2, co_x_y[1]+h/2, 0.1)
    #cv2.imwrite('result.png', frame)

def searchFor78():
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\78.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)
    
    #pya.moveTo(co_x_y[0]+w/2, co_x_y[1]+h/2, 0.1)
    #cv2.imwrite('result.png', frame)

def logonerror(login, password):
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\SignInError\\signin.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    
    if len(location) != 0:
        img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\SignInError\\login.PNG")
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        location, w, h = findImageLocation09(scr, img_fav)
        click(location, w, h)
        pya.typewrite(login)
        
        img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\SignInError\\password.PNG")
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        location, w, h = findImageLocation09(scr, img_fav)
        click(location, w, h)
        pya.typewrite(password)
        
        img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\SignInError\\signin.PNG")
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        location, w, h = findImageLocation09(scr, img_fav)
        click(location, w, h)
    else:
        pass
        
def checkForLoading(path):
    loading = True
    login = 'R252202'
    password = "Hugo2020#dog"
    while loading:
        img_fav = cv2.imread(path)
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        logonerror(login, password)
        location, w, h = findImageLocation09(scr, img_fav)
        if len(location) != 0:
            loading = True
        else:
            loading = False

def clickArrow(loc, w ,h):
    pya.click(loc[0]+(w-10), loc[1]+h/2)

def clickSlider(loc, w, h):
    pya.click(loc[0]+(w-10), loc[1]+((3*h)/4))

def clickBox(loc, w, h):
    pya.click(loc[0]+10, loc[1]+h/2)

def clickNextToWhite(loc):
    pya.click(loc[0]-30, loc[1])

def clickText(loc, w, h):
    pya.click(loc[0]+((3*w)/4), loc[1]+h/2)

def getScreenshot78(path):
    img = ImageGrab.grab(bbox=(0, 210, 1500, 465))
    img.save(path + "78Parameters.png")
    sleep(1)

def saveFile():
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\SAVING\\Save.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\SAVING\\Excel.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading3.PNG")
    sleep(1)

def viewReport():
    """
    VIEW REPORT
    """
    #VIEW
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\View.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

def SOX78setupDownload():
    ###SETUP###
    
    
    """
    SBU
    """
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\SBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\SBUall.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    
    #scrolldown
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\SBUfind.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickSlider(location, w, h)      
    pya.press("down")
    
    #boxINC
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\SBUinc.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    """
    STARTDATE
    """
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\StartDate.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickText(location, w, h)

    pya.typewrite(start_date)
    pya.press("enter")
    pya.click(location[0]+30, location[1])
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    """
    ENDDATE
    """
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\EndDate.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickText(location, w, h)
    pya.typewrite(end_date)
    pya.press("enter")
    pya.click(location[0]+30, location[1])
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    """
    FIRST COUNTRY
    """
    #ARROW
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Country.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #BOX DE
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\DE.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    getScreenshot78("g:\\Python projects\\My\\SOX downloader\\Reports\\1 Germany\\")
    """
    VIEW REPORT
    """
    viewReport()
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    """
    DOWNLOAD FIRST REPORT
    """
    saveFile()
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
def moveAndRenameFile(path_from, file, path_to, order, i, start_date):
    try: 
        what_to_replace = str(path_from) + str(file)
        where_to_replace = str(path_to) + str(start_date[6:]) + "-" + str(start_date[0:2]) + "-" +  str(order[i]) + "-" + str(file)
        shutil.move(what_to_replace, where_to_replace)
        i+=1
        return i
    except FileNotFoundError():
        moveAndRenameFile(path_from, file, path_to, order, i, start_date)



def loopOfDoom78(path_order, order, filename, path_from, start_date):
    i = 1
    while i <=(len(path_order)-3): 
        print(path_order[i])
        #country
        img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\" + str(i) + ".PNG" )
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        sleep(1)
        location, w, h = findImageLocation09(scr, img_fav)
        clickArrow(location, w, h)
        
        #unmark previous
        img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\unmark\\" + str(i) + ".PNG")
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        location, w, h = findImageLocation09(scr, img_fav)
        clickBox(location, w, h)
        
        #check next country
        img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\find\\" + str(i) + ".PNG")
        img_fav = convertToGrey(img_fav)
        scr = getScreenshot()
        location, w, h = findImageLocation09(scr, img_fav)
        clickBox(location, w, h)
        clickNextToWhite(location)
        
        sleep(2)
        checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
        sleep(2)
        
        viewReport()
        
        sleep(1)
        checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
        sleep(1)
        
        saveFile()
        sleep(1)
        checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
        sleep(1)
        path_to = path_order[i]
        getScreenshot78(path_order[i])
        sleep(2)
        moveAndRenameFile(path_from, filename, path_to, order, i, start_date)
        sleep(1)
        i+=1
    #IBERICA
    print (path_order[i])
    #country
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\" + str(i) + ".PNG" )
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(1)
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #unmark previous
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\unmark\\" + str(i) + ".PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    
    #check next country
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\find\\PT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\find\\ES.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    sleep(2)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(2)
    
    viewReport()
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    saveFile()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    path_to = path_order[i]
    getScreenshot78(path_order[i])
    sleep(2)
    moveAndRenameFile(path_from, filename, path_to, order, i, start_date)
    sleep(1)
    i+=1

    #TURKEY
    print (path_order[i])
    #country
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\" + str(i) + ".PNG" )
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(1)
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #unmark previous
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\unmark\\ES.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(1)
    
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\unmark\\PT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickBox(location, w, h)
    
    #scroll down
    clickSlider(location, w, h)      
    pya.press("down")
    sleep(1)
    
    #check next country
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\order\\find\\TR.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)

    sleep(2)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(2)
    
    viewReport()
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    saveFile()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    path_to = path_order[i]
    getScreenshot78(path_order[i])
    sleep(2)
    moveAndRenameFile(path_from, filename, path_to, order, i, start_date)
    sleep(1)
    i+=1

    
"""
def captureScreen():
    while True:
        img = ImageGrab.grab() #x, y, w, h
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0Xff == ord('q'):
            break
    cv2.destroyAllWindows()
""" 
############################################## REPORT 144 #####################
def searchFor144():
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\144.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)

def clickBoxToDelete(loc, w, h):
    pya.click(loc[0]+(2*w+100), loc[1]+h/2)

def clickTextAfterDelete(loc, w, h):
    pya.click(loc[0]+(2*w), loc[1]+h/2)

def SOX144setupDownload():
    
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\SETUP\\SBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\SETUP\\SBUall.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    
    #boxINC
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\SETUP\\SBUinc.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    """
    STARTDATE
    """
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\SETUP\\DateFrom.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    
    clickBoxToDelete(location, w, h)
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    clickBoxToDelete(location, w, h)
    
    clickTextAfterDelete(location, w, h)
    pya.typewrite(start_date)
    #pya.press("enter")
    pya.click(location[0], location[1])
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    
    """
    ENDDATE
    """
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\SETUP\\DateTo.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    
    clickTextAfterDelete(location, w, h)
    times = 9
    while times!=0:
        pya.press("backspace")
        times-=1
    pya.typewrite(end_date)
    #pya.press("enter")
    pya.click(location[0], location[1])
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)


def SOX144countrySetupCountry(path_order, i, order):
    #COUNTRY
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\CO.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
        
    #boxINC
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\order\\" + str(i+1) + ".PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

def SOX144countrySetupOrg(path_order, i, order):
    #ORGANIZATION
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\ORG.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
        
    #boxINC
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\orderOrg\\" + str(i+1) + ".PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)


def getScreenshot144(path):
    img = ImageGrab.grab(bbox=(0, 210, 1500, 320))
    img.save(path + "144Parameters.png")
    sleep(1)

def SOX144UK(path_order):
    #COUNTRY
    i=5
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\CO.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    sleep(0.5)
    pya.click((location[0]+w-45), (location[1]+h+20))
    pya.press("down")
    sleep(1)
    
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\order\\" + str(i+1) + ".PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #ORGANIZATION
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\ORG.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
        
    #boxINC
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\144\\CO+ORG\\orderOrg\\6.1.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    pya.click((location[0] + w/2), (location[1] + h + 10))
    
    
    clickNextToWhite(location)
    
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    SOX144setupDownload()
    getScreenshot144(path_order[i])
    viewReport()        
    saveFile()
    path_to = path_order[i]
    order = ["DE", "IT", "FR", "ES", "PT", "UK"]
    path_from = "C:\\Users\\R252202\\Downloads\\"
    file = "BBR-COM144V1.xlsx"
    moveAndRenameFile(path_from, file, path_to, order, i, start_date)       
############################################ REPORT 211 #######################

def searchFor211():
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\211.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    click(location, w, h)
    

def SOX211setup(path_order, i, order):
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\UNIT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\" + str(i+1) + ".PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    clickNextToWhite(location)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

    #PEROID
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Peroid.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickArrow(location, w, (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #DATE
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Date.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    sleep(0.5)
    clickArrow(location, (w-50), (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\SBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\IC.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    sleep(0.5)
    click(location, w, h)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #Customer SBU
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUall.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUinc.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    

def SOX211russia():
    #arrow
    sleep(1)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\UNIT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    pya.click((location[0]+w-50), (location[1]+(h/2)+100))
    pya.press("down")
    pya.press("down")
    
    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\RU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    clickNextToWhite(location)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

    #PEROID
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Peroid.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickArrow(location, w, (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #DATE
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Date.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    sleep(0.5)
    clickArrow(location, (w-50), (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\SBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\IC.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    sleep(0.5)
    click(location, w, h)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)   

def SOX211turkey():
        #arrow
    sleep(1)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\UNIT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\TR.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    clickNextToWhite(location)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

    #PEROID
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Peroid.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickArrow(location, w, (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #DATE
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Date.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    sleep(0.5)
    clickArrow(location, (w-50), (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #Customer SBU
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUall.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUinc.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
def SOX211ibericaIC():
    #arrow
    sleep(1)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\UNIT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    pya.click((location[0]+w-50), (location[1]+(h/2)+100))
    pya.press("down")

    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\ES.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\PT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5) 
    
    
    clickNextToWhite(location)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

    #PEROID
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Peroid.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickArrow(location, w, (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #DATE
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Date.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    sleep(0.5)
    clickArrow(location, (w-50), (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\SBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\IC.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    sleep(0.5)
    click(location, w, h)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #Customer SBU
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUall.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUinc.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

def SOX211ibericaIF():
    #arrow
    sleep(1)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\UNIT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    pya.click((location[0]+w-50), (location[1]+(h/2)+100))
    pya.press("down")

    #boxALL
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\ES.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5)
    
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\find\\PT.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    sleep(0.5)
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    sleep(0.5) 
    
    
    clickNextToWhite(location)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

    #PEROID
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Peroid.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    clickArrow(location, w, (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #DATE
     #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\Date.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    sleep(0.5)
    clickArrow(location, (w-50), (h+100))
    
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\SBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\IF.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    sleep(0.5)
    click(location, w, h)
        
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)
    
    #Customer SBU
    #SBu
    #arrow
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBU.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    
    location, w, h = findImageLocation09(scr, img_fav)
    clickArrow(location, w, h)
    
    #boxALL
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUall.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    
    sleep(0.5)
    img_fav = cv2.imread("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\211\\SETUP\\CSBUinc.PNG")
    img_fav = convertToGrey(img_fav)
    scr = getScreenshot()
    location, w, h = findImageLocation09(scr, img_fav)
    clickBox(location, w, h)
    clickNextToWhite(location)
    #LOADING
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\SETUP\\Loading2.PNG")
    sleep(1)

def getScreenshot211(path):
    img = ImageGrab.grab(bbox=(0, 210, 1500, 460))
    img.save(path + "211Parameters.png")
    sleep(1)
    
############################################# MAIN ############################

def main78(start_date, end_date):

        
    
    searchForFav()
    sleep(1)
    searchFor78()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
    sleep(1)
    SOX78setupDownload()
    
    
    path_order = ["g:\\Python projects\\My\\SOX downloader\\Reports\\1 Germany\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\2 Italy\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\3 Russia\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\4 UK\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\5 France\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\6 Iberica\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\7 Turkey\\"]
    
    order = ["DE", "IT", "RU", "UK", "FR", "IB", "TR"]
    i_order=0
    filename = "BBR-COM078V1.xlsx"
    path_from = "C:\\Users\\R252202\\Downloads\\"
    path_to = path_order[i_order]
    sleep(4)
    i_order = moveAndRenameFile(path_from, filename, path_to, order, i_order, start_date)
    
    loopOfDoom78(path_order, order, filename, path_from, start_date)

def main144(start_date, end_date):
    path_order = ["g:\\Python projects\\My\\SOX downloader\\Reports\\1 Germany\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\2 Italy\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\5 France\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\6 Iberica\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\6 Iberica\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\4 UK\\"]
    order = ["DE", "IT", "FR", "ES", "PT", "UK"]
    path_from = "C:\\Users\\R252202\\Downloads\\"
    file = "BBR-COM144V1.xlsx"
    for i in range(len(path_order)-1): #UK have scroll down
        if i == 0:
            i = 4
        print(path_order[i])
        searchForFav()
        sleep(4)
        searchFor144()
        sleep(1)
        checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
        sleep(1)
        SOX144countrySetupCountry(path_order, i, order)
        SOX144countrySetupOrg(path_order, i, order)
        SOX144setupDownload()
        getScreenshot144(path_order[i])
        viewReport()        
        saveFile()
        path_to = path_order[i]
        moveAndRenameFile(path_from, file, path_to, order, i, start_date)
    i=5
    searchForFav()
    sleep(3)
    searchFor144()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
    sleep(1)
    SOX144UK(path_order)
        
def main211(start_date, end_date):
    path_order = ["g:\\Python projects\\My\\SOX downloader\\Reports\\1 Germany\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\2 Italy\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\4 UK\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\5 France\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\3 Russia\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\7 Turkey\\",
                  "g:\\Python projects\\My\\SOX downloader\\Reports\\6 Iberica\\"]
    
    order = ["DE", "IT", "UK", "FR", "RU", "TR", "IB-IF", "IB-IC"]
    i=0
    file = "BBR-COM211BV1.xlsx"
    path_from = "C:\\Users\\R252202\\Downloads\\"
    for i in range(0,4):
        print(path_order[i])
        searchForFav()
        sleep(4)
        searchFor211()
        sleep(1)
        checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
        sleep(1)
        SOX211setup(path_order, i, order)
        getScreenshot211(path_order[i])
        viewReport()        
        saveFile()
        path_to = path_order[i]
        moveAndRenameFile(path_from, file, path_to, order, i, start_date)
    i=4
    #RUSSIA IBERICA AND TURKEY osobno
    print(path_order[i])
    searchForFav()
    sleep(4)
    searchFor211()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
    sleep(1)
    SOX211russia()
    getScreenshot211(path_order[i])
    viewReport()        
    saveFile()
    path_to = path_order[i]
    moveAndRenameFile(path_from, file, path_to, order, i, start_date)
    i+=1
    
    print(path_order[i])
    searchForFav()
    sleep(4)
    searchFor211()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
    sleep(1)
    SOX211turkey()
    getScreenshot211(path_order[i])
    viewReport()        
    saveFile()
    path_to = path_order[i]
    moveAndRenameFile(path_from, file, path_to, order, i, start_date)
    i+=1
    
    print(path_order[i])
    searchForFav()
    sleep(4)
    searchFor211()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
    sleep(1)
    SOX211ibericaIF()
    getScreenshot211(path_order[i])
    viewReport()        
    saveFile()
    path_to = path_order[i]
    moveAndRenameFile(path_from, file, path_to, order, i, start_date)
    
    print(path_order[i])
    searchForFav()
    sleep(4)
    searchFor211()
    sleep(1)
    checkForLoading("g:\\Python projects\\My\\SOX downloader\\Screenshots\\1\\78\\Loading.PNG")
    sleep(1)
    SOX211ibericaIC()
    getScreenshot211(path_order[i])
    viewReport()        
    saveFile()
    path_to = path_order[i]
    moveAndRenameFile(path_from, file, path_to, order, (i+1), start_date)

###############################################################################

#start_date = input("Provide startdate (format mm/dd/yyyy): ")
#end_date = input("Provide enddate (format mm/dd/yyyy): ")
start_date = "07/01/2021"
end_date = "07/31/2021"
main78(start_date, end_date)
main144(start_date, end_date)
main211(start_date, end_date)

#TODO LIST
