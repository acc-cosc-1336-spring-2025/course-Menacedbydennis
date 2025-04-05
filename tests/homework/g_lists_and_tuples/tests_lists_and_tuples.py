import unittest
from src.homework.g_lists_and_tuples.dictionary import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertAlmostEqual(get_p_distance(list1, list2), 0.4, places=5)

    def test_get_p_distance_matrix(self):
        dna_list = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        self.assertEqual(get_p_distance_matrix(dna_list), expected)

if __name__ == '__main__':
    unittest.main()

