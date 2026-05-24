import requests
import pytest
import allure



@allure.feature("Steam API")
@allure.story("Информация об игре Cities: Skylines II")
def test_get_cities_skylines():
    app_id = "949230"
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    with allure.step(f"Отправляем GET-запрос на Steam API для ID: {app_id}"):
        response = requests.get(url, headers=headers)
    with allure.step("Получаем статус код. Нужен 200"):
        assert response.status_code == 200
    data = response.json()
    print(data.keys())
    print(data[app_id].keys())
    with allure.step("Валидация данных об игре"):
        assert data[app_id]["success"] is True
        game_date = data[app_id]["data"]
        assert game_date["name"] == "Cities: Skylines II"
        assert game_date["type"] == "game"
        assert "builder" in game_date["short_description"].lower()


@allure.feature("Steam API")
@allure.story("Проверка цены Cities: Skylines II")
def test_check_price_game():
    app_id = "949230"
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    with allure.step(f"Отправляем GET-запрос на Steam API для ID: {app_id}"):
        response = requests.get(url, headers=headers)
    with allure.step("Получаем статус код. Нужен 200"):
        assert response.status_code == 200
    data = response.json()
    with allure.step("Валидация данных об игре"):
        assert data[app_id]["success"] is True
        game_date = data[app_id]["data"]
    with allure.step("Проверка логики: платная игра должна иметь блок цены"):
        assert game_date["is_free"] is False
        assert "price_overview" in game_date
        price_info = game_date["price_overview"]
        assert price_info["currency"] == "USD"
        assert price_info["final"] > 0
        print(f"Цена игры {game_date['name']}: {price_info['final_formatted']}")

@allure.feature("Steam API")
@allure.story("Проверка тега Cities: Skylines II")
def test_check_news_game():
    app_id = "949230"
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    with allure.step(f"Отправляем GET-запрос на Steam API для ID: {app_id}"):
        response = requests.get(url, headers=headers)
    with allure.step("Получаем статус код. Нужен 200"):
        assert response.status_code == 200
    data = response.json()
    with allure.step("Проверка, что есть тег Креатив"):
        game_date = data[app_id]["data"]
        assert "creativity" in game_date["short_description"].lower()
        print(f"Категория проверена")

@allure.feature("Steam API")
@allure.story("Проверка даты выхода Cities: Skylines II")
def test_check_release_date():
    app_id = "949230"
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    with allure.step("Запрос даты релиза"):
        response = requests.get(url, headers=headers)
        data = response.json()

    with allure.step("Проверка года выпуска"):
        release_info = data[app_id]["data"]["release_date"]
        assert release_info["coming_soon"] is False
        assert "2023" in release_info["date"]
        print(f"Дата релиза Cities: Skylines II подтверждена: {release_info['date']}")

@allure.feature("Steam API")
@allure.story("Проверка скриншотов Cities: Skylines II")
def test_check_game_screenshots():
    app_id = "949230"
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    with allure.step("Запрос медиа данных"):
        response = requests.get(url, headers=headers)
        data = response.json()

    with allure.step("Проверка на скриншоты"):
        screenshots = data[app_id]["data"]["screenshots"]
        assert len(screenshots) > 0
        print(f"Скриншоты присутствуют")