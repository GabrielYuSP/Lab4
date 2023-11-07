import time
from hal import hal_led as led
from hal import hal_input_switch as switch

def main():
    # Led Blink
    led.init()
    switch.init()
    
    while(1):
        x = switch.read_slide_switch()

        if x == 1:
            led.set_output(0,0)
            time.sleep(0.1)
            led.set_output(0, 1)
            time.sleep(0.1)

        else:
            startTime = 0
            while (startTime < 5):
                led.set_output(0, 1)
                time.sleep(0.1)
                led.set_output(0, 0)
                time.sleep(0.1)
                startTime += 1

            while switch.read_slide_switch == 0:
                led.set_output(0, 0)


if __name__ == "__main__":
    main()