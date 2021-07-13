from django.test import LiveServerTestCase
from selenium import webdriver


class AnimalTestCase(LiveServerTestCase):
    # Inicia o browser
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')

    # Fecha o browser
    def tearDown(self):
        self.browser.quit()

    def test_search_for_animal(self):
        """Teste se um usuario busca por um animal"""
        # Ele encontra o Busca Animal e decide usar
        homepage = self.browser.get(self.live_server_url + '/')
        # porque ele ve no menu do site escrito Busca Animal
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
