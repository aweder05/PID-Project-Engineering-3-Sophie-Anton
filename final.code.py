import board
import time
import pwmio
import analogio as AIO
import digitalio as DIO
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import PID_CPY as PidLib

setpoint = 180

pid = PidLib.PID(360, 30, 150.0, setpoint= setpoint)
pid.output_limits = (10000, 50000)

time.sleep(3)
#  defining lcd
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

#  difining photointerrupter
inter = DIO.DigitalInOut(board.D11)  # assigns pin to interrupter
inter.direction = DIO.Direction.INPUT  #interrupter is the input
inter.pull = DIO.Pull.UP

#  defining motor
pot = AIO.AnalogIn(board.A0)
motor =  pwmio.PWMOut(board.D7)
motor.duty_cycle = 65535
print("running")
time.sleep(0.15)

# defining led
led = DIO.DigitalInOut(board.A3)
led.direction = DIO.Direction.OUTPUT
led.value = True

#  these are the variables
intTime =0
interrupts =0
RPM = 0
lastVal = False
previous_time = time.monotonic()
rpmCheckTime = 0.5
rpmCheckState = True
photoVal = False           
oldPhotoVal = False # Used to make sure we only count the first loop when interupt is broken

time1 =0
time2 =0
RPM = 0

while True: 

    #  testing range w pot
    # motor_speed = pot.value # both of these values are 16 bit so no mapping is needed
    
    # motor.duty_cycle = motor_speed
    
    motor.duty_cycle = int(pid(RPM))

    intTime +=1
    if intTime % 1000 ==1 : # Every however many loops, print to LCD to reduce flickering
        
        #put all prints in here
        # print(f"{inter.value} {interrupts} Rpm: {RPM} TMC: {time.monotonic()}")
        #  setting up/writing to LCD
        lcd.clear()
        lcd.set_cursor_pos(0, 0)
        lcd.print(str("RPM = "))
        lcd.print(str(RPM))

    #  Prevents interrupter from interrupting more than once per interrupt
    photoVal = inter.value 


    if photoVal and (oldPhotoVal == False):
        oldPhotoVal = True
        interrupts += 1
        
        if interrupts % 2 == 0:
            time2= time.monotonic()
            RPM = 1.0/((time2-time1))*60
            print((f"{inter.value} {interrupts} Rpm: {RPM} 1"))
            time.sleep(0.05)
            time1 = time2
        elif interrupts % 2 == 1:    # first 
            time2 = time.monotonic()
            RPM = 1.0/((time2-time1))*60
            print((f"{inter.value} {interrupts} Rpm: {RPM} 2"))
            time.sleep(0.05)
            time1 = time2
    #print(pid.components)
    if not photoVal:
        oldPhotoVal  = False



    # # if enough time has elapsed - calc RPM    
    # if time.monotonic() > previous_time + rpmCheckTime:
    #     print("calc RPM")
    #     time_diff = time.monotonic() - previous_time + 0.1
    #     RPM = (interrupts/2.0/time_diff) * 60.0
    #     previous_time = time.monotonic()
    #     interrupts = 0
