from playwright.sync_api import Page

from models.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_text = page.locator("[id='forgot-password']")

    def is_welcome_text_displayed(self):
        return self.welcome_text.is_visible()