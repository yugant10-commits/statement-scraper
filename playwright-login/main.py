from playwright.sync_api import sync_playwright

username = input("Enter your username: ")
password = input("Enter your password: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto("https://banksmartxp.siddharthabank.com/")
    page.fill('input#nd-input-1',username)
    page.fill('input#nd-input-0',password)
    page.click('button[type=submit]')
