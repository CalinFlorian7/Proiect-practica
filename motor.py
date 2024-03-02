import machine
import utime

# Define the GPIO pins connected to the L9110S motor driver module
motor_pin1 = machine.Pin(14, machine.Pin.OUT)
motor_pin2 = machine.Pin(15, machine.Pin.OUT)


while True:
    # Enable the motor driver
  

    # Turn the motor on in one direction
    motor_pin1.on()
    motor_pin2.off()
    print("merge")
    # Wait for 5 seconds
    utime.sleep(5)
    motor_pin1.off()
    motor_pin2.off()
    utime.sleep(5)
    # Turn the motor off
    motor_pin1.off()
    motor_pin2.on()
    print(" nu merge")
    utime.sleep(5)
    
    motor_pin1.off()
    motor_pin2.off()
    utime.sleep(5)
    # Disable the motor driver
    
