def on_button_pressed_a():
    microIoT.microIoT_showUserText(0, "Try to send")
    microIoT.microIoT_showUserText(1, "a message")
    microIoT.microIoT_SendMessage("mess", microIoT.TOPIC.TOPIC_0)
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
    "XrqrNUIg",
    microIoT.SERVERS.CHINA)

def on_forever():
    pass
basic.forever(on_forever)
