"""
A simple Python program for quickly dragging the screen up/down and searching for building pieces in a blank grid.

Author: David Chen
"""

import pyautogui
from time import sleep

SWIPE_DURATION = 0.2  # time (s) for swiping, increase this if you want more time to activate failsafe
SCREENSHOT_REGION = (0, 100, 1920, 800)  # region to check for yellow joints (left, top, width, height)
DEBUG = False  # if True, will save screenshot as polybridge.png (useful) to check if screenshot region is correct


def alt_tab():
    """ Switch to recent window """
    sleep(.5)
    pyautogui.keyDown('alt')
    sleep(.3)
    pyautogui.press('tab')
    sleep(.3)
    pyautogui.keyUp('alt')


def move_screen_up(num_moves):
    """ Drags downward to move the screen upward """
    pos_x = pyautogui.position()[0]
    for _ in range(num_moves):
        pyautogui.moveTo(pos_x, 100)
        pyautogui.drag(0, 800, duration=0.2)


def move_screen_down(num_moves):
    """ Drags upward to move the screen downard """
    pos_x = pyautogui.position()[0]
    for _ in range(num_moves):
        pyautogui.moveTo(pos_x, 900)
        pyautogui.drag(0, -800, duration=0.2)


def take_screenshot():
    """ Takes screenshot of the game without the bottom and top button bars """
    img = pyautogui.screenshot(region=SCREENSHOT_REGION)
    if DEBUG:
        img.save('polybridge.png')
    return img


def is_same_color(c1, c2):
    """ Returns True if rgb value differences are within threshold """
    return all(abs(c1[i] - c2[i]) < 20 for i in range(len(c1)))


def search_for_joints(img):
    """ Searches screenshot for yellow joints, meaning something is on the screen """
    yellow = (230, 213, 10)
    img.resize((960, 400))  # faster search
    pixels = set(list(img.getdata()))
    total = 0
    for i, pixel in enumerate(pixels):
        if is_same_color(pixel, yellow):
            total += 1
            if total > 3:  # if 3 yellow pixels, return True
                return True
    return False


def find_joints_above(num_moves):
    """ Keeps moving screen up until it finds a yellow joint, then it stops. Returns number of moves required. """
    for move in range(num_moves):
        move_screen_up()
        img = take_screenshot()
        if search_for_joints(img):
            return move
    return None


if __name__ == '__main__':
    alt_tab()
    sleep(1)

    move_screen_up(5)
    # move_screen_down()

    print(find_joints_above(300))  # swipe up 300 times max, print out number of swipes required
