import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import RegisterLocators, Avtorization, PasswordRecovery


class MainPage(BasePage):
    def register_button(self):
        register_button = self.browser.find_element(*RegisterLocators.REGISTER)
        register_button.click()

    def registration_new_user(self):
        first_name = self.browser.find_element(*RegisterLocators.FIRST_NAME)
        first_name.send_keys('Лиза')
        last_name = self.browser.find_element(*RegisterLocators.LAST_NAME)
        last_name.send_keys('Капустина')
        email_phone = self.browser.find_element(*RegisterLocators.EMAIL_PHONE)
        email_phone.send_keys('liz.liz@mail.ru')
        password = self.browser.find_element(*RegisterLocators.PASSWORD)
        password.send_keys('Liza123456789')
        password_confirm = self.browser.find_element(*RegisterLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys('Liza123456789')
        self.browser.find_element(*RegisterLocators.BUTTON_REGISTRATION).click()

    def change_email_registration_new_user(self):
        button_change_email = self.browser.find_element(*RegisterLocators.CHANGE_EMAIL)
        button_change_email.click()

    def registration_new_user_by_registered_email(self):
        first_name = self.browser.find_element(*RegisterLocators.FIRST_NAME)
        first_name.send_keys('Лиза')
        last_name = self.browser.find_element(*RegisterLocators.LAST_NAME)
        last_name.send_keys('Лиза')
        email_phone = self.browser.find_element(*RegisterLocators.EMAIL_PHONE)
        email_phone.send_keys('liz.fedulova@mail.ru')
        password = self.browser.find_element(*RegisterLocators.PASSWORD)
        password.send_keys('Osa123456789')
        password_confirm = self.browser.find_element(*RegisterLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys('Osa123456789')
        self.browser.find_element(*RegisterLocators.BUTTON_REGISTRATION).click()

    def avtorization_email(self):
        email_tab = self.browser.find_element(*Avtorization.EMAIL_TAB)
        email_tab.click()
        email = self.browser.find_element(*Avtorization.EMAIL_PHONE)
        email.send_keys('liz.fedulova@mail.ru')
        password = self.browser.find_element(*Avtorization.PASSWORD)
        password.send_keys('Liz"123456789')
        login_button = self.browser.find_element(*Avtorization.LOGIN_BUTTON)
        login_button.click()

    def close_avtorization(self):
        logout = self.browser.find_element(*Avtorization.LOGOUT_BUTTON)
        logout.click()

    def avtorization_phone(self):
        phone_tab = self.browser.find_element(*Avtorization.PHONE_TAB)
        phone_tab.click()
        phone = self.browser.find_element(*Avtorization.EMAIL_PHONE)
        phone.send_keys('+79616405241')
        password = self.browser.find_element(*Avtorization.PASSWORD)
        password.send_keys('Liz"123456789')
        login_button = self.browser.find_element(*Avtorization.LOGIN_BUTTON)
        login_button.click()

    def avtorization_login(self):
        login_tab = self.browser.find_element(*Avtorization.LOGIN_TAB)
        login_tab.click()
        login = self.browser.find_element(*Avtorization.LOGIN)
        login.send_keys('rtkid_1680855761698')
        password = self.browser.find_element(*Avtorization.PASSWORD)
        password.send_keys('Liz"123456789')
        login_button = self.browser.find_element(*Avtorization.LOGIN_BUTTON)
        login_button.click()

    def avtorization_vk(self):
        vk = self.browser.find_element(*Avtorization.VK)
        vk.click()

    def avtorization_ok(self):
        ok = self.browser.find_element(*Avtorization.OK)
        ok.click()

    def avtorization_mail_ru(self):
        mail_ru = self.browser.find_element(*Avtorization.MAIL_RU)
        mail_ru.click()

    def avtorization_google(self):
        google = self.browser.find_element(*Avtorization.GOOGLE)
        google.click()

    def avtorization_yandex(self):
        yandex = self.browser.find_element(*Avtorization.YANDEX)
        yandex.click()
        yandex = self.browser.find_element(*Avtorization.YANDEX)
        yandex.click()

    def password_recovery_by_mail(self):
        email_tab = self.browser.find_element(*Avtorization.EMAIL_TAB)
        email_tab.click()
        forgot_password = self.browser.find_element(*PasswordRecovery.FORGOT_PASSWORD)
        forgot_password.click()

    def password_recovery_by_phone(self):
        phone_tab = self.browser.find_element(*Avtorization.PHONE_TAB)
        phone_tab.click()
        forgot_password = self.browser.find_element(*PasswordRecovery.FORGOT_PASSWORD)
        forgot_password.click()

    def password_recovery_by_login(self):
        login_tab = self.browser.find_element(*Avtorization.LOGIN_TAB)
        login_tab.click()
        forgot_password = self.browser.find_element(*PasswordRecovery.FORGOT_PASSWORD)
        forgot_password.click()

    def work_button_beak_password_recovery(self):
        login_tab = self.browser.find_element(*Avtorization.LOGIN_TAB)
        login_tab.click()
        forgot_password = self.browser.find_element(*PasswordRecovery.FORGOT_PASSWORD)
        forgot_password.click()
        button_beak = self.browser.find_element(*PasswordRecovery.BUTTON_BEAK)
        button_beak.click()






