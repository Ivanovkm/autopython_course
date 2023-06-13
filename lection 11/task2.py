# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

message_text = 'Привет'
sender_name = 'Иванов Кирилл'
send_date = None
send_date_str = ''


# Не придумал другого способа как искать в аккордеоне нужный пункт
def menu_item_finder(elements_list, text):
    for i in range(len(elements_list)):
        if elements_list[i].text == text:
            return elements_list[i]
        else:
            assert False, 'Не нашли элемент меню с нужным текстом'


site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
driver.get(site)
time.sleep(1)
assert driver.current_url == 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/', 'Неправильный адрес сайта'

log_field = driver.find_element(By.NAME, 'Login')
assert log_field.is_displayed(), 'Не отображается поле ввода логина'
log_field.send_keys('Рекламашки')
time.sleep(1)

auth_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa=auth-AdaptiveLoginForm__checkSignInTypeButton]')
assert auth_btn.is_displayed(), 'Не отображается кнопка -> на форме логина'
auth_btn.click()

pass_field = driver.find_element(By.CSS_SELECTOR, '[type=password]')
assert pass_field.is_displayed(), 'Не отображается поле "Пароль"'
pass_field.send_keys('123qwerty')

auth_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa=auth-AdaptiveLoginForm__signInButton]')
assert auth_btn.is_displayed(), 'Не отображается кнопка аутентификации'
auth_btn.click()
time.sleep(2)

accordion = driver.find_elements(By.CSS_SELECTOR, '[data-qa=NavigationPanels-Accordion__title]')
menu_item = menu_item_finder(accordion, 'Контакты')
assert menu_item.is_displayed(), 'Пункт аккордеона "Контакты" не отображается'
menu_item.click()
time.sleep(1)

menu_item = driver.find_element(By.CLASS_NAME, 'NavigationPanels-SubMenu__headTitle')
assert menu_item.is_displayed(), 'Подменю аккордеона "Контакты" не отображается'
menu_item.click()
time.sleep(1)

add_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
assert add_btn.is_displayed(), 'Кнопка "+" для добавления сообщения не отображается'
add_btn.click()
time.sleep(2)

find_input = driver.find_element(By.CSS_SELECTOR,
                                 '[data-qa="addressee-selector-root"] [data-qa="controls-Render__field"]')
assert find_input.is_displayed(), 'Не отображается строка поиска'
find_input.click()
find_input.send_keys(sender_name)
time.sleep(1)

person = driver.find_element(By.CSS_SELECTOR,
                             '[data-qa="addressee-selector-root"] [class="msg-person-selector__item"] '
                             'span[title="Иванов Кирилл"]')
assert person.text == sender_name, f'Не нашли сотрудника {sender_name}'
assert person.is_displayed()
person.click()
time.sleep(2)

text_editor = driver.find_element(By.CSS_SELECTOR, '[data-qa=textEditor_slate_Field]')
assert text_editor.is_displayed(), 'Не отображается поле ввода сообщения'
text_editor.click()
text_editor.send_keys(message_text)
time.sleep(1)

send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
assert send_btn.is_displayed(), 'Не отображается кнопка отправки сообщения'
send_btn.click()
send_date = datetime.datetime.now()

time.sleep(1)
message_title = driver.find_element(By.CSS_SELECTOR,
                                    f'div[name="readDateTarget"] [data-qa="item"] [title="{sender_name}"]')
assert message_title.text == sender_name, 'Не нашли сообщение от нужного отправителя'
msg_text = driver.find_element(By.CSS_SELECTOR, 'div[name="readDateTarget"] [data-qa="item"] p')
assert msg_text.text == message_text, 'Текст сообщения неправильный'

msg_date = driver.find_element(By.CSS_SELECTOR,
                               'div[name="readDateTarget"] [data-qa="item"] [data-qa="msg-entity-date"]')
# Я проверяю тут время, но я не знаю как надежно синхронизировать
# время на тачке автотестирования с сервером сообщений
# У меня из-за разницы с локальной машиной тест падает
send_date_str += msg_date.text[0:2] + ' ' + msg_date.text[7:12]
assert send_date_str == send_date.strftime(
    '%d %H:%M'), f'Ошибка при сравнении времении сообщения, ожидали {send_date_str}, ' \
                 f'получили {send_date.strftime("%d %H:%M")}'

driver.quit()
