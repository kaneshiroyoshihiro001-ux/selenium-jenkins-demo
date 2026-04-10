import pytest
from playwright.sync_api import Page, sync_playwright


class GooglePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        self.page.goto("https://www.google.com")

    def search(self, keyword: str) -> None:
        self.page.fill('textarea[name="q"]', keyword)
        self.page.press('textarea[name="q"]', "Enter")

    def has_keyword(self, keyword: str) -> bool:
        return keyword.lower() in self.page.content().lower()


@pytest.mark.parametrize("keyword", [
    "playwright",
    "python",
    "automation",
])
def test_google_search(keyword: str) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        google_page = GooglePage(page)
        google_page.open()
        google_page.search(keyword)

        page.wait_for_timeout(3000)

        assert google_page.has_keyword(keyword)

        browser.close()