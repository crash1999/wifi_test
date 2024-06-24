microIoT.microIoT_MQTT_Event(microIoT.TOPIC.topic_0, function (message) {
    microIoT.microIoT_clear()
    microIoT.microIoT_showUserText(0, "The message is:")
    microIoT.microIoT_showUserText(1, message)
    basic.pause(2000)
})
input.onButtonPressed(Button.A, function () {
    microIoT.microIoT_showUserText(0, "Try to send")
    microIoT.microIoT_showUserText(1, "a message")
    microIoT.microIoT_SendMessage("10", microIoT.TOPIC.topic_0)
    basic.pause(1000)
    microIoT.microIoT_clear()
    microIoT.microIoT_showUserText(0, "Doing nothing")
})
let var2 = 0
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI("POCO F5 Pro", "Polpetta96")
// microIoT.microIoT_WIFI("HUAWEI-4464", "12515016")
microIoT.microIoT_showUserText(0, "Doing nothing")
microIoT.microIoT_MQTT(
"9BpjrHUSR",
"9ftC9H8Igz",
"-XrqrNUIg",
microIoT.SERVERS.English
)
basic.forever(function () {
    if (!(input.buttonIsPressed(Button.B))) {
        basic.pause(1000)
    } else {
        microIoT.microIoT_showUserText(0, "Sending " + convertToText(var2))
        microIoT.microIoT_SendMessage(convertToText(var2), microIoT.TOPIC.topic_0)
        var2 = var2 + 1
        if (var2 == 101) {
            var2 = 0
        }
        basic.pause(100)
        microIoT.microIoT_clear()
    }
})
