from machine import ADC
import time
import utime
temp_sensor = ADC(4)
motor_pin1 = machine.Pin(14, machine.Pin.OUT)
motor_pin2 = machine.Pin(15, machine.Pin.OUT)

while True:
    adc_voltage = temp_sensor.read_u16() * 3.3 / 65535
    cpu_temp = 27 - (adc_voltage - 0.706)/0.001721 # Formula given in RP2040 Datasheet
    print(cpu_temp)
    time.sleep_ms(1_000)
    if cpu_temp>35:
        motor_pin1.on()
        motor_pin2.off()
        print("merge")
    # Wait for 5 seconds
        utime.sleep(5)
        motor_pin1.off()
        motor_pin2.off()
        
    utime.sleep(5)        
