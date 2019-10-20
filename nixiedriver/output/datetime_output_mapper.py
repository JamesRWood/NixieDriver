from typing import Type
from datetime import datetime

from .output_driver import OutputDriver
from .output_mode import OutputMode
from .output import Output

class DateTimeOutputMapper:
    def __init__(self):
        self._24HrFormat = "%H %M"
        self._12HrFormat = "%I %M"
        self._dateFormat = "%d %m"
        self._outputMode = OutputMode.Military

        self._outputSwitch = {
            OutputMode.Military: self._military,
            OutputMode.Standard: self._standard,
            OutputMode.Date: self._date
        }

    def setFormat(self, outputMode: Type[OutputMode]):
        self._outputMode = outputMode

    def map(self, dateTime: Type[datetime]) -> Output:
        formatFunc = self._outputSwitch.get(self._outputMode)
        outputString = formatFunc(dateTime).split(" ")
        return Output(int(outputString[0][0]), int(outputString[0][1]), int(outputString[1][0]), int(outputString[1][1]))

    def _military(self, dateTime: Type[datetime]) -> str:
        return dateTime.strftime(self._24HrFormat)

    def _standard(self, dateTime: Type[datetime]) -> str:
        return dateTime.strftime(self._12HrFormat)

    def _date(self, dateTime: Type[datetime]) -> str:
        return dateTime.strftime(self._dateFormat)
