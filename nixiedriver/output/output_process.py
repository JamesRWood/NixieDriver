import multiprocessing as mp

from multiprocessing import JoinableQueue
from typing import Type
from datetime import datetime

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.output.output_mode import OutputMode
from nixiedriver.output.output_driver import OutputDriver
from nixiedriver.output.datetime_output_mapper import DateTimeOutputMapper

from nixiedriver.messages import TimeUpdatedMessage, OutputModeUpdatedMessage

class OutputProcess(mp.Process):
    def __init__(self, config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        super().__init__()
        self._outputDriver = OutputDriver(config)
        self._outputMapper = DateTimeOutputMapper()
        self._messageQueue = messageQueue

    def run(self, run_once=False):
        cont = True
        current_dateTime = None
        while cont:
            # Will await a message on the queue
            message = self._messageQueue.get()

            if isinstance(message, OutputModeUpdatedMessage):
                self._outputMapper.setFormat(message.outputMode())
                self._update(current_dateTime)
                self._messageQueue.task_done()

            elif isinstance(message, TimeUpdatedMessage):
                current_dateTime = message.dateTime()
                self._update(current_dateTime)
                self._messageQueue.task_done()

            if run_once:
                cont = False
        return

    def _update(self, date_time):
        if date_time == None:
            return

        output =  self._outputMapper.map(date_time)
        self._outputDriver.update(output)