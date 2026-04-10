import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("keyword", [
    "playwright",
    "python",
    "automation"
])
def test_google_search(keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.google.com")

        page.fill('textarea[name="q"]', keyword)
        page.press('textarea[name="q"]', "Enter")

        # ⭐ 等待搜索结果元素出现（关键）
        page.wait_for_selector("text=" + keyword, timeout=10000)

        assert keyword in page.content().lower()

        browser.close()
