import multiprocessing as mp
from multiprocessing import JoinableQueue
from typing import Type
from logging import Logger

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.input.input_driver import InputDriver

class InputProcess(mp.Process):
    def __init__(self, logger: Type[Logger], config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        super().__init__()
        self._cfg = config
        self._messageQueue = messageQueue
        self._logger = logger

    def run(self):
        try:
            InputDriver(self._cfg, self._messageQueue)
        except KeyboardInterrupt:
            return
        except:
            self._logger.exception('Exception occurred', exc_info=True)