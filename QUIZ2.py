import RPi.GPIO as GPIO
import time

RED_PIN = 17
GREEN_PIN=27
BLUE_PIN = 22

BTN_RED = 5
BTN_GREEN = 6
BTN_BLUE = 13

def setup():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN, GPIO.OUT)
    
    GPIO.setup(BTN_RED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BTN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BTN_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
def set_color(r, g, b):
    
    GPIO.output(RED_PIN, r)
    GPIO.output(GREEN_PIN, g)
    GPIO.output(BLUE_PIN, b)

def read_buttons():
    red = GPIO.input(BTN_RED)
    green = GPIO.input(BTN_GREEN)
    blue = GPIO.input(BTN_BLUE)
    return red, green, blue

def main():
    setup()
    print("Press Button")
    
    try:
        while True:
            r, g, b = read_buttons()
            set_color(r, g, b)
            time.sleep(0.1)
    except KeyboardInterrupt:
            print("Exiting")
    finally:
            set_color(0, 0, 0)
            GPIO.cleanup()
if __name__ == "__main__":
    main()
    
    
    

    
    
    

    
    
    