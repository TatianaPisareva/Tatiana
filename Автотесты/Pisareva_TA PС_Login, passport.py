import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть сайт и залогинеться
s = Service('/users/Test/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
#максимальное окно
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
#login
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("tatianaapisareva@gmail.com")
#password
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)
# Открыть форму Паспорт
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
# Очистка полей, установка курсора в начало бокса и заполнение по объему
def fill_field(name, value):
    driver.find_element(By.ID, name).clear()
    driver.find_element(By.ID, name).send_keys(Keys.HOME)
    driver.find_element(By.ID, name).send_keys(value)
# Заполнение формы Паспорт. ФИО
driver.find_element(By.ID, "surname").send_keys("Пупкин")
driver.find_element(By.ID, "name").send_keys("Василий")
driver.find_element(By.ID, "patronymic").send_keys("Владимирович")
# Дата рождения
driver.find_element(By.XPATH, "//*[@id='birthday']/div/input").send_keys("15.03.1990")
# Серия и номер паспорта
fill_field("passportSeries", "1358")
fill_field("passportNumber", "987654")
# Дата выдачи
driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").send_keys("14.04.2022")
# Код подразделения
fill_field("code", "654321")
fill_field("issued", "ОВД МР Замоскворечье по гор. Москве")
# СНИЛС
fill_field("cardId", "01234567890")
# Кем выдан
fill_field("issued", "ОУФМС России по УР")
# перемещение по странице
driver.execute_script("window.scrollTo(0, 1080)")
# Адрес
address = driver.find_element(By.XPATH, "//*[@id='address']/div/div/input")
address.send_keys("г Ижевск, ул Университетская, д 1")
address.click()
wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vue-dadata__suggestions')))
address.send_keys(Keys.ARROW_DOWN)
address.send_keys(Keys.ENTER)
# Телефон
fill_field("phone", "9092223334")
# Загрузка файла
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys(
    "/Users/tatyana/PycharmProjects/pythonProject/PythonProject/img/12.jpg")
time.sleep(5)
driver.find_element(By.XPATH, "//button[2]").click()