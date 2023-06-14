# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://sbis.ru')
time.sleep(1)
assert driver.current_url == 'https://sbis.ru/', 'Неправильный адрес страницы sbis.ru'

contacts_btn = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
assert contacts_btn.is_displayed(), 'Кнопка "Контакты" не отображается'
contacts_btn.click()
time.sleep(1)
url = driver.current_url[0:24]
assert url == 'https://sbis.ru/contacts', 'Не открылся раздел "Контакты"'
time.sleep(1)
tensor_logo = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
tensor_logo.is_displayed(), 'Не отображается лого тензора'
tensor_logo.click()
time.sleep(1)

handles = driver.window_handles
driver.switch_to.window(handles[1])


assert driver.current_url == 'https://tensor.ru/', "Не открылась страница tensor.ru"
people_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
assert people_block.is_displayed(), "Не отображается блок 'Сила в людях'"
about_people = driver.find_element(By.CSS_SELECTOR,
                                   'div>p>[href="/about"]')
about_people.location_once_scrolled_into_view
assert about_people.is_displayed(), 'Не отображается кнопка "Подробнее"'
about_people.click()
assert driver.current_url == 'https://tensor.ru/about', "Не открылась страница Тензор - о Компании"
time.sleep(5)

driver.quit()
