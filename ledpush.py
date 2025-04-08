import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button - GPIO18
GPIO.setup(24, GPIO.OUT)  #LED - GPIO24
print("Program ON")
try:
    while True:
        print("Petla ON")
        button_state = GPIO.input(18)
        if button_state == False:
            GPIO.output(24, True)
            print('Button Pressed...')
            time.sleep(0.2)
        else:
            GPIO.output(24, False)
except KeyboardInterrupt:
    print("\nZatrzymano program.")
finally:
    print("Koniec programu.")
    GPIO.cleanup()