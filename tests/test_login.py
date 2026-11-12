from playwright.sync_api import Playwright, Page, expect

def test_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    input_username = page.get_by_label("username")
    input_username.fill("tomsmith")
    input_password = page.get_by_label("password")
    input_password.fill("SuperSecretPassword!")
    login = page.locator("button[type='submit']").click()
    page.wait_for_timeout(4000)
    result = page.get_by_text(
    "Welcome to the Secure Area. When you are done click logout below."
)

    expect(result).to_contain_text(
    "Welcome to the Secure Area. When you are done click logout below."
)