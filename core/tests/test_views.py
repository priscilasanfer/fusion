from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@email.com',
            'assunto': 'Envio de email',
            'mensagem': 'Testando envio de email'
        }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@email.com'
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)

