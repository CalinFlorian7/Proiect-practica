import machine
import utime

# Configure PWM output pin
pwm = machine.PWM(machine.Pin(14))

# Set up siren parameters
siren_freq_low = 400  # Lowest frequency of siren
siren_freq_high = 2000  # Highest frequency of siren
siren_duty_cycle_low = 20000  # Lowest duty cycle of siren
siren_duty_cycle_high = 60000  # Highest duty cycle of siren
siren_step_size = 50  # Step size for frequency and duty cycle changes
siren_step_time = 0.01  # Time between each step

# Generate siren sound
freq = siren_freq_low
duty_cycle = siren_duty_cycle_low
while True:
    pwm.freq(freq)
    pwm.duty_u16(duty_cycle)
    if freq >= siren_freq_high:
        freq = siren_freq_low
    else:
        freq += siren_step_size
    if duty_cycle >= siren_duty_cycle_high:
        duty_cycle = siren_duty_cycle_low
    else:
        duty_cycle += siren_step_size
    utime.sleep(siren_step_time)
    
  
