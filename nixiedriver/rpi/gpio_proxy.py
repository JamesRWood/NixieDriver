_rpiLoaded = True

try:
    import RPi.GPIO as GPIO
except:
    _rpiLoaded = False

class GPIOProxy():
    BCM = GPIO.BCM if _rpiLoaded else 'BCM'
   
    HIGH = GPIO.HIGH if _rpiLoaded else 'HIGH'
    LOW = GPIO.LOW if _rpiLoaded else 'LOW'

    IN = GPIO.IN if _rpiLoaded else 'IN'
    OUT = GPIO.OUT if _rpiLoaded else 'OUT'

    FALLING = GPIO.FALLING if _rpiLoaded else 'FALLING'
    RISING = GPIO.RISING if _rpiLoaded else 'RISING'
    BOTH = GPIO.BOTH if _rpiLoaded else 'BOTH'

    PUD_UP = GPIO.PUD_UP if _rpiLoaded else 'PUD_UP'
    PUD_DOWN = GPIO.PUD_DOWN if _rpiLoaded else 'PUD_DOWN'

    def setmode(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setmode(*args, **kwargs)
        else:
            pass

    def setwarnings(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setwarnings(*args, **kwargs)
        else:
            pass

    def setup(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setup(*args, **kwargs)
        else:
            pass

    def input(*args, **kwargs):
        if _rpiLoaded:
            GPIO.input(*args, **kwargs)
        else:
            pass

    def output(*args, **kwargs):
        if _rpiLoaded:
            GPIO.output(*args, **kwargs)
        else:
            pass

    def add_event_detect(*args, **kwargs):
        if _rpiLoaded:
            GPIO.add_event_detect(*args, **kwargs)
        else:
            pass

    def cleanup(*args, **kwargs):
        if _rpiLoaded:
            GPIO.cleanup(*args, **kwargs)
        else:
            pass