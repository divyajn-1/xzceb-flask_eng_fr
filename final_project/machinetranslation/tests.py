'''Unit tests for both functions E2F and F2E'''

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''all 4 test functions'''

    #e2f tests

    def test1(self):
        '''null input test for e2f'''
        self.assertNotEqual(english_to_french(' '), None)

    def test2(self):
        '''hello to bonjour test'''
        self.assertEqual(english_to_french('Hello'), 'Bonjour',  )

    #f2e tests

    def test3(self):
        '''null input test for f2e'''
        self.assertNotEqual(french_to_english(' '), None)

    def test4(self):
        ''' bonjour to hello test'''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
