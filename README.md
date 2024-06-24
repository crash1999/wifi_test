
# Microbit internet communication system

Send and recieve data with Microbit board over the internet using the DFRobot wifi expantion board. 


> Open this page at [https://crash1999.github.io/wifi_test/](https://crash1999.github.io/wifi_test/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/crash1999/wifi_test** and import

## Edit this project

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/crash1999/wifi_test** and click import

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>


## Getting started

The DFRobot micro:IoT is an affordable expantion board based on the microbit; it has several feature that makes it a good solution for education about IoT. Itcan be found at https://www.dfrobot.com/product-1926.html?tracking=5d9d760421f87
The board offers 3 pin connectors for the GPIO and 2 wire connectors for DC motor, I2C interface, RGB LEDs and an OLED display. 

## Internet connection

The board connects easily at the microbit and it makes possible (according to the manufacturer) to communicate via IFTT, Thingspeak and a DFRobot server. All of the possibility were tested and the aim of this work is to show how to send and recieve data in the easiest way and what are the limits of this system. 

The expantion board connects to WiFi with the dedicated block "setup WiFi name and password" but it can connect only to 2.4 GHz WiFi; this is not addressed by the manufacturer but the connection to a 5 GHz network will fail (the LED indicator will be red). 

## Sending data

The easiest way to send data to a server is to use the DFRobot server. The server requires the setup of an account that has to be setup via phone number because entering an email will lead to a page where a chinese phone number is required. Once the account is set up, there is the possibility to open the topics: a topic is a container for the data that are communicated with a device. 
On the Microbit there is the MQTT setup to initialize this communication and only strings can be sendend as a message. The message can be sent at 100ms delay without any problem in this way. 
On the topic of the server page there is the possibility to plot a graph of the data and there is also the possibility to download the data as an exel file. 
