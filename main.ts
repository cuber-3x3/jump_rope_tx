radio.onReceivedString(function (receivedString) {
    if (receivedString == "START") {
        跳绳个数 = 0
        basic.showLeds(`
            # # # # #
            . # # # .
            . . # . .
            . # . # .
            # # # # #
            `)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 300, 1, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
        跳绳时间 = 60000
        while (跳绳时间 > 0) {
            basic.pause(1000)
            跳绳时间 += -1000
        }
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.happy), SoundExpressionPlayMode.UntilDone)
        radio.sendString("FINISH")
        跳绳时间 = 0
        basic.showLeds(`
            # # # # #
            . # . # .
            . . # . .
            . # # # .
            # # # # #
            `)
    }
})
input.onGesture(Gesture.ThreeG, function () {
    if (跳绳时间 > 0) {
        跳绳个数 += 1
        radio.sendNumber(跳绳个数)
    }
})
let 跳绳时间 = 0
let 跳绳个数 = 0
radio.setGroup(31)
music.setVolume(249)
跳绳个数 = 0
