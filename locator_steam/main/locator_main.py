#Основные кнопки переходящие на другую страницу

store = "//div[@id='global_header']//a[contains(@class, 'menuitem') and contains(text(), 'МАГАЗИН')]"
store_charts = '(//*[@data-submenuid="Store"])[2]/*[6]'
btn_home = '//*[@alt="Ссылка на домашнюю страницу Steam"]'
btn_enter = "//*[@aria-label='Меню аккаунта']/*[2]"
btn_community = '(//*[@data-tooltip-content=".submenu_Community"])[2]'
btn_about_steam = '//*[@aria-label="Глобальное меню"]/*[3]'
btn_support = '//*[@aria-label="Глобальное меню"]/*[4]'

#Поле ввода поиска игр
steam_search_game = '//*[@aria-autocomplete="list"]'

#Кнопка переходящая на страничку поиска игр
btn_button_search = '(//*[@aria-label="Меню магазина"]//button)[6]'

#Под кнопки на main странице (не переходят на другие страницы)
btn_view_games = "//button[.//div[text()='Просмотр']]"
btn_recommendation_games = '(//*[@aria-expanded="false"])[2]/*[1]'
btn_category_games = '(//*[@aria-expanded="false"])[3]/*[1]'
btn_ways_to_play = '(//*[@aria-expanded="false"])[4]/*[1]'
btn_special_sections = '//*[@aria-expanded="true"]/*[1]'
btn_change_language = '//*[@id="language_pulldown"]'
category_menu_new_games = '(//*[@role="button"])[5]/*[1]'

btn_skip_game = "(//*[contains(concat(' ', normalize-space(@class), ' '), ' right ')])[1]"