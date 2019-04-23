# Raspberry Pi RGB LED Strip Controller

Control RGB LED Strip through a web browser.

![background](background.png)

## Getting Started

### Prerequisites

* [Raspberry Pi](https://www.raspberrypi.org/)
* [RGB LED Strip controller board](https://hackaday.io/project/162126-raspberry-pi-rgb-led-strip-controller)
* [Python pip](https://pypi.org/project/pip/)
* [pigpio library](http://abyz.me.uk/rpi/pigpio/)
* [Flask](http://flask.pocoo.org/)
* [flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)

### Installation

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
4. Download and install this repository.
```bash
```

### Usage

1. Launch application (from within the project directory):
```bash
python3 app.py
```
2. Launch your browser and go to your Raspberry Pi IP address, eg: `http://127.0.0.1:5000`

## Authors

* **Dimitry Ishenko** - dimitry (dot) ishenko (at) (gee) mail (dot) com

## License

This project is distributed under the GNU GPL license. See the
[LICENSE.md](LICENSE.md) file for details.

