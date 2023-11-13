import datetime
from django.test import TestCase
from .models import Pergunta,Alternativa
from django.utils import timezone


# Create your tests here.
class PerguntaDataTest(TestCase):
    def test_questions_has(self):
      texto="A tem som de 'U'?"
      data_pub = timezone.now() + datetime.timedelta(days=1)
      pergunta = Pergunta(texto=texto, data_pub=data_pub)
      self.assertIs(pergunta.rece_pub(),True)







