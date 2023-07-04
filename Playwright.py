from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    page.get_by_placeholder("Искать в Википедии").click()
    page.get_by_placeholder("Искать в Википедии").fill("Тестирование")
    page.get_by_role("button", name="Перейти").click()
    page.get_by_role("link", name="Тестирование программного обеспечения").click()
    page.get_by_text("Интеграционное тестирование — тестируются интерфейсы между компонентами, подсист").click()
    page.get_by_text("Описанные ниже техники — тестирование белого ящика и тестирование чёрного ящика ").click()
    page.locator("b").filter(has_text="Регрессионное тестирование").get_by_role("link", name="Регрессионное тестирование").click()
    page.get_by_role("link", name="Автоматизированное тестирование").click()
    page.get_by_role("link", name="Selenium", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
