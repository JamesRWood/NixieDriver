import multiprocessing as mp

from multiprocessing import JoinableQueue
from typing import Type

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.clock.time_manager import TimeManager

class TimeProcess(mp.Process):
    def __init__(self, config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        super().__init__()
        self._messageQueue = messageQueue

    def run(self):
        try:
            TimeManager(self._messageQueue).run()
        except Exception as e:
            print('TimeProcess: Exception "{}"'.format(e))