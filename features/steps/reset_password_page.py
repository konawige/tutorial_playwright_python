from behave import then
from behave.api.async_step import async_run_until_complete

from models.account import AccountPage
from models.reset_password import ResetPasswordPage


@then("the text message on reset password page is visible")
@async_run_until_complete
async def is_reset_welcome_text_displayed(context):
    """
    :type context: behave.runner.Context
    """
    reset_pwd_page = ResetPasswordPage(context.page)
    assert await reset_pwd_page.welcome_text.is_visible()