from django.http import response
from django.test import RequestFactory, TestCase
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory
        self.animal = Animal.objects.create(
            nome_animal='Cachorro',
            predador='Não',
            venenoso='Não',
            domestico='Sim'
        )

    def test_index_view_retorna_caracteristicas_do_animal(self):
        """Teste que verifica se a index retorna as caracteristicas do animal pesquisado"""
        # Significado self.client : é o cliente de teste Django integrado.
        # Este não é um navegador real e nem mesmo faz solicitações reais.
        # Ele apenas constrói um objeto Django HttpRequest e o passa pelo processo de solicitação / resposta - middleware, resolvedor de URL, visão, modelo - e retorna tudo o que o Django produz.
        # Ele não analisará essa resposta, nem a renderizará, e não fará outras solicitações orientadas pelo HTML para recursos etc.
        response = self.client.get('/',
                                   {'buscar': 'Cachorro'}
                                   )
        # pega o conteudo da resposta
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        # assetIs verifica que tipo de dados estao sendo utilizado no caso desse querySet
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        # Verifica se nessa possição é o animal criado
        self.assertEqual(
            caracteristica_animal_pesquisado[0].nome_animal, 'Cachorro')
