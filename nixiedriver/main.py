import argparse
import multiprocessing as mp
from multiprocessing import JoinableQueue

from nixiedriver.config.config_manager import ConfigManager
from nixiedriver.output.output_process import OutputProcess
from nixiedriver.input.input_process import InputProcess
from nixiedriver.clock.time_process import TimeProcess
from nixiedriver.rpi.gpio_proxy import GPIOProxy

def main(argv):
    GPIOProxy.setmode(GPIOProxy.BCM)
    GPIOProxy.setwarnings(False)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--debug', action='store_true', help='run in debug mode')

    parsed_args, unparsed_args = arg_parser.parse_known_args(argv)
    argv = argv[:1] + unparsed_args

    message_queue = mp.JoinableQueue()
    config = ConfigManager()

    if parsed_args.debug:
        config.set('run', 'debug_mode', 'True')

    dependencies = {
        "config": config,
        "messageQueue": message_queue
    }

    process_classes = (OutputProcess, InputProcess, TimeProcess)
    procs = [P(**dependencies) for P in process_classes]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()