import multiprocessing as mp

from multiprocessing import JoinableQueue
from typing import Type

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.input.input_driver import InputDriver

class InputProcess(mp.Process):
    def __init__(self, config: Type[ConfigManager], messageQueue: Type[JoinableQueue]):
        super().__init__()
        self._cfg = config
        self._messageQueue = messageQueue

    def run(self):
        try:
            InputDriver(self._cfg, self._messageQueue)
        except Exception as e:
            print('InputProcess: Exception "{}"'.format(e))
        pass