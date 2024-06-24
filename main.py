def on_microiot_mqtt_topic_0(message):
    microIoT.microIoT_clear()
    microIoT.microIoT_showUserText(0, "The message is:")
    microIoT.microIoT_showUserText(1, message)
    basic.pause(2000)
microIoT.microIoT_MQTT_Event(microIoT.TOPIC.TOPIC_0, on_microiot_mqtt_topic_0)

def on_button_pressed_a():
    microIoT.microIoT_showUserText(0, "Try to send")
    microIoT.microIoT_showUserText(1, "a message")
    microIoT.microIoT_SendMessage("10", microIoT.TOPIC.TOPIC_0)
    basic.pause(1000)
    microIoT.microIoT_clear()
    microIoT.microIoT_showUserText(0, "Doing nothing")
input.on_button_pressed(Button.A, on_button_pressed_a)

var2 = 0
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI("POCO F5 Pro", "Polpetta96")
# microIoT.microIoT_WIFI("HUAWEI-4464", "12515016")
microIoT.microIoT_showUserText(0, "Doing nothing")
microIoT.microIoT_MQTT("9BpjrHUSR",
    "9ftC9H8Igz",
    "-XrqrNUIg",
    microIoT.SERVERS.ENGLISH)

def on_forever():
    global var2
    if not (input.button_is_pressed(Button.B)):
        microIoT.microIoT_clear()
        microIoT.microIoT_showUserText(0, "Doing nothing")
        basic.pause(1000)
    else:
        microIoT.microIoT_showUserText(0, "Sending " + convert_to_text(var2))
        microIoT.microIoT_SendMessage(convert_to_text(var2), microIoT.TOPIC.TOPIC_0)
        var2 = var2 + 1
        if var2 == 101:
            var2 = 0
        basic.pause(200)
        microIoT.microIoT_clear()
basic.forever(on_forever)
