import unittest
from unittest.mock import patch
from datetime import datetime
from typing import Type

from multiprocessing import JoinableQueue
from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.output.output_process import OutputProcess
from nixiedriver.output.output_mode import OutputMode
from nixiedriver.messages import OutputModeUpdatedMessage, TimeUpdatedMessage

from nixiedriver.output.datetime_output_mapper import DateTimeOutputMapper
from nixiedriver.output.output_driver import OutputDriver
from nixiedriver.output.output import Output

def map_callback(dateTime: Type[datetime]) -> Output:
    x = dateTime.strftime("%H %M").split(" ")
    return Output(int(x[0][0]), int(x[0][1]), int(x[1][0]), int(x[1][1]))

class Output_OutputProcess_Test(unittest.TestCase):
    def setUp(self):
        self._config = ConfigManager()
        self._messageQueue = JoinableQueue()
        self._unitUnderTest = OutputProcess(self._config, self._messageQueue)

    def tearDown(self):
        self._config = None
        self._messageQueue = None
        self._unitUnderTest = None

    @patch.object(DateTimeOutputMapper, "setFormat")
    def test_output_mode_updated_message_date(self, mock_set_format):
        # Arrange
        outputMode = OutputMode.Date
        message = OutputModeUpdatedMessage(outputMode)

        # Act
        self._messageQueue.put(message)
        self._unitUnderTest.run(run_once=True)        

        # Assert
        self.assertEqual(1, mock_set_format.call_count)
        mock_set_format.assert_called_with(outputMode)

    @patch.object(DateTimeOutputMapper, "setFormat")
    def test_output_mode_updated_message_standard(self, mock_set_format):
        # Arrange
        outputMode = OutputMode.Standard
        message = OutputModeUpdatedMessage(outputMode)

        # Act
        self._messageQueue.put(message)
        self._unitUnderTest.run(run_once=True)        

        # Assert
        self.assertEqual(1, mock_set_format.call_count)
        mock_set_format.assert_called_with(outputMode)

    @patch.object(DateTimeOutputMapper, "setFormat")
    def test_output_mode_updated_message_military(self, mock_set_format):
        # Arrange
        outputMode = OutputMode.Military
        message = OutputModeUpdatedMessage(outputMode)

        # Act
        self._messageQueue.put(message)
        self._unitUnderTest.run(run_once=True)        

        # Assert
        self.assertEqual(1, mock_set_format.call_count)
        mock_set_format.assert_called_with(outputMode)

    @patch.object(DateTimeOutputMapper, "map", side_effect=map_callback)
    @patch.object(OutputDriver, "update")
    def test_time_updated_message(self, mock_update, mock_map):
        # Arrange
        dateTime = datetime.strptime("Aug 23 2017 19:36", "%b %d %Y %H:%M")
        message = TimeUpdatedMessage(dateTime)

        # Act
        self._messageQueue.put(message)
        self._unitUnderTest.run(run_once=True)

        # Assert
        self.assertEqual(1, mock_map.call_count)
        self.assertEqual(1, mock_update.call_count)

        outputArg: Output = mock_update.call_args[0][0]

        map(self.assertEqual, [1, 9, 3, 6], [outputArg.tubeA, outputArg.tubeB, outputArg.tubeC, outputArg.tubeD])

if __name__ == '__main__':
    unittest.main()