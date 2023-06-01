import board
import time
import pwmio
import analogio as AIO
import digitalio as DIO
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import PID_CPY as PidLib

setpoint = 5


pid = PidLib.PID(5, 0.01, 0.1, setpoint= setpoint)


i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

inter = DIO.DigitalInOut(board.D11)
inter.direction = DIO.Direction.INPUT
inter.pull = DIO.Pull.UP

# motor =  pwmio.PWMOut(board.D7)
# motor.duty_cycle = 65535``
# print("running")
# time.sleep(0.15)

#  these are the variables needed for the code
intTime =0
interrupts =0
time1 = 0
time2 = 0
RPM = 0
lastVal = False



while True: 
    intTime +=1
    if intTime % 250 ==1 :
        
        #put all prints in here
        print(f"{inter.value} {interrupts} Rpm: {RPM} ")
        lcd.clear()  #  setting lcd up to print
        lcd.set_cursor_pos(0, 0)
        lcd.print(str("RPM = "))
        lcd.print(str(RPM))

    
    #  ensuring that the photointerrupter doesn't output more than one interrupt per interrupt
    if inter.value and lastVal == False:
        lastVal = True
        interrupts += 1
    if not inter.value:
        lastVal  = False

    #  this is the rpm math
    if interrupts % 10 == 0:
        time1= time.monotonic()
    elif interrupts % 10 == 9:
        time2 = time.monotonic()
        RPM = 60/((time2-time1)/10)

        
    # if motor.duty_cycle == True:
    #     lcd.clear()
    #     lcd.set_cursor_pos(0, 1)
    #     lcd.print(str("ON"))
