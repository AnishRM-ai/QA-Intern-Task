import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from utils.mailosaur_cllient import MailsaurHelper

load_dotenv()

@pytest.fixture(scope="session")
def mailosaur():
    return MailsaurHelper()

@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
        
@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

    