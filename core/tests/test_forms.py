from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@email.com'
        self.assunto = 'Envio de email'
        self.mensagem = 'Testando envio de email'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)  # ContatoForm(request.POST)

    def test_send_mail(self):
        form1 = ContatoForm(self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEqual(res1, res2)
