import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Teste retorno comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Teste reterno comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Teste returno domirndo pouco."""
        self.assertEqual(
            dormir(4),
            f'Continuo cansado após dormir 4 horas!'
        )

    def test_dormir_muito(self):
        """Teste retorno dormindo muiot."""
        self.assertEqual(
            dormir(10),
            f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        """Teste retorno é engraçada."""
        # self.assertEqual(eh_engracada('Sérgio Malandro'), False)
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado!')


if __name__ == '__main__':
    unittest.main()
