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
