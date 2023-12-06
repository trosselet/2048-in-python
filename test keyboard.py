import keyboard

shot_pressed = 0
was_pressed = False

while True:
    if keyboard.is_pressed('s'):
            shot_pressed += 1
            print("shot_pressed %d times"%shot_pressed)
            was_pressed = True
    else:
        was_pressed = False