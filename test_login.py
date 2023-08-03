import re

import pytest
from playwright.sync_api import Page, expect

from config import Config


@pytest.fixture()
def get_config():
    config = Config()
    config.url = "http://localhost:3000/login"
    return config


def test_successful_login(page: Page, get_config):
    url = get_config.url
    page.goto(url)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Login"))

    # data
    # create a locator
    get_username = page.locator("[id='name']")
    get_password = page.locator("[id='password']")

    # action
    get_username.fill("Willy")
    get_password.fill("password")
    page.get_by_role('button', name='Submit').click()

    # result
    expect(page).to_have_title(re.compile("Account"))
    expect(page.locator("[id='welcome-text']")).to_contain_text('Willy')


def test_wrong_password(page: Page, get_config):
    url = get_config.url
    page.goto(url)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Login"))

    # data
    # create a locator
    get_username = page.locator("[id='name']")
    get_password = page.locator("[id='password']")

    # action
    get_username.fill("Willy")
    get_password.fill("12345")
    page.get_by_role('button', name='Submit').click()

    # result
    expect(page).to_have_title(re.compile("Login"))
    assert page.wait_for_selector(".error-text").is_visible()


def test_forgot_password(page: Page, get_config):
    url = get_config.url
    page.goto(url)

    # data
    # create a locator
    get_reset_password = page.get_by_role('button', name='Forgot Password')

    # action
    get_reset_password.click()

    # result
    expect(page).to_have_title(re.compile("Forgot Password"))
    assert page.locator("[id='forgot-password']").is_visible()
