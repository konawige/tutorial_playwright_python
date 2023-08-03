# -- FILE: features/environment.py
import asyncio

from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright

@fixture
async def browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    # webkit = sync_playwright().start().webkit
    # browser = webkit.launch(headless=False)
    # playwright_context = browser.new_context()
    # context.page = playwright_context.new_page()
    # yield context.page
    # # -- CLEANUP-FIXTURE PART:
    # context.page.close()

    p = await async_playwright().start()
    browser = await p.webkit.launch(headless=False)
    context.page = await browser.new_page()
    return context.page
    # await browser.close()


@async_run_until_complete
async def before_scenario(context, scenario):
    await use_fixture(browser_chrome, context)


# def after_scenario(context, scenario):
#     context.page.close()
