from selenium.webdriver.common.by import By

class RegisterLocators:
    REGISTER = (By.CSS_SELECTOR, '#kc-register')
    TITLE = (By.CSS_SELECTOR, 'h1.card-container__title')
    FIRST_NAME =(By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastName"]')
    EMAIL_PHONE = (By.CSS_SELECTOR, '#address')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#password-confirm')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button.rt-btn.rt-btn--orange.rt-btn--medium.rt-btn--rounded.register-form__reg-btn')
    CHANGE_EMAIL = (By.CSS_SELECTOR, 'button[name="otp_back_phone"]')
    ALLERT_TITLE = (By.CSS_SELECTOR, 'h2.card-modal__title')

class Avtorization:
    EMAIL_TAB = (By.CSS_SELECTOR, 'div[id=t-btn-tab-mail]')
    EMAIL_PHONE = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[id="kc-login"]')
    PHONE_TAB = (By.CSS_SELECTOR, '#t-btn-tab-phone')
    PERSONAL_ACCOUNT_TITLE = (By.CSS_SELECTOR, 'h3.card-title')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout-btn')
    LOGIN_TAB = (By.CSS_SELECTOR, '#t-btn-tab-login')
    LOGIN = (By.CSS_SELECTOR, '#username')
    VK = (By.CSS_SELECTOR, '#oidc_vk')
    OK = (By.CSS_SELECTOR, '#oidc_ok')
    MAIL_RU = (By.CSS_SELECTOR, '#oidc_mail')
    GOOGLE = (By.CSS_SELECTOR, '#oidc_google')
    YANDEX = (By.CSS_SELECTOR, '#oidc_ya')

class PasswordRecovery:
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '#forgot_password')
    BUTTON_BEAK = (By.CSS_SELECTOR, '#reset-back')








