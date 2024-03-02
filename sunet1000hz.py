import utime
import machine

pwm=machine.PWM(machine.Pin(15))


while True:
    pwm.freq(1000)
    pwm.duty_u16(32768)
    utime.sleep(1)
    print("merge")
pwm.deinit()    
