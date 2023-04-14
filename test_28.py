import pytest

from pythonProject1.module_28.pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from pythonProject1.module_28.pages.locators import RegisterLocators, Avtorization, PasswordRecovery
from pythonProject1.module_28.pages.conftest import browser

max_text_256 = '!=2$%д"+*ф@@s.j)' * 16
min_text = 'L'


class TestRT:
    @pytest.mark.positive
    def test_click_register(self, browser):
        """ Переход на форму регистрации нового пользователя """
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.register_button()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Регистрация'

    @pytest.mark.positive
    def test_registration_new_user_positive(self, browser):
        """Регистрация нового пользователя (позитивный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.register_button()
        page.registration_new_user()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Подтверждение email'

    @pytest.mark.positive
    def test_registration_new_user_positive_change_email_positive(self, browser):
        """Изменение e-mail при регистрации пользователя"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.register_button()
        page.registration_new_user()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Подтверждение email'
        page.change_email_registration_new_user()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Регистрация'

    @pytest.mark.negative
    def test_registration_new_user_by_registered_email(self, browser):
        """Регистрация пользователя по зарегистрированному email"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.register_button()
        page.registration_new_user_by_registered_email()
        assert browser.find_element(*RegisterLocators.ALLERT_TITLE).text == 'Учётная запись уже существует'

    @pytest.mark.negative
    @pytest.mark.parametrize('first_name', ['', 'Liza', max_text_256, min_text])
    @pytest.mark.parametrize('last_name', ['', 'Liza', max_text_256, min_text])
    @pytest.mark.parametrize('password', ['', 'Liza', max_text_256, min_text, 'liza123456789'])
    def test_registration_new_user_negative(self, browser, first_name, last_name, password):
        """Регистрация нового пользователя (негативный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.register_button()
        first_name_av = browser.find_element(*RegisterLocators.FIRST_NAME)
        first_name_av.send_keys(first_name)
        last_name_av = browser.find_element(*RegisterLocators.LAST_NAME)
        last_name_av.send_keys(last_name)
        email_phone = browser.find_element(*RegisterLocators.EMAIL_PHONE)
        email_phone.send_keys('liz.liz@mail.ru')
        password_av = browser.find_element(*RegisterLocators.PASSWORD)
        password_av.send_keys(password)
        password_confirm = browser.find_element(*RegisterLocators.PASSWORD_CONFIRM)
        password_confirm.send_keys(password)
        browser.find_element(*RegisterLocators.BUTTON_REGISTRATION).click()
        assert browser.find_element(By.CSS_SELECTOR, 'span.rt-input-container__meta.rt-input-container__meta--error')
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Регистрация'

    @pytest.mark.positive
    def test_user_authorization_email_positive(self, browser):
        """Вход в личный кабинет по e-mail (позитивный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_email()
        assert browser.find_element(*Avtorization.PERSONAL_ACCOUNT_TITLE).text == 'Учетные данные'
        page.close_avtorization()

    @pytest.mark.negative
    @pytest.mark.parametrize('email', ['', 'liz.fedulova.ru', max_text_256, min_text, '123456789'],
                             ids=['Пустая строка', 'Невалидный email', 'Ввод 256 символов', 'Ввод 1 символа', 'Ввод числовых данных'])
    def test_user_authorization_email_negative(self, browser, email):
        """Вход в личный кабинет по e-mail (негативный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        email_tab = browser.find_element(*Avtorization.EMAIL_TAB)
        email_tab.click()
        email_av = browser.find_element(*Avtorization.EMAIL_PHONE)
        email_av.send_keys(email)
        password = browser.find_element(*Avtorization.PASSWORD)
        password.send_keys('Liz"123456789')
        login_button = browser.find_element(*Avtorization.LOGIN_BUTTON)
        login_button.click()
        assert browser.find_element(*RegisterLocators.TITLE).text != 'Учетные данные'

    @pytest.mark.positive
    def test_user_authorization_phone_positive(self, browser):
        """Вход в личный кабинет по номеру телефона (позитивный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_phone()
        assert browser.find_element(*Avtorization.PERSONAL_ACCOUNT_TITLE).text == 'Учетные данные'
        page.close_avtorization()

    @pytest.mark.negative
    @pytest.mark.parametrize('phone', ['', '88888', max_text_256, min_text, 'dhgahdghadgj'],
                             ids=['Пустая строка', 'Невалидный номер телефона', 'Ввод 256 символов', 'Ввод 1 символа',
                                  'Ввод строковых данных'])
    def test_user_authorization_phone_negative(self, browser, phone):
        """Вход в личный кабинет по номеру телефона (негативный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        phone_tab = browser.find_element(*Avtorization.PHONE_TAB)
        phone_tab.click()
        phone_av = browser.find_element(*Avtorization.EMAIL_PHONE)
        phone_av.send_keys(phone)
        password = browser.find_element(*Avtorization.PASSWORD)
        password.send_keys('Liz"123456789')
        login_button = browser.find_element(*Avtorization.LOGIN_BUTTON)
        login_button.click()
        assert browser.find_element(*RegisterLocators.TITLE).text != 'Учетные данные'

    @pytest.mark.positive
    def test_user_authorization_login_positive(self, browser):
        """Вход в личный кабинет по логину (позитивный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_login()
        assert browser.find_element(*Avtorization.PERSONAL_ACCOUNT_TITLE).text == 'Учетные данные'
        page.close_avtorization()

    @pytest.mark.negative
    @pytest.mark.parametrize('login', ['', '1680855761698', max_text_256, min_text],
                             ids=['Пустая строка', 'Некорректный логин', 'Ввод 256 символов', 'Ввод одного символа'])
    def test_user_authorization_login_negative(self, browser, login):
        """Вход в личный кабинет по логину (негативный тест-кейс)"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        login_tab = browser.find_element(*Avtorization.LOGIN_TAB)
        login_tab.click()
        login_av = browser.find_element(*Avtorization.LOGIN)
        login_av.send_keys(login)
        password = browser.find_element(*Avtorization.PASSWORD)
        password.send_keys('Liz"123456789')
        login_button = browser.find_element(*Avtorization.LOGIN_BUTTON)
        login_button.click()
        assert browser.find_element(*RegisterLocators.TITLE).text != 'Учетные данные'

    @pytest.mark.positive
    def test_user_authorization_vk(self, browser):
        """Вход в личный кабинет с помощью аккаунта социальной сети 'ВКонтакте'"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_vk()
        assert browser.find_element(By.CSS_SELECTOR, 'div.box_msg_gray.box_msg_padded b').text == 'ВКонтакте'

    @pytest.mark.positive
    def test_user_authorization_ok(self, browser):
        """Вход в личный кабинет с помощью аккаунта социальной сети 'Одноклассники'"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_ok()
        assert browser.find_element(By.CSS_SELECTOR, 'div.ext-widget_h_tx').text == 'Одноклассники'

    @pytest.mark.positive
    def test_user_authorization_mail_ru(self, browser):
        """Вход в личный кабинет с помощью аккаунта 'Mail.ru'"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_mail_ru()
        assert browser.find_element(By.CSS_SELECTOR, 'span.header__logo').text == 'Мой Мир@Mail.Ru'

    @pytest.mark.positive
    def test_user_authorization_google(self, browser):
        """Вход в личный кабинет с помощью аккаунта 'Google.com'"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_google()
        assert browser.find_element(By.CSS_SELECTOR, 'div.kHn9Lb').text == 'Войдите в аккаунт Google'

    @pytest.mark.positive
    def test_user_authorization_yandex(self, browser):
        """Вход в личный кабинет с помощью аккаунта 'Yandex.ru'"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.avtorization_yandex()
        assert browser.find_element(By.CSS_SELECTOR, 'a[href="https://ya.ru"]')

    @pytest.mark.positive
    def test_password_recovery_by_mail(self, browser):
        """Переход на страницу восстановления пароля по e-mail """
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.password_recovery_by_mail()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Восстановление пароля'

    @pytest.mark.positive
    def test_password_recovery_by_phone(self, browser):
        """Переход на страницу восстановления пароля по номеру телефона"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.password_recovery_by_phone()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Восстановление пароля'

    @pytest.mark.positive
    def test_password_recovery_by_login(self, browser):
        """Переход на страницу восстановления пароля по логину"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.password_recovery_by_login()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Восстановление пароля'

    @pytest.mark.positive
    def test_work_button_beak_password_recovery(self, browser):
        """Работа кнопки "Вернуться назад" при восстановлении пароля"""
        url = 'https://b2c.passport.rt.ru'
        page = MainPage(browser, url)
        page.open()
        page.work_button_beak_password_recovery()
        assert browser.find_element(*RegisterLocators.TITLE).text == 'Авторизация'







