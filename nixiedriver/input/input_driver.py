import time

from typing import Type
from multiprocessing import JoinableQueue

from nixiedriver.output.output_mode import OutputMode
from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.rpi.gpio_proxy import GPIOProxy
from nixiedriver.messages import OutputModeUpdatedMessage

class InputDriver:
    def __init__(self, config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        self._messageQueue = messageQueue
        self._outputMode = OutputMode.Military
        self._showdate = False

        _outputModePin = config.getInt('input', 'output_mode_pin')
        _dateModePin = config.getInt('input', 'date_mode_pin')

        GPIOProxy.setup(_outputModePin, GPIOProxy.IN, GPIOProxy.PUD_DOWN)
        GPIOProxy.setup(_dateModePin, GPIOProxy.IN, GPIOProxy.PUD_DOWN)

        GPIOProxy.add_event_detect(_outputModePin, GPIOProxy.FALLING, callback=self._toggleOutputTimeMode, bouncetime=500)
        GPIOProxy.add_event_detect(_dateModePin, GPIOProxy.BOTH, callback=self._toggleDate, bouncetime=50)

        while True:
            time.sleep(1)

    def _toggleOutputTimeMode(self, channel):
        if self._outputMode == OutputMode.Military:
            self._outputMode = OutputMode.Standard
        else:
            self._outputMode = OutputMode.Military

        self._messageQueue.put(OutputModeUpdatedMessage(self._outputMode))

    def _toggleDate(self, channel):
        if self._showdate == False:
            self._showdate = True
            self._messageQueue.put(OutputModeUpdatedMessage(OutputMode.Date))
        else:
            self._showdate = False
            self._messageQueue.put(OutputModeUpdatedMessage(self._outputMode))
