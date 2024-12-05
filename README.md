# Genmitsu-WiFi-Module-PC-Connect
Connect Genmitsu GGW-UART module with UGS or Candle running on a PC

The Genmitsu CNC machines utilize GRBL firmware, with G-code instructions transmitted over a serial interface. Typically, the machine's GRBL controller connects to a PC via a USB cable, which appears as a COM port on the system. CNC software, such as UGS (https://winder.github.io/ugs_website), communicates with the machine through this COM port to send G-code commands. While the USB connection provides a fast and reliable link to the machine, having a computer physically tethered to the machine in a shop environment can be inconvenient. A wireless connection would be a more practical solution.

In addition to the USB interface, Genmitsu machines typically feature a connector for an Offline Control Module or a Wireless Wi-Fi Module. This connector is a simple UART interface with RX, TX, GND, and +5 VCC pins. The [Genmitsu GGW-U232 Wireless Wi-Fi Module Kit](https://www.amazon.com/gp/product/B0D1BZ987W/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) enables a wireless connection to the machine via an app (available for iOS or Android). The app provides a clean and intuitive interface, allowing users to upload G-code, jog the machine, and more. However, it lacks features such as design creation and visual monitoring that UGS offers. This project aims to connect the Genmitsu PROVerXL 4030 with the GGW-U232 Wireless Wi-Fi Module to a PC running UGS.

## Connect over TCP
Follow the steps to set up the GGW-U232 module with the Genmitsu app normally, as described in its documentation and also in YouTube videos, [such as this one](https://youtu.be/EhqjQdmAdek?si=9t6JqkdQHI0NXC3i). Make sure everything works and you can jog the machine with the app. Then disconnect and close the app, keep the CNC and Wi-Fi module powered on, and open your PC or laptop connected to the same Wi-Fi network. Run the simple Python script, DiscGenm.py, provided here to discover the Genmitsu module and retrieve its information. After being configured with the app, the module broadcasts its info on the network every 1 seconds in the following format:

    {"ip":"192.168.1.x","port":"10086","name":"Gmt_Grbl_xxxx","uuid":"xx:xx:xx:xx:xx:xx"} 

Note the IP address and port number as we need those when connecting with UGS. Open UGS, go to Tools -> Options and select the TCP driver as described here: (https://github.com/winder/Universal-G-Code-Sender/wiki/Connecting-the-Controller#grbl-over-the-network). Then type the host and port information into the “Host” and “Baud” fields in the UGS connection bar, like this:

    Host: 192.168.1.x    Baud: 10086

Then go ahead and select GRBL from the Firmware list **even if it is already selected**. Then click the connect icon and see if you can successfully connect to the module and control the machine. You may get an error message, like "ensure that port number is between 1 and 65535" - just go to the Firmware list and select GRBL again.
