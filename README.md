# PID Project Engineering 3 
# _**The Banana of Doom**_ 

<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/banana%20border.png?raw=true" width = 700>

## __Table of Contents__

* [Project Porposal](#Project_Idea)
    * [Project Idea](#Project_Idea)
    * [Proposed Project Schedule](#Propsed_Project_Schedule)
* [CAD Design for PID Project](#CAD_Design_for_PID_Project)
* [Planning](#Planning)
* [CAD Images](#CAD_Images)
* [Code Prototype and Evidence](#Code_Prototype_and_Evidence)
* [Evidence for Code Prototype](#Evidence_for_Code_Prototype)
* [Wiring for Prototype](#Wiring_for_Prototype)

<!-- <a name="CAD_Design_for_PID_Project"></a>  -->
<!-- <a name="Project_Idea"></a> -->

## **Project_Idea**

Since we were unable to completely finish our last project, we decided that we would choose a simple PID project. This was also because PID was a completely new concept to use, and because we knew that it would take up a lot of our time to find a basis of understanding for PID and how to apply that to our coding and all other aspects of our project. Therefore, we decided to do the following: create a box with a TT-Motor on the inside, which spins a mini-banana on the outside. This would then be read by a photointerruptor in terms of rotations per minute. Then this value would be displayed on the front of our box using a Liquid Crystal Display. The entire box would be powered by a 9-Volt battery back, with an on switch and a corresponding LED to signify if our box was switched on or not.

---

## __Proposed_Project_Schedule__

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

---

## **Planning**

| Planning_for_CAD | Planning_for_Code |
| :------------ | :------------- |
| <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/CAD.PID.Planning.png?raw=true" width="300">  |  <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/PLANNING.CODE.png?raw=true" width="300"> |
| From the Robotic Arm Project, we learned that learned that ambitious ideas mixed with inefficient planning produces poor results. For the PID project, we modeled a box where the PID is performed between the motor and the photointerrupter, and is displayed on an LCD screen. | I had trouble understanding PID initially, which is why I had to organize my thoughts as shown above. I made a checklist of what to do in order to get the project working. In the future I think it would be a good idea to make this a habit before starting code so that I can start with small tasks leading up to a larger one

----

## __CAD_Design_for_PID_Project__

We knew that we needed to choose a simple project to make it so that we wouldn't have to cram in everything all at once near the end of our project. That was reflected in the way we approached our CAD design, as we opted for a simple T-Slot box with all the electronic elements on the inside. The only slightly-challenging element of our CAD Design process was making sure that there was enough space for everything, especially since we knew that we would need plenty of space for all of the wiring for the LCD, LED, Adafruit Metro, Switch, TT-Motor, and finally the Photointerruptor. In the end, reflecting on what we could have probably done better, it might have been smart to make the box a little bigger in order to allow for better ease if access while wiring.

### __The link to our Onshape document can be found here: [link](https://cvilleschools.onshape.com/documents/eb53edd93056d781bfd5d1be/w/7a942e8a39012302d831d4e7/e/d26a37774ba29daec19e587c?renderMode=0&uiState=6479f2072df10846c8d284a7)__
---
## __Materials__
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
----

### Link for Prototype Code can be found [Here](prototype.py), for the sake of space

----

##### This is the beginning of the PID code. So far we have the Rotations per Minute being calculated (implying that the photointerrupter is functioning properly) and sent to the lcd display. Our next steps are to get the motor running, and control it using PID.

I needed help with the code for the RPM:
```python
if interrupts % 10 == 0:  #  if the interrupt number divided by ten has the remainder of zero, run this code:
        time1= time.monotonic()
    elif interrupts % 10 == 9:
        time2 = time.monotonic()
        RPM = 60/((time2-time1)/10)
```
##### Thanks to Paul Weder, I learned that the percent sign is a "modulo operator". A modulo operator divides the left hand number/variable with the right hand number/variable and retrieves the remainder.

```python
if inter.value and lastVal == False:
        lastVal = True
        interrupts += 1
    if not inter.value:
        lastVal  = False
```
##### These lines ensure that the photointerrupter doesn't read an interrupt as more than one interrupt. It acts as a debouncer.
---
### Rewritting of RPM code

```python
# if enough time has elapsed - calc RPM    
    if time.monotonic() > previous_time + rpmCheckTime:
        print("calc RPM") #  variable in code that isn't written in this excerpt; it's the calculation of the RPM
        time_diff = time.monotonic() - previous_time + 0.1
        RPM = (interrupts/2.0/time_diff) * 60.0
        #  the amount of interrupts, divided by 2 (number of spokes on wheel), divided by the time between them, multiplied by 60
        previous_time = time.monotonic()
        interrupts = 0
```

##### We added the code shown above in place of the code postioned below.
##### Although this code is longer and admittedly less efficient, it makes more sense for our project, and uses language that Anton and I can better comprehend.

```python
if interrupts % 10 == 0:
        time1= time.monotonic()
    elif interrupts % 10 == 9:
        time2 = time.monotonic()  #  defining the RPM
        RPM = 60/((time2-time1)/10)
```
---
### PID Code

##### Although the code shown above was written well, it wasn't fit for our project. The math was incorrect, leading to the incorrect RPM.

```python
setpoint = 180

pid = PidLib.PID(500, 0.0, 10, setpoint= setpoint)
pid.output_limits = (10000, 50000)
```
##### This is the new PID code we used to control the power going to the motor. In the 3rd line of this section of code, we stated the range of power the motor will be in to match the setpoint. We stated the set point on the 1st line, then attempted to match that setpoint on the code directly below. Key word: attempt. This isn't the final code for the PID, but because we've found that the motor responds to the PID code, our final steps are to tune it.

```python
motor.duty_cycle = int(pid(RPM))
```
##### This chunk of code sets the motor cycle to the PID, as opposed to the potentiometer.
---
## __Evidence_for_Code_Prototype__

<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/earlycodeevidence.gif?raw=true" width="400">

##### This is evidence of the LCD displaying RPM, and the photointerrupter working properly. The video is a little bit shaky, but what is basically happening is that first you can see a little piece of red wire being waved back and forth between the photointerruptor. Then, you can see that this value is then printed on the serial monitor, and then on the LCD Display.  

----



## __Wiring_for_Prototype__

<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/updated-wiring5.30.23.png?raw=true" width="500"> 

###### The link for the wiring diagram is here, in case the image is not large enough: 

[Wiring Diagram Link](https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/updated-wiring5.30.23.png?raw=true)

----

##### This is probably going to be the final wiring. The hardest thing about wiring this project was the space that we allowed ourselves to work with from the beginning. Since we wanted to avoid having a large and bulky box, we decided during our design process that we would try and fit everything inside a relatively small box. Eventually we decided that it would probably be better to take all of the electronic components out of the box, get it working, and then assemble everything at the end.

---- 

|Breadboard Zoom-In | Metro Board Zoom-In | 
|-|-|
| <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/Photointerrupter_PID.png?raw=true" width="300"> | <img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/SDA_SCL_PID.png?raw=true" width="300"> |
|Because we had to use a mini breadboard in the place of the photointerrupter, this is a zoomed in screenshot of the individual pins. Your can follow colored wires to their pins in the larger image.| Similar to the image beside it, this is an inflated image used to exemplify the SCL and SDA pins that don't appear on Arduino's, but do on Metro's, which is what we used. SCL and SDA pins are important for the LCD display. Again, you can follow the wire colors to the LCD. |

## **Wiring Diagram V.2 | Final Wiring**
<img src="https://github.com/aweder05/PID-Project-Engineering-3-Sophie-Anton/blob/main/media.md/WiringDiagramPIDV.2.png?raw=true" width="700">

----

##### This is the wiring updated wiring diagram. Nearly everything stayed the same except for the changing of the transistor and the implementation of the potentiomenter for the tuning of the PID. This is almost the final wiring, with the exclusion of the potentiomenter, and the inclusion of the LED. The Potentiometer has been included in this version of the wiring because of how we purposed it to try and figure our our desired Setpoint, and to prepare our variables for PID Tuning.

###### Note: the Wiring Diagram V.2 uses the same "Breadboard Zoom In" and "Metro Board Zoom-In" as the initial wiring diagram for the prototype. 

----

## __Final Code__

[insert code here]

A portion of the PID Code was from Copper280z's Github Repository: _CircuitPython Simple PID_

The link for their repository can be found here: [**link**](https://github.com/Copper280z/CircuitPython_simple-pid)

My partner and I spent the most time in calculating the RPM. We had a lot of help from Paul Weder in the beginning, then after better understanding the function of PID, and the importance of RPM, we began to tune the code to our preferations. After coding the RPM, a few lines of code were written to connect the motor power to the PID. Finally, we fine tuned our project to match its setpoint, and the code was done!

---
## **Reflection** 

This project was fun. Although sometimes we had setbacks, or problems that took us annoyingly long to solve, we figured them out. It also taught us even more about many things, especially time management and code. One thing that I'm happy to say is that I am really proud of how we used our time to work as hard as we could on one task, and then moved on to the next. I am also very proud because of how we spent so much extra time in the lab just trying to make any sort of progress. PID is challenging, and it is definitely a good thing that we realized such so early on. It helped us plan better, come up with more ideas, and eventually it taught us how to optimize all aspects of our project so that we're able to actually to work with PID. 

The first step after planning was of course to start with the computer aided design portion of our project. This was probably the least difficult and least time-consuming part of our project, since it only took one or two days. Looking back at that design process, we could've definitely made our box a little bigger for more room to wire everything up during assembly, and also made the spinner a little bit more prominent, since it is the main element of our project. 

After that, our focus was immediately directed towards wiring and coding our project. We started bit by bit, coding one part at a time, and then putting it all together. This strategy worked very well for us, because it allowed us to tackle one problem at a time, and work out problems one by one. If I, Anton, was to go back and do it all over again, I would definitely try and repurpose some of my old circuitpython code a lot more than I did. I did use certain bits of it, but I don't think I really realized how much easier things would be if I just used my old code which I already worked hard to figure out. Code obviously took up the bulk of the time for our project, but we managed to figure it out eventually, which is a huge achievement. Next to code, something else that did take a good bit to figure out was our wiring. Since our box was quite small, as previously stated, we used a Prototyping Shield for all of our wiring. In retrospect, I think the Prototyping Shield was perfect for our purpose, as it had plenty of power pins and GND pins for us to connect to our various different electronic elements of our project. 

Our biggest regret for this project will forever be the fact that our final project did not have a banana on it. It became a little to tricky to calculate RPM since the banana was not a rectangle. This meant that there were two different intervals between interrupts, so therefore we just decided to make it a normal rectangle. Kind of a bummer since our whole project is called _The Banana of Doom_. 

But other than that unfortunate mishap, everything else went relatively smoothly. Planning out every single week from the beginning really helped us stay on track and not spend too long on one thing. We have both learned a tremendous amount during our process of completing our project, and are very grateful for the help we have recieved, especially from our Teachers, and our classmates. We went from knowing absolutely nothing about PID to being semi-knowledgeable about it, and actually being able to apply PID to our own creation. 
