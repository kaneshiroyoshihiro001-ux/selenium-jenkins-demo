import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("url", [
    "https://example.com",
    "https://example.com",
    "https://example.com"
])
def test_open_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)

        # 等待页面标题出现
        page.wait_for_selector("h1")

        # 验证标题
        assert "Example Domain" in page.title()

        browser.close()
