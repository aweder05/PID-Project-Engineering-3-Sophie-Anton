# PID Project Engineering 3 
# _**The Banana of Doom**_ 

<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/banana%20border.png?raw=true" width = 700>

## Table of Contents 

* [Project Idea](#Project_Idea)
* [Proposed Project Schedule](#Proposed_Project_Schedule)
* [CAD Design for PID Project](#CAD_Design_for_PID_Project)
* [Planning for CAD](#Planning_for_CAD)
* [Planning for Code](#Planning_for_Code)
* [CAD Images](#CAD_Images)
* [Code Prototype and Evidence](#Code_Prototype_and_Evidence)
* [Wiring](#Wiring)
* [Evidence](#Evidence)
<!-- <a name="CAD_Design_for_PID_Project"></a>  -->
<!-- <a name="Project_Idea"></a> -->

## **Project_Idea**

Since we were unable to completely finish our last project, we decided that we would choose a simple PID project. This was also because PID was a completely new concept to use, and because we knew that it would take up a lot of our time to find a basis of understanding for PID and how to apply that to our coding and all other aspects of our project. Therefore, we decided to do the following: create a box with a TT-Motor on the inside, which spins a mini-banana on the outside. This would then be read by a photointerruptor in terms of rotations per minute. Then this value would be displayed on the front of our box using a Liquid Crystal Display. The entire box would be powered by a 9-Volt battery back, with an on switch and a corresponding LED to signify if our box was switched on or not.

## Proposed_Project_Schedule  

Attached below is a table of our week-to-week goals, and what we would like to get done in that time.
The most likely outcome is that we will probably need more time for some things, and less time for others. For example, code and assembly may need more time than CAD and planning.

| **Week / Day**       | **To-Do**            |
| -------------------- | -------------------- |
|                      |                      |
| **Week of 4/17-21**  | CAD Design           |
| **Week of 4/24-28**  | See Below            |
| Monday               | CAD Retouches        |
| Tuesday-Friday       | Fabrication/Assembly |
| **Week of 5/1-5**    | PID Coding           |
| **Week of 5/8-12**   | PID Coding           |
| **Week of 5/15-19**  | PID Tuning           |
| **Week of 5/22-26**  | PID Tuning/Testing   |
| **Week of 5/29-6/2** | Extra Time           |

# **Planning**

| Planning_for_CAD | Planning_for_Code |
| :------------ | :------------- |
| <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/CAD.PID.Planning.png?raw=true" width="300">  |  <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/PLANNING.CODE.png?raw=true" width="300"> |
| From the Robotic Arm Project, we learned that learned that ambitious ideas mixed with inefficient planning produces poor results. For the PID project, we modeled a box where the PID is performed between the motor and the photointerrupter, and is displayed on an LCD screen. | I had trouble understanding PID initially, which is why I had to organize my thoughts as shown above. I made a checklist of what to do in order to get the project working. In the future I think it would be a good idea to make this a habit before starting code so that I can start with small tasks leading up to a larger one

----

## CAD_Design_for_PID_Project

We knew that we needed to choose a simple project to make it so that we wouldn't have to cram in everything all at once near the end of our project. That was reflected in the way we approached our CAD design, as we opted for a simple T-Slot box with all the electronic elements on the inside. The only slightly-challenging element of our CAD Design process was making sure that there was enough space for everything, especially since we knew that we would need plenty of space for all of the wiring for the LCD, LED, Adafruit Metro, Switch, TT-Motor, and finally the Photointerruptor. In the end, reflecting on what we could have probably done better, it might have been smart to make the box a little bigger in order to allow for better ease if access while wiring.

## Materials
- Adafruit Metro M4 Airift Lite Board
- Breadboard
- I2C Liquid Crystal Display 2x16
- Panel-Mount LED
- Panel-Mount Switch 
- Adafruit Photointerruptor 
- TT-Motor / DC Gearbox Motor
- Arduino Prototyping Shield 
- 9V Battery Pack

---- 



## **CAD_Images**

| | | 
|-|- | 
|<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/assets/112981462/63fc40c7-1fdc-4013-946f-fb41ca2daa3c" width="300"> |<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/assets/112981462/0dfa37ee-ca52-4004-9bfc-da7c6b830cb5" width="300"> | 
|This is a 3/4 view of our project CAD. My partner and I were sure to take an image that shows the inside of the box. This angle displays where the LCD, motor, battery pack, LED, and switch are positioned. | This image encapsulates what the inside of the box looks like, minus the jumper wires. | 
|<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/assets/112981462/c7c0869f-74ba-422c-8d60-07509ed2f411" width="300"> |<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/assets/112981462/830d2f33-b15f-41eb-a28a-b038ec8a305c" width="300"> |
|This image shows the outside of the box. This angle exemplifies what the box would look like fabricated. The LED and switch are placed around the LCD, with the battery pack on top of the box, and the photointerrupter and motor piece on the side. | This is the piece that attaches to the motor.

## **Code_Prototype_and_Evidence**

```python
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
```
This is the beginning of the PID code. So far we have the Rotations per Minute being calculated (implying that the photointerrupter is functioning properly) and sent to the lcd display. Our next steps are to get the motor running, and control it using PID.

I needed help with the code for the RPM:
```python
if interrupts % 10 == 0:  #  if the interrupt number divided by ten has the remainder of zero, run this code:
        time1= time.monotonic()
    elif interrupts % 10 == 9:
        time2 = time.monotonic()
        RPM = 60/((time2-time1)/10)
```
Thanks to Paul Weder, I learned that the percent sign is a "modulo operator". A modulo operator divides the left hand number/variable with the right hand number/variable and retrieves the remainder.

## __Wiring__

<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/Wiring%20Diagram%20PID.png?raw=true" width="600"> 

----

##### This is the final wiring. The hardest thing about wiring this project was the space that we allowed ourselves to work with from the beginning. Since we wanted to avoid having a large and bulky box, we decided during our design process that we would try and fit everything inside a relatively small box. Eventually we decided that it would probably be better to take all of the electronic components out of the box, get it working, and then assemble everything at the end.

---- 

|Breadboard Zoom-In | Metro Board Zoom-In | 
|-|-|
| <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/Photointerrupter_PID.png?raw=true" width="300"> | <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/SDA_SCL_PID.png?raw=true" width="300"> |
|Because we had to use a mini breadboard in the place of the photointerrupter, this is a zoomed in screenshot of the individual pins. Your can follow colored wires to their pins in the larger image.| Similar to the image beside it, this is an inflated image used to exemplify the SCL and SDA pins that don't appear on Arduino's, but do on Metro's, which is what we used. SCL and SDA pins are important for the LCD display. Again, you can follow the wire colors to the LCD. |








## Evidence

[GIF of working LCD displaying RPM]

##### This is evidence of the LCD displaying RPM, and the photointerrupter working.

----

