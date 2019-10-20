from typing import Type
from datetime import datetime

from nixiedriver.output.output_mode import OutputMode

class TimeUpdatedMessage():
    def __init__(self, newDateTime: Type[datetime]):
        self._dateTime: datetime = newDateTime

    def dateTime(self) -> datetime:
        return self._dateTime

class OutputModeUpdatedMessage():
    def __init__(self, outputMode: Type[OutputMode]):
        self._outputMode: OutputMode = outputMode

    def outputMode(self) -> OutputMode:
        return self._outputMode