import multiprocessing as mp
from multiprocessing import JoinableQueue
from typing import Type
from logging import Logger

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.clock.time_manager import TimeManager

class TimeProcess(mp.Process):
    def __init__(self, logger: Type[Logger], config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        super().__init__()
        self._messageQueue = messageQueue
        self._logger = logger

    def run(self):
        try:
            TimeManager(self._messageQueue).run()
        except KeyboardInterrupt:
            return
        except:
            self._logger.exception('Exception occurred', exc_info=True)