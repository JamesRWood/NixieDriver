import unittest
from unittest.mock import patch

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.output.output_driver import OutputDriver
from nixiedriver.output.output import Output
from nixiedriver.rpi.gpio_proxy import GPIOProxy

class Output_OutputDriver_Test(unittest.TestCase):
    def setUp(self):
        self._config = ConfigManager()
        self._unitUnderTest = OutputDriver(self._config)

        self._tubeA = [2,3,4,17]
        self._tubeB = [27,22,10,9]
        self._tubeC = [5,6,13,19]
        self._tubeD = [14,15,18,23]

    def tearDown(self):
        self._config = None
        self._unitUnderTest = None
        self._tubeA = None
        self._tubeB = None
        self._tubeC = None
        self._tubeD = None

    @patch.object(GPIOProxy, "output")
    def test_update_0_0_0_0(self, mock_output):
        # Arrange
        x = Output(0, 0, 0, 0)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeB, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeC, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeD, (0, 0, 0, 0))

    @patch.object(GPIOProxy, "output")
    def test_update_1_0_0_0(self, mock_output):
        # Arrange
        x = Output(1, 0, 0, 0)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (0, 0, 0, 1))
        mock_output.assert_any_call(self._tubeB, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeC, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeD, (0, 0, 0, 0))

    @patch.object(GPIOProxy, "output")
    def test_update_0_2_0_0(self, mock_output):
        # Arrange
        x = Output(0, 2, 0, 0)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeB, (0, 0, 1, 0))
        mock_output.assert_any_call(self._tubeC, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeD, (0, 0, 0, 0))

    @patch.object(GPIOProxy, "output")
    def test_update_0_0_3_0(self, mock_output):
        # Arrange
        x = Output(0, 0, 3, 0)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeB, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeC, (0, 0, 1, 1))
        mock_output.assert_any_call(self._tubeD, (0, 0, 0, 0))

    @patch.object(GPIOProxy, "output")
    def test_update_0_0_0_4(self, mock_output):
        # Arrange
        x = Output(0, 0, 0, 4)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeB, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeC, (0, 0, 0, 0))
        mock_output.assert_any_call(self._tubeD, (0, 1, 0, 0))

    @patch.object(GPIOProxy, "output")
    def test_update_5_6_7_8(self, mock_output):
        # Arrange
        x = Output(5, 6, 7, 8)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (0, 1, 0, 1))
        mock_output.assert_any_call(self._tubeB, (0, 1, 1, 0))
        mock_output.assert_any_call(self._tubeC, (0, 1, 1, 1))
        mock_output.assert_any_call(self._tubeD, (1, 0, 0, 0))

    @patch.object(GPIOProxy, "output")
    def test_update_9_9_9_9(self, mock_output):
        # Arrange
        x = Output(9, 9, 9, 9)

        # Act
        result = self._unitUnderTest.update(x)

        # Assert
        self.assertEqual(4, mock_output.call_count)
        mock_output.assert_any_call(self._tubeA, (1, 0, 0, 1))
        mock_output.assert_any_call(self._tubeB, (1, 0, 0, 1))
        mock_output.assert_any_call(self._tubeC, (1, 0, 0, 1))
        mock_output.assert_any_call(self._tubeD, (1, 0, 0, 1))

if __name__ == '__main__':
    unittest.main()