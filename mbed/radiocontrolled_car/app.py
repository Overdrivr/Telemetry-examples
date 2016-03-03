import tkinter as tk
from pytelemetry.pytelemetry import Pytelemetry
import pytelemetry.transports.serialtransport as transports

pressedKeys = dict()
direction = 0
throttle = 0

# Configure pytelemetry
transport = transports.SerialTransport()
telemetry = Pytelemetry(transport)

def clear():
    global pressedKey
    global direction
    global throttle
    pressedKeys['Up'] = False
    pressedKeys['Down'] = False
    pressedKeys['Left'] = False
    pressedKeys['Right'] = False
    direction = 0
    throttle = 0

def onKeyPress(event):
    global pressedKey
    pressedKeys[event.keysym] = True

def onKeyRelease(event):
    global pressedKey
    pressedKeys[event.keysym] = False

def update():
    global pressedKey
    global direction
    global throttle
    # Update throttle
    if pressedKeys['Up']:
        throttle = min(throttle + throttleGain, 1.0)
    elif pressedKeys['Down']:
        throttle = max(throttle - throttleGain, -1.0)
    elif not pressedKeys['Up'] and not pressedKeys['Down']:
        throttle = 0

    # Update direction
    if pressedKeys['Right']:
        direction = min(direction + directionGain, 1.0)
    elif pressedKeys['Left']:
        direction = max(direction - directionGain, -1.0)
    elif not pressedKeys['Left'] and not pressedKeys['Right']:
        direction = 0

    telemetry.update()
    root.after(10,update)

def pub():
    # Send new data
    telemetry.publish("direction",direction,"float32")
    telemetry.publish("throttle",throttle,"float32")
    #print("D T : %f %f" % (direction, throttle))
    root.after(100,pub)

def printer(topic,data,opts):
    print(topic,":",data)

options = dict()
options['port'] = "COM15"
options['baudrate'] = 115200

# Open connection
transport.connect(options)
telemetry.subscribe(None,printer)

# Start Tk app
root = tk.Tk()
clear()
directionGain = 0.1
throttleGain = 0.03
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.bind('<KeyRelease>', onKeyRelease)
update()
pub()
root.mainloop()

transport.disconnect()
print("Done.")
