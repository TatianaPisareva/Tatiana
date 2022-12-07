# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPasport():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pasport(self):
    self.driver.get("https://qa.neapro.site/login/")
    self.driver.set_window_size(1280, 800)
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("tatianaapisareva@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldsets:nth-child(1) > .fieldset").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldsets:nth-child(1) > .fieldset").click()
    self.driver.find_element(By.ID, "surname").click()
    self.driver.find_element(By.ID, "surname").send_keys("Фамилия")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Имя")
    self.driver.find_element(By.ID, "patronymic").click()
    self.driver.find_element(By.ID, "patronymic").send_keys("Отчество")
    self.driver.find_element(By.CSS_SELECTOR, "#birthday path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mx-icon-calendar:nth-child(2) > svg").click()
    self.driver.find_element(By.ID, "passportSeries").click()
    self.driver.find_element(By.ID, "passportSeries").send_keys("11-11")
    self.driver.find_element(By.ID, "passportNumber").click()
    self.driver.find_element(By.ID, "passportNumber").send_keys("111111")
    self.driver.find_element(By.CSS_SELECTOR, ".mx-icon-calendar:nth-child(2) > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mx-date-row:nth-child(1) > .cell:nth-child(4) > div").click()
    self.driver.find_element(By.ID, "code").click()
    self.driver.find_element(By.ID, "code").send_keys("111-111")
    self.driver.find_element(By.ID, "cardId").click()
    self.driver.find_element(By.ID, "cardId").send_keys("111-111-111 11")
    self.driver.find_element(By.ID, "issued").click()
    self.driver.find_element(By.ID, "issued").send_keys("Кем выдан")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Ижевск")
    element = self.driver.find_element(By.CSS_SELECTOR, ".phone label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "privacy").click()
    self.driver.find_element(By.CSS_SELECTOR, ".outline").click()
    self.driver.find_element(By.CSS_SELECTOR, ".outline").send_keys("C:\\fakepath\\123.jpg")
    self.driver.find_element(By.CSS_SELECTOR, ".fill").click()
  
