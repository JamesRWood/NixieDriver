from typing import Type
from multiprocessing import JoinableQueue

from nixiedriver.output.output_mode import OutputMode
from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.rpi.GPIO import GPIO
from nixiedriver.messages import OutputModeUpdatedMessage

class InputDriver:
    def __init__(self, config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        self._messageQueue = messageQueue
        self._outputMode = OutputMode.Military

        _outputModePin = config.getInt('input', 'output_mode_pin')
        _dateModePin = config.getInt('input', 'date_mode_pin')

        GPIO.setup(_outputModePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(_outputModePin, GPIO.FALLING, callback=self._toggleOutputTimeMode, bouncetime=300)
        GPIO.add_event_detect(_dateModePin, GPIO.FALLING, callback=self._showDate)
        GPIO.add_event_detect(_dateModePin, GPIO.RISING, callback=self._showTime)

    def _toggleOutputTimeMode(self):
        if self._outputMode == OutputMode.Military:
            self._outputMode = OutputMode.Standard
        else:
            self._outputMode = OutputMode.Military

        self._messageQueue.put(OutputModeUpdatedMessage(self._outputMode))

    def _showDate(self):
        self._messageQueue.put(OutputModeUpdatedMessage(OutputMode.Date))

    def _showTime(self):
        self._messageQueue.put(OutputModeUpdatedMessage(self._outputMode))