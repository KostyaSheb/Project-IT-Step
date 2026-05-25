import allure
import pytest
from playwright.sync_api import Page, expect

from locator_steam.games.games_locator import game_steam, add_game_basket, open_basket, basket, add_game_windrose
from locator_steam.main.locator_main import steam_search_game


@allure.feature("Магазин Steam")
@allure.story("Поиск игр (Playwright)")
def test_steam_search_playwright(page: Page):
    with allure.step("Открывается главная страница"):
        page.goto("https://store.steampowered.com")
    with allure.step("Поиск нужной игры в Steam"):
        search_game = "Portal 2"
        search_input = page.locator(steam_search_game)
        search_input.fill(search_game)
        search_input.press("Enter")
    with allure.step("Проверка на совпадении в названии"):
        first_result = page.locator(".search_result_row .title").first
        expect(first_result).to_contain_text(search_game)
        result_text = first_result.text_content()
        print(f"Тест пройден: Игра '{result_text}' найдена")

@allure.feature("Корзина Steam")
@allure.story("Добавление товара в корзину")
def test_steam_basket_playwright(page: Page):
    with allure.step("Открывается главная страница"):
        page.goto("https://store.steampowered.com")
    with allure.step("Поиск нужной игры в Steam"):
        search_game = "Windrose"
        search_input = page.locator(steam_search_game)
        search_input.fill(search_game)
        search_input.press("Enter")
    with allure.step("Добавление игры в корзину"):
        page.locator(game_steam).first.click()
        page.locator(add_game_windrose).click()
        page.locator(open_basket).click()
    with allure.step("Проверка, что нужный товар в корзине"):
        game_in_basket = page.locator(basket).first.text_content()
        assert search_game.lower() in game_in_basket.lower()
        print(f"Игра {search_game} в корзине")
