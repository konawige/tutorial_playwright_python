from playwright.sync_api import Page

from models.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_text = page.locator("[id='welcome-text']")

    def is_welcome_text_contains(self, value):
        content = self.welcome_text.text_content()
        if content.find(value) == -1:
            return False
        else:
            return True