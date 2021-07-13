from django.test import LiveServerTestCase
from selenium import webdriver
#import time


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

        # Ele ve um campo para pesquisar animais pelo nome .
        bucar_animal_input = self.browser.find_element_by_css_selector(
            'input#buscar-animal')
        self.assertEquals(bucar_animal_input.get_attribute(
            'placeholder'), 'Exemplo: leão, urso...')

        # Ele pesquisa por Leão e clica no botão pesquisar.
        bucar_animal_input.send_keys('leão')
        # para pausar para ver o codigo rodando
        # time.sleep(2)
        self.browser.find_element_by_css_selector('form button')

        # O site exibe 4 caracteristicas do animal pesquisado.
        # Como seram exibidos + de uma caracteristicas ao inves de utilizar element vai ser utilizado elements
        caracteristicas = self.browser.find_elements_by_css_selector(
            '.result-description')
        #O comando assertGreater ve se ha mais de 3 caracteristicas , se houver ele roda caso nao ele falha
        self.assertGreater(len(caracteristicas), 3)
