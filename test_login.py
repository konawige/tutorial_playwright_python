import re

import pytest
from playwright.sync_api import Page

from models.account_page import AccountPage
from models.login_page import LoginPage
from models.reset_password_page import ResetPasswordPage


@pytest.fixture()
def login_url(base_url):
    return base_url + "/login"


def test_successful_login(page: Page, login_url):
    login_page = LoginPage(page)
    login_page.navigate(login_url)

    # Expect a title "to contain" a substring.
    assert login_page.is_title_contains("Login")

    #action
    login_page.fill_username("Willy")
    login_page.fill_password("password")
    login_page.submit_login()

    #result
    account_page = AccountPage(page)
    assert account_page.is_title_contains("Account")
    assert account_page.is_welcome_text_contains('Willy')


def test_wrong_password(page: Page, login_url):
    login_page = LoginPage(page)
    login_page.navigate(login_url)

    # Expect a title "to contain" a substring.
    assert login_page.is_title_contains("Login")

    # action
    login_page.fill_username("Willy")
    login_page.fill_password("12345")
    login_page.submit_login()

    # result
    assert login_page.is_title_contains("Login")
    assert login_page.is_error_message_displayed()


def test_forgot_password(page: Page, login_url):
    login_page = LoginPage(page)
    login_page.navigate(login_url)

    # action
    login_page.click_button("forgot password")

    # result
    reset_password_page = ResetPasswordPage(page)
    assert reset_password_page.is_title_contains("Forgot Password")
    assert reset_password_page.is_welcome_text_displayed()


