# Raspberry Pi RGB LED Strip Controller

![background](background.png)

Control an RGB LED Strip through the web browser. This is a companion to my project on [Hackaday.io](https://hackaday.io/project/162126-raspberry-pi-rgb-led-strip-controller).

## Getting Started

### Prerequisites

* [Raspberry Pi](https://www.raspberrypi.org/)
* [RGB LED Strip controller board](https://hackaday.io/project/162126-raspberry-pi-rgb-led-strip-controller)
* [Python pip](https://pypi.org/project/pip/)
* [pigpio library](http://abyz.me.uk/rpi/pigpio/)
* [Flask](http://flask.pocoo.org/)
* [flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)

### Instructions

1. Install Raspbian.
2. Install prerequisites.
```bash
sudo apt install python3-pip pigpio
sudo pip3 install flask flask-socketio eventlet pigpio
```
3. Install custom pigpiod service.
- Edit pigpiod service file:
```bash
nano /etc/systemd/system/pigpiod.service
```
- Paste the following in it:
```ini
[Unit]
Description=pigpio daemon

[Service]
ExecStart=/usr/bin/pigpiod -g

[Install]
WantedBy=multi-user.target
```
- Save and exit
- Enable and start the service:
```bash
sudo systemctl enable pigpiod.service
sudo systemctl start pigpiod.service
```
4. Download and unpack this repository.
```bash
wget https://github.com/dimitry-ishenko/rgb-led/archive/master.zip
unzip master.zip
mv rgb-led-master rgb-led
```
5. Launch the application:
```bash
cd rgb-led
python3 app.py
```
6. On your computer, open the web browser and navigate to the Pi IP address and port 5000 (eg: `http://192.168.1.1:5000`). You should see the following:
![image](image.png)
7. Control your RGB LED Strip from the browser. How cool.
8. Share and enjoy.

## Authors

* **Dimitry Ishenko** - dimitry (dot) ishenko (at) (gee) mail (dot) com

## License

This project is distributed under the GNU GPL license. See the
[LICENSE.md](LICENSE.md) file for details.

