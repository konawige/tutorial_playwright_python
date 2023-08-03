from playwright.sync_api import Page

from models.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_text = page.locator("[id='forgot-password']")

