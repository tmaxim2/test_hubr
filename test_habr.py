# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
	#Открываем Firefox
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
		driver = self.driver
	#Открываем сайт google.com
		driver.get("http://www.google.com")
	#Проверяем, что это действительно Google
		self.assertIn("Google", driver.title)
	#Ищем строку поиска
		elem = driver.find_element_by_id("lst-ib")
	#Вводим в нее искомую фразу и нажимаем Enter
		elem.send_keys("habrahabr")
		elem.send_keys(Keys.RETURN)
	#В результатах поиска находим ссылку на сайт habrahabr.ru и переходим на нее
		driver.find_element_by_link_text('Хабрахабр').click()
	#Находим ссылку Песочница и переходим на нее
		driver.find_element_by_link_text('Песочница').click()
	#Находим ссылку на 2-ю страницу раздела Песочница и переходим на нее
		driver.find_element_by_link_text('2').click()

    def tearDown(self):
	#Закрываем Firefox
        self.driver.close()

if __name__ == "__main__":
    unittest.main()