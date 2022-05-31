from microbit import *

buttonA = ""

right = Image("09990:"
             "09090:"
             "09990:"
             "09900:"
             "09090")
             
left = Image("09000:"
             "09000:"
             "09000:"
             "09000:"
             "09990")
             
shooter = Image("90009:"
             "99099:"
             "09990:"
             "00900:"
             "00900")

while True:
    a = accelerometer.get_values()
    if button_a.is_pressed():
        buttonA = "True"
    else:
        buttonA = "False"
    print(a[0],buttonA)
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(shooter)
    elif gesture == "right":
        display.show(right)
    elif gesture == "left":
        display.show(left)
    else:
        pass
    sleep(100)