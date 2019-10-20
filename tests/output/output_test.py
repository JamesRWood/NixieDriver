import unittest

from nixiedriver.output.output import Output

class Output_Output_Test(unittest.TestCase):
    def test_constructor(self):
        # Arrange
        a = 1
        b = 5
        c = 8 
        d = 4

        # Act
        obj = Output(a, b, c, d)

        # Assert
        map(self.assertIsInstance, [int, int, int, int], [obj.tubeA, obj.tubeB, obj.tubeC, obj.tubeD])
        map(self.assertEqual, [a, b, c, d], [obj.tubeA, obj.tubeB, obj.tubeC, obj.tubeD])