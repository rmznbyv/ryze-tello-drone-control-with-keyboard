from djitellopy import tello
import cv2
import keyboard
from time import sleep

me = tello.Tello()
me.connect()
me.streamon()
print(me.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if keyboard.is_pressed('left'):
        lr = -speed
    elif keyboard.is_pressed('right'):
        lr = speed
    if keyboard.is_pressed('up'):
        fb = speed
    elif keyboard.is_pressed('down'):
        fb = -speed
    if keyboard.is_pressed('w'):
        ud = speed
    elif keyboard.is_pressed('s'):
        ud = -speed
    if keyboard.is_pressed('a'):
        yv = -speed
    elif keyboard.is_pressed('d'):
        yv = speed
    if keyboard.is_pressed('l'):
        me.land()
        sleep(3)
    if keyboard.is_pressed('t'):
        me.takeoff()
    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.005)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (1440, 960))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


 

