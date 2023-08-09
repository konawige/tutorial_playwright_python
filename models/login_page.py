from playwright.sync_api import Page

from models.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("[id='name']")
        self.password = page.locator("[id='password']")
        self.submit = page.get_by_role('button', name='Submit')
        self.reset_password = page.get_by_role('button', name='Forgot Password')

    def navigate(self, url):
        self.page.goto(url, timeout=5000)

    def fill_username(self, text):
        self.username.fill(text)

    def fill_password(self, text):
        self.password.fill(text)

    def submit_login(self):
        self.submit.click()

    def click_button(self, action):
        if action == "submit":
            self.submit_login()
        elif action == "forgot password":
            self.reset_password.click()
            self.page.wait_for_url('**/forgot-password', timeout=2000)

    def is_error_message_displayed(self):
        return self.page.wait_for_selector(".error-text", state="visible", timeout=5000)
