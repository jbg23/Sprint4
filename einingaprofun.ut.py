import unittest
from Spurningaleikur_grafik_rett import Question
from subprocess import call

quest= Question(1,0)
class TestSpurningaleikur(unittest.TestCase):
    call(['clear'])


    """def setUp(self):
        self.func= Question(1,0)"""

    def test_2(self):
        self.assertEqual(quest.leikmadur, 0)

if __name__ == '__main__':
    unittest.main()
