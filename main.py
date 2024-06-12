def on_button_pressed_a():
    microIoT.microIoT_showUserText(0, "Try to send")
    microIoT.microIoT_showUserText(1, "a message")
    microIoT.microIoT_SendMessage("10", microIoT.TOPIC.TOPIC_0)
    basic.pause(1000)
    microIoT.microIoT_clear()
    microIoT.microIoT_showUserText(0, "Doing nothing")
input.on_button_pressed(Button.A, on_button_pressed_a)

microIoT.microIoT_initDisplay()
# microIoT.microIoT_WIFI("POCO F5 Pro", "Polpetta96")
microIoT.microIoT_WIFI("HUAWEI-4464", "12515016")
microIoT.microIoT_showUserText(0, "Doing nothing")
microIoT.microIoT_MQTT("9BpjrHUSR",
    "9ftC9H8Igz",
    "-XrqrNUIg",
    microIoT.SERVERS.ENGLISH)
_var = 0

def on_forever():
    microIoT.microIoT_showUserText(0, "Sending " + convert_to_text(_var))
    microIoT.microIoT_SendMessage(convert_to_text(_var), microIoT.TOPIC.TOPIC_0)
    _var = _var + 1
    if _var == 101: 
        _var = 0
    basic.pause(1000)
    microIoT.microIoT_clear()
basic.forever(on_forever)
