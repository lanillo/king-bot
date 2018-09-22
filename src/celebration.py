from .custom_driver import client, use_browser
from threading import Thread
import time
from .utils import log
from .util_game import close_modal


def celebration_thread(browser: client, village: [], celebration_type: int, interval: int) -> None:
    # init delay
    time.sleep(2)

    while True:
        remaining_time = start_celebration(browser, village, celebration_type)
        time.sleep(interval)


@use_browser
def start_celebration(browser: client, interval: int) -> bool:
    #log("adventure thread waking up")

    heroLinks = browser.find("//div[@class='heroLinks']")
    a = heroLinks.find_element_by_xpath(
        ".//a[contains(@class, 'adventureLink')]")
    browser.click(a, 2)
    el = browser.find("//div[@class='modalContent']")
    el = el.find_element_by_xpath(
        ".//button")

    classes = el.get_attribute("class").split(" ")
    available = True

    for c in classes:
        if c == "disabled":
            available = False
            break

    if available:
        browser.click(el, 2)
        log("adventure started")

    close_modal(browser)
    return available
    #log("adventure thread sleeping")

