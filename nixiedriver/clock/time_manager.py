import time, sched

from typing import Type
from multiprocessing import JoinableQueue
from datetime import datetime
from time import strftime

from nixiedriver.messages import TimeUpdatedMessage

class TimeManager:
    def __init__(self, messageQueue: Type[JoinableQueue]):
        self._cont = True
        self._messageQueue = messageQueue
        self._sched = sched.scheduler(time.time, time.sleep)
        self._currentMinute = ""

    def run(self):
        self._sched.enter(0.5, 1, self._timeAction)
        self._sched.run()

    def _timeAction(self):
        currentTime = datetime.now()
        cm = currentTime.strftime("%M")
        if cm != self._currentMinute:
            self._currentMinute = cm
            self._messageQueue.put(TimeUpdatedMessage(currentTime))
        self._sched.enter(0.5, 1, self._timeAction)