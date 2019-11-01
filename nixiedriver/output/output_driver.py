from typing import Type

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.output.output import Output
from nixiedriver.rpi.gpio_proxy import GPIOProxy

class OutputDriver:
    def __init__(self, config: Type[ConfigManager]):
        self._debugMode = config.getBoolean('run', 'debug_mode')

        self._gpio_tube_a, self._gpio_tube_b, self._gpio_tube_c, self._gpio_tube_d = map(config.getIntList, ['nixtube', 'nixtube', 'nixtube', 'nixtube'], ['tubea_pin_array', 'tubeb_pin_array', 'tubec_pin_array', 'tubed_pin_array'])
        
        GPIOProxy.setup(self._gpio_tube_a + self._gpio_tube_b + self._gpio_tube_c + self._gpio_tube_d, GPIOProxy.OUT)

    def update(self, output: Type[Output]):
        tubeA, tubeB, tubeC, tubeD = map(self._getGPIOInput, [output.tubeA, output.tubeB, output.tubeC, output.tubeD])

        if self._debugMode == True: 
            print(f'{tubeA[0]}{tubeA[1]}{tubeA[2]}{tubeA[3]} {tubeB[0]}{tubeB[1]}{tubeB[2]}{tubeB[3]} {tubeC[0]}{tubeC[1]}{tubeC[2]}{tubeC[3]} {tubeD[0]}{tubeD[1]}{tubeD[2]}{tubeD[3]}')

        else:
            _param_array = [
                _GPIOOutputParameter(self._gpio_tube_a, tubeA),
                _GPIOOutputParameter(self._gpio_tube_b, tubeB),
                _GPIOOutputParameter(self._gpio_tube_c, tubeC),
                _GPIOOutputParameter(self._gpio_tube_d, tubeD)
            ]

            [GPIOProxy.output(x.tube, x.value) for x in _param_array]

    def _getGPIOInput(self, intValue: int) -> tuple:
        return tuple([int(s) for s in list(self._intToBCD(intValue))])

    def _intToBCD(self, intValue: int) -> str:
        return format(int(hex(intValue), 16), '04b')

class _GPIOOutputParameter:
    def __init__(self, tube: [], value: Type[tuple]):
        self.tube: [] = tube
        self.value: tuple = value