#Noah Zissman
#TEC 284
from gpiozero import LED, Button   
import time #delay timer
from signal import pause

red_led = LED(17) #Pin assignment
green_led = LED(27)
blue_led = LED(22)

btn_red = Button(5) #Button Assignment 
btn_green = Button(6)
btn_blue = Button(13)

def setup():
    red_led.off()
    green_led.off()
    blue_led.off()

def main():
    setup()
    print("Press Button")
    
    try:
        while True:
            if btn_red.is_pressed:
                red_led.on()
            else:
                red_led.off()
            
            if btn_green.is_pressed:
                green_led.on()
            else:
                green_led.off()
            
            if btn_blue.is_pressed:
                blue_led.on()
            else:
                blue_led.off()
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program Stopped")
    finally:
        red_led.off()
        green_led.off()
        blue_led.off()
        
        
        
