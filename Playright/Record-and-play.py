import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.goto("https://www.saucedemo.com/v1/")
    page.pause()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()
    expect(page.locator("#inventory_filter_container")).to_contain_text("Products")
    expect(page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button")).to_be_visible()
    page.get_by_text("carry.allTheThings() with the").click()

    # ---------------------
    context.close()
    browser.close()
print(1234)

print(21)