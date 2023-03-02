from djitellopy import tello
import cv2
import keyboard
from time import sleep

me = tello.Tello()
me.connect()
me.streamon()

speed = 50

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
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
        sleep(1)
    if keyboard.is_pressed('t'):
        me.takeoff()
        sleep(1)
    if keyboard.is_pressed('h'):
        me.flip_right()
        sleep(1)
    if keyboard.is_pressed('g'):
        me.flip_left()
        sleep(1)
    if keyboard.is_pressed('b'):
        me.flip_back()
        sleep(1)
    if keyboard.is_pressed('y'):
        me.flip_forward()
        sleep(1)
    if keyboard.is_pressed('+'):
        speed = speed+10
    if keyboard.is_pressed('-'):
        speed = speed-10
    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    battery_view= me.get_battery()
    altitude_view = vals[2]
    speed_view = speed/10
    sleep(0.001)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (1440, 960))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,
                "Battery: " + str(battery_view),
                (50, 50),
                font, 1,
                (0, 0, 255),
                2, cv2.LINE_4)
    cv2.putText(img,
                "Altitude: " + str(altitude_view),
                (50, 150),
                font, 1,
                (0, 255, 0),
                2, cv2.LINE_4)
    cv2.putText(img,
                "Speed: " + str(speed_view),
                (50, 250),
                font, 1,
                (255, 0, 0),
                2, cv2.LINE_4)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
