import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_quote = Quote('E. W. Dijkstra', 15, 'It is practically impossible to teach good programming style to students that have had prior exposure to BASIC. As potential programmers, they are mentally mutilated beyond hope of regeneration.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote, Quote))

    def test_instance_variables(self):
        self.assertEqual(self.new_quote.author, 'E. W. Dijkstra')
        self.assertEqual(self.new_quote.id, 15)
        self.assertEqual(self.new_quote.quote, 'It is practically impossible to teach good programming style to students that have had prior exposure to BASIC. As potential programmers, they are mentally mutilated beyond hope of regeneration.')