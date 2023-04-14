from selenium import webdriver


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
