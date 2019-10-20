import unittest
from datetime import datetime

from nixiedriver.output.datetime_output_mapper import DateTimeOutputMapper
from nixiedriver.output.output import Output
from nixiedriver.output.output_mode import OutputMode

class Output_DateTimeOutputMapper_Test(unittest.TestCase):
    def setUp(self):
        self._testDate = datetime.strptime("Jun 16 2016 15:47", "%b %d %Y %H:%M")
        self._unitUnderTest = DateTimeOutputMapper()

    def tearDown(self):
        self._testDate = None
        self._unitUnderTest = None

    def test_map_military(self):
        # Arrange
        self._unitUnderTest.setFormat(OutputMode.Military)

        # Act
        result = self._unitUnderTest.map(self._testDate)

        # Assert
        map(self.assertEqual, [result.tubeA, result.tubeB, result.tubeC, result.tubeD], [1, 5, 4, 7])

    def test_map_standard(self):
        # Arrange
        self._unitUnderTest.setFormat(OutputMode.Standard)

        # Act
        result = self._unitUnderTest.map(self._testDate)

        # Assert
        map(self.assertEqual, [result.tubeA, result.tubeB, result.tubeC, result.tubeD], [0, 3, 4, 7])

    def test_map_date(self):
        # Arrange
        self._unitUnderTest.setFormat(OutputMode.Date)

        # Act
        result = self._unitUnderTest.map(self._testDate)

        # Assert
        map(self.assertEqual, [result.tubeA, result.tubeB, result.tubeC, result.tubeD], [1, 6, 0, 6])

if __name__ == '__main__':
    unittest.main()