_rpiLoaded = True

try:
    import RPi.GPIO as GPIO
except:
    _rpiLoaded = False

class GPIO():
    BCM = GPIO.BCM if _rpiLoaded else 'BCM'
   
    HIGH = GPIO.HIGH if _rpiLoaded else 'HIGH'
    LOW = GPIO.LOW if _rpiLoaded else 'LOW'

    IN = GPIO.IN if _rpiLoaded else 'IN'
    OUT = GPIO.OUT if _rpiLoaded else 'OUT'

    FALLING = GPIO.FALLING if _rpiLoaded else 'FALLING'
    RISING = GPIO.RISING if _rpiLoaded else 'RISING'

    PUD_UP = GPIO.PUD_IP if _rpiLoaded else 'PUD_UP'
    PUD_DOWN = GPIO.PUD_DOWN if _rpiLoaded else 'PUD_DOWN'

    def setmode(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setmode(args, kwargs)
        else:
            pass

    def setwarnings(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setwarnings(args, kwargs)
        else:
            pass

    def setup(*args, **kwargs):
        if _rpiLoaded:
            GPIO.setup(args, kwargs)
        else:
            pass

    def output(*args, **kwargs):
        if _rpiLoaded:
            GPIO.output(args, kwargs)
        else:
            pass

    def add_event_detect(*args, **kwargs):
        if _rpiLoaded:
            GPIO.add_event_detect(args, kwargs)
        else:
            pass