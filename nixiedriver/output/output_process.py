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
        while cont:
            # Will await a message on the queue
            message = self._messageQueue.get()

            if isinstance(message, OutputModeUpdatedMessage):
                self._outputMapper.setFormat(message.outputMode())
                self._messageQueue.task_done()

            elif isinstance(message, TimeUpdatedMessage):
                output =  self._outputMapper.map(message.dateTime())
                self._outputDriver.update(output)
                self._messageQueue.task_done()

            if run_once:
                cont = False
        return