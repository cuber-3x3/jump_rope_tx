def on_received_string(receivedString):
    global 跳绳个数, 跳绳时间
    if receivedString == "START":
        跳绳个数 = 0
        basic.show_leds("""
            # # # # #
                        . # # # .
                        . . # . .
                        . # . # .
                        # # # # #
        """)
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                300,
                1,
                255,
                0,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
        跳绳时间 = 60000
        while 跳绳时间 > 0:
            basic.pause(1000)
            跳绳时间 += -1000
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.happy),
            SoundExpressionPlayMode.UNTIL_DONE)
        radio.send_string("FINISH")
        跳绳时间 = 0
        basic.show_leds("""
            # # # # #
                        . # . # .
                        . . # . .
                        . # # # .
                        # # # # #
        """)
radio.on_received_string(on_received_string)

def on_gesture_three_g():
    global 跳绳个数
    if 跳绳时间 > 0:
        跳绳个数 += 1
        radio.send_number(跳绳个数)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

跳绳时间 = 0
跳绳个数 = 0
radio.set_group(31)
music.set_volume(249)
跳绳个数 = 0