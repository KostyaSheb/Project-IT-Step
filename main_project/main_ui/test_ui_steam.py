import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locator_steam.games.games_locator import game_steam, add_game_basket, open_basket, basket, crimson_desert, \
    basket_for_delete, remove_button_crimson
from locator_steam.main.locator_main import steam_search_game, category_menu_new_games, store, store_charts


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature ("Магазин Steam")
@allure.story ("Поиск игр")
def test_steam_search(driver):
    with allure.step("Открывается главная страница"):
        driver.get("https://steampowered.com")
    with allure.step("Поиск нужной игры в Steam"):
        search_input = driver.find_element(By.XPATH, value=steam_search_game)
        search_game = "Portal 2"
        search_input.send_keys(search_game)
        search_input.send_keys(Keys.RETURN)
    with allure.step("Проверка на совпадении в названии"):
        first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".search_result_row .title"))
        )

        assert search_game in first_result.text
        print(f"Тест пройден: Игра '{first_result.text}' найдена!")

@allure.feature("Корзина Steam")
@allure.story("Добавление товара в корзину")
def test_steam_basket(driver):
    with allure.step("Открывается главная страница"):
        driver.get("https://steampowered.com")
    with allure.step("Поиск нужной игры в Steam"):
        search_game_steam = driver.find_element(By.XPATH, value=steam_search_game)
        search_game_basket = "Windrose"
        search_game_steam.send_keys(search_game_basket)
        search_game_steam.send_keys(Keys.RETURN)
    with allure.step("Добавление игры в корзину"):
        driver.find_element(By.XPATH, value=game_steam).click()
        driver.find_element(By.XPATH, value=add_game_basket).click()
        driver.find_element(By.XPATH, value=open_basket).click()
    with allure.step("Проверка, что нужный товар в корзине"):
        actual_game_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, basket))
        )
        WebDriverWait(driver, 5).until(lambda d: actual_game_element.text.strip() != "")
        game_in_basket = actual_game_element.text

        assert search_game_basket.lower() in game_in_basket.lower()
        print(f"Игра {search_game_basket} в корзине!")

@allure.feature("Корзина Steam")
@allure.story("Добавление товара в корзину и удаление")
def test_add_basket_and_delete_products(driver):
    with allure.step("Открывается главная страница"):
        driver.get("https://steampowered.com")
    with allure.step("Поиск нужной игры в Steam"):
        search_game_for_test_delete = driver.find_element(By.XPATH, value=steam_search_game)
        add_game_in_basket = "Crimson Desert"
        search_game_for_test_delete.send_keys(add_game_in_basket)
        search_game_for_test_delete.send_keys(Keys.RETURN)
    with allure.step("Добавление игры в корзину (Также проверка возраста)"):
        driver.find_element(By.XPATH, value=crimson_desert).click()
        driver.find_element(By.ID,"ageYear").send_keys("2000")
        driver.find_element(By.ID, "view_product_page_btn").click()
        driver.find_element(By.XPATH, value=add_game_basket).click()
        driver.find_element(By.XPATH, value=open_basket).click()
    with allure.step("Проверка, что нужный товар в корзине"):
        game_in_busket = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, basket_for_delete))
        )
        WebDriverWait(driver, 5).until(lambda d: game_in_busket.text.strip() != "")
        game_in_basket = game_in_busket.text

        assert add_game_in_basket.lower() in game_in_basket.lower()

        print(f"Игра {add_game_in_basket} сейчас в корзине и готова к удалению!")
    with allure.step("Удаление товара из корзины и проверка"):
        driver.find_element(By.XPATH, value=remove_button_crimson).click()
        product_delete = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, basket_for_delete))
        )
        assert product_delete
        print(f"Успешный тест. Игра {add_game_in_basket} удалена, после добавление в корзину")

@allure.feature("Чарты Steam")
@allure.story("Переход на Чарты")
def test_action_chains(driver):
    with allure.step("Открывается главная страница"):
        driver.get("https://steampowered.com")
    with allure.step("Наводим на вкладку магазин и находим Чарты"):
        menu_store = driver.find_element(By.XPATH, store)
        ActionChains(driver).move_to_element(menu_store).perform()
        driver.find_element(By.XPATH, store_charts).click()
    with allure.step("Переходим в чарты и проверяем"):
        charts_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        assert "ЧАРТЫ STEAM" in charts_header.text.upper()
        assert "charts" in driver.current_url
        print(f"Тест пройден! Мы на странице: {charts_header.text}")





