from time import sleep
from machine import Pin, I2C
import bme280
import utime

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
motor_pin1 = machine.Pin(14, machine.Pin.OUT)
motor_pin2 = machine.Pin(15, machine.Pin.OUT)
def oprireProgram():
    
    motor_pin1.off()
    motor_pin2.off()
    


def startProgram():
    
    while True:
        
        bme = bme280.BME280(i2c=i2c)
        temp = bme.values[0]
        pres = bme.values[1]
        umiditate = bme.values[2]
        inregistrare = 'Temperatura: ' + temp 
        temperatura=float(temp[:-1])
        print(temperatura)
        print(inregistrare)
        if temperatura>25:
            motor_pin1.off()
            motor_pin2.on()
            print("motorul e pornit")
            utime.sleep(25)
            # motor_pin1.off()
            # motor_pin2.off()
            print("motorul e oprit")
            # utime.sleep(5)
            # motor_pin1.off()
            # motor_pin2.on()
            print("motorul e pornit")
            # utime.sleep(5)
            try:
                pass
            except KeyboardInterrupt:
                oprireProgram()
                break
        else:
            oprireProgram()
            

            
        utime.sleep(3)
        
        try:
            pass
        except KeyboardInterrupt:
            oprireProgram()
            break
try:
    startProgram()
except KeyboardInterrupt:
    machine.reset()


    
    