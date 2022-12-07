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

class TestSidebar():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sidebar(self):
    self.driver.get("https://qa.neapro.site/login")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("tatianaapisareva@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456789")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".menu-header").click()
    self.driver.find_element(By.CSS_SELECTOR, ".logout_name").click()
  
